import io
import tempfile
import subprocess

try:
    from subprocess import DEVNULL
except ImportError:
    DEVNULL = open('/dev/null', 'w')

from django import forms
from django.core import checks
from django.db import models
from django.utils.translation import ugettext_lazy as _


class VideoFormField(forms.FileField):
    default_error_messages = {
        'invalid_video': _(
            'Upload a valid video. The file you uploaded was either not an '
            'video or a corrupted video.'
        )
    }

    def to_python(self, data):
        f = super(VideoFormField, self).to_python(data)

        if f is None:
            return None

        if hasattr(data, 'temporary_file_path'):
            input_file = data.temporary_file_path()
        else:
            if hasattr(data, 'read'):
                content = data.read()
            else:
                content = data['content']

            fd, input_file = tempfile.mkstemp()

            with io.open(fd, 'w') as f:  # this works on Python 2?
                f.write(str(content))

        # tries to open the video file with ffmpeg to check his integrity
        exit_code = subprocess.call([
            'ffmpeg',
            '-v', 'quiet',     # don't print messages
            '-i', input_file,  # input file
            '-f', 'null',      # format is null because we don't really want to convert anything
            '-'                # output to nowhere
        ], stdout=DEVNULL, stderr=DEVNULL)

        # TODO: if file is an image ffmpeg dont exit with error code
        # we should use ffprobe and analyze the output too

        if not exit_code == 0:
            raise forms.ValidationError(
                self.error_messages['invalid_video'],
                code='invalid_video'
            )

        if hasattr(f, 'seek') and callable(f.seek):
            f.seek(0)

        return f


class VideoField(models.FileField):
    description = _('Video')

    def __init__(self, *args, **kwargs):
        self.width_field = kwargs.pop('width_field', None)
        self.height_field = kwargs.pop('height_field', None)
        self.duration_field = kwargs.pop('duration_field', None)
        self.size_field = kwargs.pop('size_field', None)
        self.thumbnail_field = kwargs.pop('thumbnail_field', None)

        super(VideoField, self).__init__(*args, **kwargs)

    def check(self, **kwargs):
        errors = super(VideoField, self).check(**kwargs)
        errors.extend(self._check_ffmpeg_installed())

        return errors

    def _check_ffmpeg_installed(self):
        exit_code = subprocess.call(['which', 'ffmpeg'], stdout=DEVNULL)

        if not exit_code == 0:
            return [
                checks.Error(
                    'Cannot use VideoField because ffmpeg is not installed.',
                    hint='Get ffmpeg at https://ffmpeg.org/download.html',
                    obj=self,
                    id='videofield.E001',
                )
            ]

        return []

    def deconstruct(self):
        name, path, args, kwargs = super(VideoField, self).deconstruct()

        if self.width_field:
            kwargs['width_field'] = self.width_field
        if self.height_field:
            kwargs['height_field'] = self.height_field
        if self.duration_field:
            kwargs['duration_field'] = self.duration_field
        if self.size_field:
            kwargs['size_field'] = self.size_field
        if self.thumbnail_field:
            kwargs['thumbnail_field'] = self.thumbnail_field

        return name, path, args, kwargs

    def formfield(self, **kwargs):
        defaults = {'form_class': VideoFormField}
        defaults.update(kwargs)

        return super(VideoField, self).formfield(**defaults)

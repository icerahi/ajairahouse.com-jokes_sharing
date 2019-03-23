from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from .models import Logo


l=Logo.objects.last()

# Create your views here.
def policy(request):

    context={"l":l,
    'title':'Privacy Policy'}
    return render(request,'policy.html',context)
def terms(request):
    context={"l":l,
    'title':'Terms and Conditions'}
    return render(request,'terms.html',context)

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('messageText')

        from_email = settings.EMAIL_HOST_USER
        to_email = ['zanjarwhite@gmail.com']
        subject = "Mail From AjairaHouse"
        body = "Name : {} \n Email : {} \n Message : {}".format(name,email,message)
        msg = EmailMultiAlternatives(subject, body, from_email, to_email)
        msg.send()

        messages.success(request, 'Your message has been send Successfully')
    return render(request,'contact.html',{'title':'contact','l':l})

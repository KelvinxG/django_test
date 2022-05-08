from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
# Create your views here.

def index(request):
    #send email
    # if request.method =="POST":
    #     send_mail(
    #         'Subject here',
    #         'Here is the message.',
    #         'This is a content',
    #         ['tearteamoguy@gmail.com'] )
    #     return HttpResponse("Email sent")
    if request.method == 'POST':
        receiver=request.POST.get('receiver')
        subject=request.POST.get('subject')
        content=request.POST.get('content')
        send_mail(
            receiver,
            subject,
            content,
            ['tearteamoguy@gmail.com'],fail_silently=False )
        print("sent")

    return render(request,'app/index.html')

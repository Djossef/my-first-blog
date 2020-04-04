from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.core.mail import send_mail


def sendMails(request):
    if request.method == 'POST':
        your_name = request.POST['yourname']
        your_email = request.POST['youremail']
        your_phone = request.POST['yourphone']
        your_message = request.POST['yourmessage']
        send_mail('from My Blog', "Hi I am " + your_name + " My number phone is : " + your_phone + your_message,
                  your_email, ['Djossef.msf@gmail.com'], fail_silently=False)


def home(request):
    sendMails(request)
    return render(request, 'blog/home.html', {})


def post_list(request):
    sendMails(request)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

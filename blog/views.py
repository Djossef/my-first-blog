from django.shortcuts import render

from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from marketing.models import Signup
from marketing.forms import EmailSignupForm


def home(request):
    form = EmailSignupForm()
    return render(request, 'blog/home.html', {'form': form})


def post_list(request):
    form = EmailSignupForm()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'form': form})

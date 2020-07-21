from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render
from .models import Post, Comment
from django.utils import timezone
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.conf import settings
from marketing.models import Signup
from marketing.forms import EmailSignupForm
from blog.forms import CommentForm


def home(request):
    form = EmailSignupForm()
    return render(request, 'blog/home.html', {'form': form})


def post_list(request):
    form = EmailSignupForm()
    commentForm = CommentForm()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    comments = Comment.objects.all()
    return render(request, 'blog/post_list.html',
                  {'posts': posts, 'form': form, 'commentForm': commentForm, 'comments': comments})


def comment_Manip(request):
    if request.method == "POST":
        commentText = request.POST['comment']
        post_title = request.POST['post_title']
        commenter = request.POST['commenter']
        post = Post.objects.filter(title=post_title)
        postList = list(post)
        commenter = User.objects.filter(username=commenter)
        commenterList = list(commenter)
        comment = Comment.objects.create(comment=commentText, post=postList[0], commenter=commenterList[0])

        comment.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def post_detail(request, post_title):
    form = EmailSignupForm()
    post = get_object_or_404(Post, title=post_title)
    comments = Comment.objects.all()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})


def covid_tracker(request):
    return render(request, 'covid.html')

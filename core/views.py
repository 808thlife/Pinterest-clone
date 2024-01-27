from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .utils import update_view_counter
from .models import Post

# Create your views here.
@login_required(login_url = settings.LOGIN_URL)
def index(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request, "core/index.html", context)

def post(request, id):
    post = Post.objects.get(id = id)
    update_view_counter(post)
    context = {"post":post}
    return render(request, "core/post.html", context)

def profile(request, id):
    user = User.objects.get(id = id)


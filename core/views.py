from django.shortcuts import render
from .utils import update_view_counter
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request, "core/index.html", context)

def post(request, id):
    post = Post.objects.get(id = id)
    update_view_counter(post)
    context = {"post":post}
    return render(request, "core/post.html", context)


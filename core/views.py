from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request, "core/index.html", context)

def post(request, id):
    return render(request, "core/post.html")


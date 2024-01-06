from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name = "index"),
    path("post/<int:id>", views.post, name = "post")
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
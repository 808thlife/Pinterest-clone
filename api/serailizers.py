from rest_framework import serializers
from core.models import Tag, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'photo']


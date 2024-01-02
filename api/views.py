from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class PostModelView(APIView):
    permission_clases = [IsAuthenticated]
    #getting all Posts
    def get(self, request):
       pass

    #creating a Post
    def post(self, request):
       pass

    #Update Post
    def put(self, request, id):
        
       pass
        

    #Delete Post
    def delete(self, request, id):
        
        pass
    

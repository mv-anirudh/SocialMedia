from urllib import response
from django.shortcuts import render

from rest_framework.generics import  CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from socialapp.serializers import UserSerializer,PostSerializer,CommentSerializer

from socialapp.models import Post

from rest_framework import authentication,permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class SignUpView(CreateAPIView):

    serializer_class=UserSerializer

class PostListCreateView(ListAPIView,CreateAPIView):

    queryset=Post.objects.all()

    serializer_class=PostSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(owner=self.request.user)

class PostRetrieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    
class PostLikeView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):
    
        id=kwargs.get("pk")
    
        post_object=Post.objects.get(id=id)
    
        post_object.liked_by.add(request.user)

        return Response(data={"message":"liked"})


class PostCommentCreateView(CreateAPIView):
    
    serializer_class=CommentSerializer
    
    
    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]
    
    
   

  
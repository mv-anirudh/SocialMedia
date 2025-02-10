from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from socialapp.serializers import UserSerializer,PostSerializer,CommentSerializer,ProfileSerializer

from socialapp.models import Post,Profile

from rest_framework import authentication,permissions

from rest_framework.views import APIView

from socialapp.permissions import IsOwnerOnly,IsOwnerOrReadOnly

class SignUpView(CreateAPIView):

    serializer_class=UserSerializer

class PostListCreateView(ListAPIView,CreateAPIView):

    queryset=Post.objects.all()

    serializer_class=PostSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(owner=self.request.user)

    def get_serializer_context(self):

        context=super().get_serializer_context()

        context["request"]=self.request

        return context

class PostRetrieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[IsOwnerOrReadOnly]

class PostLikeView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        post_object=Post.objects.get(id=id)

        liked=False

        if request.user in post_object.liked_by.all():

            post_object.liked_by.remove(request.user)

        else:

            post_object.liked_by.add(request.user)

            liked=True

        return Response(data={"message":"ok","liked":liked})

class PostCommentView(CreateAPIView):

    serializer_class=CommentSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):

        serializer_instance=self.serializer_class(data=request.data)

        id=kwargs.get("pk")

        post_object=Post.objects.get(id=id)

        if serializer_instance.is_valid():

            serializer_instance.save(post=post_object,owner=request.user)

            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)

class UserProfileView(UpdateAPIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=ProfileSerializer

    def get_object(self):

        return Profile.objects.get(owner__username=self.request.user)

    


from django.shortcuts import render
from socialapp.serializers import UserSerializer
from rest_framework.generics import CreateAPIView

# Create your views here.

class UserprofileView(CreateAPIView):
    
    serializer_class=UserSerializer
    
    
    
    

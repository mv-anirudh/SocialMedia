from django.urls import path
from socialapp import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns =[
    path("signup/",views.SignUpView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
    path("posts/",views.PostListCreateView.as_view()),

    path("posts/<int:pk>/",views.PostRetrieveUpdateDestroyView.as_view()),
    path("posts/<int:pk>/add-like/",views.PostLikeView.as_view()),

]
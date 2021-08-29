from django.urls import path
from . import views
app_name="awesome_store"
urlpatterns=[
    path('',views.Index.as_view(),name='index'),
    path('register',views.Register.as_view(),name='register'),
    path('login',views.UserLogin.as_view(),name='login'),
    path('logout', views.UserLogout.as_view(), name='logout'),
    path('profile',views.Profile.as_view(),name='profile'),
]
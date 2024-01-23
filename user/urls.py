from django.urls import path
from .views import register,profile,profile_update
urlpatterns=[
      path('register/',register,name='register'),
      path('profile/',profile,name='profile'),
      path('profile_update/',profile_update,name='profile_update')
]
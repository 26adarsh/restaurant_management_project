from django.urls import path
from .views import *

user_profile=UserProfileViewSet.as_view({'put':'update'})

urlpatterns = [
    path('profile/',user_profile,name='user-profile-update'),
]
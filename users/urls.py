from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import *

urlpatterns:list = [
    path(
        'api/login', TokenObtainPairView.as_view(),
        name="You can get your jwt token from here"
    ),
    
    path(
        'api/refresh', TokenRefreshView.as_view(),
        name="You can refresh jwt token from here if your jwt is expired"
    ),

    path(
        'api/getUser', get_user,
        name="This endpoint returns user info by jwt token in auth header"),

    path(
        'api/fetchUsers', fetch_users,
        name="This endpoint returns ALL information about USERS. * Only for admins"
    )

]

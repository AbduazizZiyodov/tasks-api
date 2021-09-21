from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.urls.conf import include

from .views import home
from .yasg import schema_view


urlpatterns: list = [
    path('admin/', admin.site.urls),

    path('', include('users.urls')),
    path('', include('tasks.urls')),

    url(
        r'^(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(
            cache_timeout=0
        ),
        name='schema-json'
    ),
    url(
        r'^$', schema_view.with_ui(
            'swagger',
            cache_timeout=0
        ), 
        name='schema-swagger-ui'
    ),
]

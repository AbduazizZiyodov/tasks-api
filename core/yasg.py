from rest_framework.permissions import AllowAny

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="Tasks API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(AllowAny,),
)
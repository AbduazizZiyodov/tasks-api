from rest_framework.permissions import AllowAny

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="Tasks-API",
        default_version="v1",
        description="Simple API for managing tasks written DRF",
        contact=openapi.Contact(
            "Abduaziz Ziyodov",
            "https://github.com/AbduazizZiyodov",
            "abduaziz.ziyodov@mail.ru"
        ),
        license=openapi.License("MIT")
    ),
    public=True,
    permission_classes=(AllowAny,),
)

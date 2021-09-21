from django.contrib.auth import get_user_model

from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

from .serializers import UserSerializer


User = get_user_model()

class FetchUsersView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer

class GetUserView(RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        pk = self.request.user.pk

        if pk is not None:
            self.kwargs['pk'] = pk

        return super(GetUserView, self).get_object()



get_user, fetch_users = GetUserView.as_view(), FetchUsersView.as_view()

__all__ = ["get_user", "fetch_users", ]

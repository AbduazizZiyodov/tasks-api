from django.http import HttpRequest
from rest_framework.permissions import BasePermission

from .utils import can

class CanRead(BasePermission):
    def has_permission(self, request: HttpRequest, view) -> bool:
        return can(request, "read")


class CanCreate(BasePermission):
    def has_permission(self, request: HttpRequest, view) -> bool:
        return can(request, "create")


class CanUpdate(BasePermission):
    def has_permission(self, request: HttpRequest, view) -> bool:
        return can(request, "update")


class CanDelete(BasePermission):
    def has_permission(self, request: HttpRequest, view) -> bool:
        return can(request, "delete")

__all__ = ["CanRead","CanCreate","CanUpdate","CanDelete",]

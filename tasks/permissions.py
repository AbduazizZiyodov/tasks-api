from django.http import HttpRequest
from rest_framework.permissions import BasePermission


def can(request: HttpRequest, action: str) -> bool:
    if request.user.is_superuser:
        return True

    permissions: dict[str, int] = {
        "read": "tasks.view_task",
        "create": "tasks.add_task",
        "update": "tasks.change_task",
        "delete": "tasks.delete_task"
    }

    return request.user.has_perm(permissions[action])


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


__all__ = ["CanRead", "CanCreate", "CanUpdate", "CanDelete", ]

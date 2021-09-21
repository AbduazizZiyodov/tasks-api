from django.http import HttpRequest

def get_groups_of_user(request: HttpRequest) -> set:
    return set(
        [
            group.name
            for group in request.user.groups.all()
        ]
    )


def can(request: HttpRequest, action: str) -> bool:
    if request.user.is_superuser:
        return True

    permissions: dict[str, set] = {
        "read": {"student", "supervisor", "reviewer"},
        "create": {"student", "supervisor"},
        "update": {"student", "supervisor"},
        "delete": {"student"}
    }

    groups: list = get_groups_of_user(request)

    return bool(permissions[action] & groups)

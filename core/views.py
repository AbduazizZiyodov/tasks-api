from django.http import JsonResponse
from django.http import HttpRequest



def home(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        {
            "message": "API is working 🔥"
        }
    )
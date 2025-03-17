from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def hello_name(request):
    """
    A simple view that returns 'Hello, {name}, you are {age} years old and speak {language}' in JSON format.
    Uses query parameters: 'name', 'age', and 'language'.
    """
    name = request.GET.get("name", "World")
    age = request.GET.get("age", None)
    language = request.GET.get("language", "English").strip()

    if age is not None:
        try:
            age = int(age)
            if age < 0:
                return JsonResponse({"error": "Age must be a positive number."}, status=400)
        except ValueError:
            return JsonResponse({"error": "Invalid age format. Age must be a number."}, status=400)

    if not language:
        return JsonResponse({"error": "Language must not be empty."}, status=400)

    return JsonResponse({
        "message": f"Hello, {name}! You are {age} years old and speak {language}."
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_name),  # Keep the hello world API
    path('api/', include('product.urls')),  # Corrected the product API route
]

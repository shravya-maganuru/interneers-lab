'''
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world! I am Shravya Maganuru")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
]
'''
# django_app/urls.py

from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def hello_name(request):
    """
    A simple view that returns 'Hello, {name}, you are {age} years old and speak {language}' in JSON format.
     Uses query parameters: 'name', 'age', and 'language'.
    """
    # Gets query parameters with default values
    name = request.GET.get("name", "World")
    age = request.GET.get("age", None)
    language = request.GET.get("language", "English").strip()

    # Validates age (must be a positive number)
    if age is not None:
        try:
            age = int(age)
            if age < 0:
                return JsonResponse({"error": "Age must be a positive number."}, status=400)
        except ValueError:
            return JsonResponse({"error": "Invalid age format. Age must be a number."}, status=400)

    # Validates language (must be a non-empty string)
    if not language:
        return JsonResponse({"error": "Language must not be empty."}, status=400)

    return JsonResponse({
        "message": f"Hello, {name}! You are {age} years old and speak {language}."
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_name),
    # Example usage: /hello/?name=Alice&age=30&language=German
    # Response: {"message": "Hello, Alice! You are 30 years old and speak German."}
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),  # Ścieżka dla aplikacji polls
    path('', include('polls.urls')),  # Dodaj to, jeśli chcesz, aby "/polls/" była także stroną główną
]


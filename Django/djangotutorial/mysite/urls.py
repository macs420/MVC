from django.contrib import admin
from django.urls import path, include
from polls import views

urlpatterns = [
    path('', views.home, name='home'),
    path('polls/', include('polls.urls')),  
    path('admin/', admin.site.urls),  
]

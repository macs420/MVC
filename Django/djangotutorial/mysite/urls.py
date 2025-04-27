from django.contrib import admin
from django.urls import path, include
from polls import views as polls_views 
from mysite.views import home 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('polls/', include('polls.urls')),
]

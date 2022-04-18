from django.contrib import admin
from django.urls import path, include

from leads.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', home),
    path('leads/', include('leads.urls', namespace='leads'))
]

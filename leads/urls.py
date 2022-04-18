from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', leads_lists),
    path('<int:pk>/', lead_detail, name = "detallar"),
    path('<int:pk>/update_detail', lead_update, name = "ozgartirish"),
    path('<int:pk>/delete_detail', lead_delete, name = "ochirish"),
    path('create-yaratish/', lead_create, name = "lead-create")
]
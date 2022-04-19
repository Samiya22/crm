from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', ListsView.as_view(), name="listlar"),
    path('<int:pk>/', LeadDetailView.as_view(), name = "detallar"),
    path('<int:pk>/update_detail', LeadUpdateView.as_view(), name = "update"),
    path('<int:pk>/delete_detail', LeadDeleteView.as_view(), name = "delete"),
    path('create-yaratish/', LeadCreateView.as_view(), name = "lead-create")
]
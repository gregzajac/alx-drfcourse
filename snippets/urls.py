from django.urls import path
from snippets import views

urlpatterns = [
    path("", views.snippet_list),  # /api/v1/snippets/
    path("<int:pk>/", views.snippet_detail)  # /api/v1/snippets/1/
]
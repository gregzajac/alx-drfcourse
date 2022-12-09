from django.urls import path
from snippets import views

urlpatterns = [
    path("", views.SnippetList.as_view()),  # /api/v1/snippets/
    path("<int:pk>/", views.SnippetDetail.as_view())  # /api/v1/snippets/1/
]
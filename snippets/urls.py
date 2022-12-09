from django.urls import path
from snippets import views

urlpatterns = [
    path("snippets/", views.SnippetList.as_view()),  # /api/v1/snippets/
    path("snippets/<int:pk>/", views.SnippetDetail.as_view()) , # /api/v1/snippets/1/
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
]
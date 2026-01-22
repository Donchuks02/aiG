from django.urls import path

from image_editor import views

urlpatterns = [
    path('api/prompts/', views.PromptListView.as_view(), name='prompt-list'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('generate-story/', views.generate_story, name='generate_story'),
    path('get-stories/', views.get_all_stories, name='get_all_stories'),
]

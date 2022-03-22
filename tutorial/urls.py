from django.urls import path
from . import views

urlpatterns = [
    path('tutorials', views.tutorial_list),
    path('tutorials/<str:pk>', views.tutorial_detail),
    path('tutorials/published/', views.tutorial_list_published),
]

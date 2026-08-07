
from django.urls import path
from . import views

urlpatterns = [
    path('', views.web_list, name='web_list'),
    path('create/', views.web_created, name='web_created'),
    path('<int:web_id>/edit/', views.web_edit, name='web_edit'),
    path('<int:web_id>/delete/', views.web_delete, name='web_delete'),
]

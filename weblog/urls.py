from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_category, name='show_category'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('llists/<int:category_id>/', views.post_list, name='post_list'),  
    path('user_pins/', views.user_pins, name='user_pins'),  # مسیر جدید
]

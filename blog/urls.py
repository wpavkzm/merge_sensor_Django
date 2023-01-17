from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('radar_info', views.radar_info, name='radar_list'),
    path('ir_info', views.ir_info, name='ir_list'),
]

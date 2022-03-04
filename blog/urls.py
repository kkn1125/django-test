from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('post/<int:num>', views.post_control, name = 'post_control'),
    path('form', views.post_form, name = 'post_form'),
]
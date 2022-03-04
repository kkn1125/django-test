from django.urls import path
from . import views

urlpatterns = [
    # path('', views.PostView.as_view(), name = 'post_list'),
    # path('post/<int:num>', views.PostView.as_view(), name = 'post_detail'),
    path('', views.post_list, name = 'post_list'),
    path('post/<int:num>', views.post_control, name = 'post_control'),
    path('form', views.post_form, name = 'post_form'),
]

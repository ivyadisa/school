from django.urls import path
from .views import *

urlpatterns = [
    path('uploads/', upload_blogs, name='uploads'),
    path('', list_blogs, name='blogs'),
    path('blogs/<int:blog_id>/', detail_blogs, name='blog-detail'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('register/', register_user, name="register"),
]

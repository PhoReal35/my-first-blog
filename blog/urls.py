from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views  # rename to avoid confusion
from . import views  # your app's views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path('post/new/', views.post_new, name='post_new'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),   # auth_views.LoginView here
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout')
]

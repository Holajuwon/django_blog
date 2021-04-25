from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogEditView, BlogDeleteView, UserRegisterView, UserResetPassword
from blog import views


urlpatterns = [
  path('user/reset', UserResetPassword.as_view(), name='password_reset'),
  path('user/logout/', views.logout_view, name='user_logout'),
  path('user/login/', views.login_request, name='user_login'),
  path('user/register/', UserRegisterView.as_view(), name='user_register'),
  path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
  path('post/<int:pk>/edit/', BlogEditView.as_view(), name='post_edit'),
  path('post/new/', BlogCreateView.as_view(), name='post_new'),
  path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
  path('', BlogListView.as_view(), name='home'),
]
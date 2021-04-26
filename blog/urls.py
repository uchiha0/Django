from django.urls import path
from django.contrib.auth import views as auth_views
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, AddCommentView, register, profile, password_reset_request


urlpatterns = [
   path('register/', register, name = 'register'),
   path('profile/', profile, name = 'profile'),
   path('login/', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
   path('logout/', auth_views.LogoutView.as_view(template_name= 'logout.html'), name = 'logout'),

   path("password_reset/", password_reset_request, name="password_reset"),
   path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
   path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),      

   path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name = 'post_delete'),
   path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name = 'post_edit'),
   path('post/new/', BlogCreateView.as_view(), name= 'post_new'),
   path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'), 
   path('post/<int:pk>/comment', AddCommentView.as_view(), name = 'add_comment'), 
   path('', BlogListView.as_view(), name = 'blog-home'),
]

from django.urls import path
from django_app import views

app_name = 'django_app'
urlpatterns = [
    path('', views.home_view, name=''),
    path('index/', views.HomeView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),

    # path('post/ratings/', views.posts),
    path('post_list/', views.post_list, name='post_list'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/detail/', views.post_detail, name='post_detail'),
    path('home_main/', views.home_main, name='home_main'),
    path('post/<int:pk>/comment/create/', views.post_comment_create, name='post_comment_create'),
    path('post/<int:pk>/comment/delete/', views.post_comment_delete, name='post_comment_delete'),
    path('post_create/', views.post_create, name='post_create'),
    path('logout/', views.logout_f, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.profileupdate, name='profile_update'),
]
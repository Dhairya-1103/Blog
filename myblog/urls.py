from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', blog_views.post_list, name='post_list'),
    path('tag/<slug:slug>/', blog_views.post_list, name='post_list_by_tag'),
    path('post/<int:pk>/', blog_views.post_detail, name='post_detail'),
    path('post/new/', blog_views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', blog_views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', blog_views.post_delete, name='post_delete'),
    path('post/<int:pk>/comment/', blog_views.add_comment, name='add_comment'),
    path('search/', blog_views.search, name='search'),
]

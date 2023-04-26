from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from posts.views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDetailView,
    PostDeleteView,
    home,
    like,
    post_following
    
  
    
)


urlpatterns = [
  
    path('Rhan/', admin.site.urls),
    path('', home,name='list'),
   
    path('posts_following/',post_following,name='posts_following'),  
    path('create/',PostCreateView.as_view(),name='create'),  
    path('like/<slug>', like,name='like'), 
    path('<slug>/',PostDetailView.as_view(),name='detail'),
    path('<slug>/update/',PostUpdateView.as_view(),name='update'),
    path('<slug>/delete/',PostDeleteView.as_view(),name='delete'),
    # path('accounts/', include('allauth.urls')), 

    
    path('users/', include('users.urls',namespace='users')), 
   

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path,re_path
from . import views
from posts.views import followers
from django.conf import settings
from django.conf.urls.static import static


app_name = 'users'

urlpatterns = [
    path('perfil_create/', views.Perfil_user, name='perfil_create'),
     path('perfiles/', views.perfiles_all, name='perfiles'),
    path('perfil/<int:id>/', views.perfiles, name='perfil'),
    path('register/', views.Register, name='register'),
    path('login/', views.IniciaSession, name='login'),
    path('logout/', views.logoute, name='logout'),
    path('follower/<int:id>/', followers, name='follower'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






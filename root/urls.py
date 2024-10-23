from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from django.contrib.auth.views import LogoutView
from myapp.views import user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('library/', views.library, name='library'),
    path('download/<int:cheatsheet_id>/', views.download_cheatsheet, name='download_cheatsheet'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

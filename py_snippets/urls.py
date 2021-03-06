from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/profile/', users_views.ProfileView.as_view(), name='profile'),
    path('accounts/', include('allauth.urls')),
    path('api/', include('api.urls')),
    path('', include('website.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app_seguridad import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cajero/', include('app_transacciones.urls')),
    path('', views.index),
    path('login/', views.log_in, name="login_view"),
    path('logout/', views.log_out, name="logout_view"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),

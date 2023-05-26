
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    # Optional UI:
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='docs'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='api-schema'), name='redoc'),
]

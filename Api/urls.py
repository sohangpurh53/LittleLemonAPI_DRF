from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Main.urls')),
    path('api/users/', include('djoser.urls')),
    path('api/tokens/login/', TokenObtainPairView.as_view()),
    path('api/tokens/refresh/', TokenRefreshView.as_view())
]

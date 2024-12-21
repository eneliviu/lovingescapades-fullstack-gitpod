from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import root_route  # , logout_route

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),

    # For the browsable API login and logout views
    path('api/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # app urls
    path('', include('user_profile.urls')),

]

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from api.views import (
    ParentViewset,
    StudentViewset,
    BusViewset,
    ReceiptViewset,
)

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'student', StudentViewset)
router.register(r'parent', ParentViewset)
router.register(r'bus', BusViewset)
router.register(r'receipt', ReceiptViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
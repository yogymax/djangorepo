from electornics.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'eproducts', ElectornicProducts, basename='etcprod')
router.register(r'evendor', VendorProducts, basename='etcven')

urlpatterns = router.urls
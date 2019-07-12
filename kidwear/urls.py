from kidwear.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'kproducts', ClothProducts, basename='etcprod')
router.register(r'kvendor', VenProducts, basename='etcven')

urlpatterns = router.urls
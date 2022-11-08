from django.urls import path, include

from rest_framework.routers import DefaultRouter
from apps.products.api_views import ProductApiViewSet, MovementApiViewSet

router = DefaultRouter()
router.register("products", ProductApiViewSet)
router.register("movements", MovementApiViewSet)


urlpatterns = [path("", include(router.urls))]

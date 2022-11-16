from django.urls import path, include

from rest_framework.routers import DefaultRouter
from apps.products.api_views import ProductApiViewSet

router = DefaultRouter()
router.register("products", ProductApiViewSet)


urlpatterns = [path("", include(router.urls))]

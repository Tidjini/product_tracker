from django.urls import path, include

from rest_framework.routers import DefaultRouter
from apps.products.api_views import ProductApiViewSet
from apps.encaissements.api_views import EncaissementViewSet

router = DefaultRouter()
router.register("products", ProductApiViewSet)
router.register("encaissements", EncaissementViewSet)


urlpatterns = [path("", include(router.urls))]

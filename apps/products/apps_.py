from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name: str = "products"
    verbose_name: str = "products application"

    def ready(self) -> None:
        from . import signals

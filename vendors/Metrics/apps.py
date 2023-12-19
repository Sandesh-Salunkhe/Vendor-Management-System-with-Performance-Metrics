from django.apps import AppConfig


class MetricsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Metrics"

    def ready(self):
        import Metrics.signals

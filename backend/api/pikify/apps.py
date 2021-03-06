from django.apps import AppConfig


class PikifyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pikify'

    def ready(self):
        import pikify.signals

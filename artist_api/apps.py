from django.apps import AppConfig


class ArtistApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artist_api'

    def ready(self):
        import artist_api.signals
from django.apps import AppConfig


class ProfilesApiConfig(AppConfig):
    name = 'profiles_api'

    def ready(self):
        import profiles_api.signals

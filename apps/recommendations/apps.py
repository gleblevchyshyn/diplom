from django.apps import AppConfig


class RecommendationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.recommendations'

    def __init__(self, app_name, app_module):
        super().__init__(app_name, app_module)
        self.recommendation_system = None

    def ready(self):
        print("READY METHOD")
        from .recommendations import RecommendationSystems
        self.recommendation_system = RecommendationSystems()

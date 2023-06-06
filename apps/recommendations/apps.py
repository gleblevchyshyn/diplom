from django.apps import AppConfig



class RecommendationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.recommendations'
    recommendation_system = None

    def ready(self):
        from recommendations import RecommendationSystems

        # Create an instance of your recommendation system
        self.recommendation_system = RecommendationSystems()


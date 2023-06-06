from django.shortcuts import render
from apps import RecommendationsConfig

# Create your views here.
def top_books():
    rec_sys = RecommendationsConfig.recommendation_system

    return 0

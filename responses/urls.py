from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeedbackViewSet

# Criando o roteador e registrando a viewset
router = DefaultRouter()
router.register(r'feedback', FeedbackViewSet)

# Incluindo as URLs do roteador
urlpatterns = [
    path('', include(router.urls)),
]

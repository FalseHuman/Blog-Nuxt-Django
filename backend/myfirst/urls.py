from rest_framework import routers
from django.urls import path, include
from .views import ArticleViewSet, CommentViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.SimpleRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'comment', CommentViewSet)

# URLs настраиваются автоматически роутером
urlpatterns = [
    path("", include(router.urls)),
]
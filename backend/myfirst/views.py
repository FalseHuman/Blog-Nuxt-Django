from rest_framework import viewsets

from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-pub_date')
    serializer_class = ArticleSerializer
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-comm_date')
    serializer_class = CommentSerializer
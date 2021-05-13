from rest_framework import viewsets, status
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response

from rest_framework.decorators import action
from rest_framework import filters

class ArticleViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['title', 'story', 'author__fname', "author__lname", 'author__mname']

	@action(detail=False)
	def get_by_category(self, request):
		cat = self.request.query_params.get('category', None)
		articles = Article.objects.filter(category = cat)
		serializer = self.get_serializer(articles, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	@action(detail=False)
	def get_by_author(self, request):
		author = self.request.query_params.get('author', None)
		articles = Article.objects.filter(author__account = author)
		serializer = self.get_serializer(articles, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	@action(detail=True, methods=['get','put'])
	def publish(self, request, pk):
		article = self.get_object()
		article.published = True
		article.save()
		return Response({'response':'Article published'})


	@action(detail=True, methods=['get','put'])
	def unpublish(self, request, pk):
		article = self.get_object()
		article.published = False
		article.save()
		return Response({'response':'Article unpublished'})


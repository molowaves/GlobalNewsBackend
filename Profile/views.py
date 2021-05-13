from rest_framework import viewsets
from .models import Journalist, Reader
from .serializers import JournalistSerializer, ReaderSerializer


class JournalistViewSet(viewsets.ModelViewSet):
	queryset = Journalist.objects.all()
	serializer_class = JournalistSerializer
	lookup_field = 'account'	

class ReaderViewSet(viewsets.ModelViewSet):
	queryset = Reader.objects.all()
	serializer_class = ReaderSerializer
	lookup_field = 'account'

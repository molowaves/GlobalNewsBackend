from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'', views.ArticleViewSet)

urlpatterns = [
	path('', include(router.urls))
]

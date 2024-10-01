from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib import admin

router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('book.urls')),
]

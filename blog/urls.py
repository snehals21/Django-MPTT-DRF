from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"book", views.BookViewSet)
router.register(r"chapter", views.ChapterViewSet)
app_name = 'blog'

urlpatterns = [
    path('', include(router.urls)),
]

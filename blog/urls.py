from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"book", views.BookViewSet)
router.register(r"chapter", views.ChapterViewSet)
app_name = 'blog'

urlpatterns = [
    path('', include(router.urls)),
    path('chapter/get-child/<int:pk>/', views.ChapterViewSet.as_view({'get': 'get_child'})),
    path('chapter/get-parent/<int:pk>/', views.ChapterViewSet.as_view({'get': 'get_parent'}))
]

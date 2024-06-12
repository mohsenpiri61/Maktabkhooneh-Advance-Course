from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post-router")
router.register("category", views.CategoryModelViewSet, basename="category-router")
urlpatterns = router.urls

# urlpatterns = [
#     # path for FBV
#     # path('post/', views.postList, name="post-list"),
#     # path('post/<int:id>/', views.postDetail, name='post-detail'),
#     # path for ApiView in CBV
#     # path('post/', views.PostList.as_view(), name="post-list"),
#     # path('post/<int:id>/', views.PostDetail.as_view(), name="post-detail"),
#     # path for ViewSet
#     # path('post/', views.PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
#     # path('post/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name="post-detail"),
#     # path for ModelViewSet
#     path('post/', views.PostModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
#     path('post/<int:pk>/', views.PostModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name="post-detail"),
# ]

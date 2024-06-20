from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

"""Example for Function Based View"""
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework import status
from django.shortcuts import get_object_or_404

# @api_view((["GET", "POST"]))
# @permission_classes([IsAuthenticated])
# def postList(request):
#     if request.method == "GET":
#         post_obj = Post.objects.filter(status=True)
#         serial_obj = PostSerializer(post_obj, many=True)
#         return Response(serial_obj.data)
#     elif request.method == "POST":
#         serial_receive = PostSerializer(data=request.data)
#         serial_receive.is_valid(raise_exception=True)
#         serial_receive.save()
#         return Response(serial_receive.data)


"""
we can use below codes instead of raise_exception
elif request.method == "POST":
    serial_receive = PostSerializer(data=request.data)
    if serial_receive.is_valid():
        serial_receive.save()
        return Response(serial_receive.data)
    else:    
        return Response(serial_receive.errors)
"""

# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def postDetail(request, id):
#     post_obj = get_object_or_404(Post, pk=id, status=True)
#     if request.method == "GET":
#         serializer = PostSerializer(post_obj)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = PostSerializer(post_obj, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         post_obj.delete()
#         return Response({"detail": "item removed successfully"}, status=status.HTTP_204_NO_CONTENT)


"""
we can use 'try/except' instead of 'get_object_or_404()'
post_obj = get_object_or_404(Post, pk=id)
serial_obj = PostSerializer(post_obj)
return Response(serial_obj.data)
 try:
        post_obj = Post.objects.get(pk=id, status=True)
        serial_obj = PostSerializer(post_obj)
        return Response(serial_obj.data)
    except Post.DoesNotExist:
        return Response({"detail": "post doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
"""

""" Example for ApiView in Class Based View """
from rest_framework.views import APIView

# class PostList(APIView):
#     """getting a list of posts and creating new posts"""
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#
#     def get(self, request):
#         """retriveing a list of posts"""
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         """creating a post with provided data"""
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#
# class PostDetail(APIView):
#     """ getting detail of the post and edit plus removing it """
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#
#     def get(self, request, id):
#         """ retrieving the post data """
#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         """ editing the post data """
#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = PostSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, id):
#         """ deleting the post object """
#         post = get_object_or_404(Post, pk=id, status=True)
#         post.delete()
#         return Response({"detail": "item removed successfully"}, status=status.HTTP_204_NO_CONTENT)


""" Example for GenericApiView in Class Based View """
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# class PostList(ListCreateAPIView):
#     """getting a list of posts and creating new posts"""
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
#
#
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     """ getting detail of the post and edit plus removing it """
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
#     lookup_field = 'id'  # because in urls.py we have defined 'post/<int:id>'


""" Example for ViewSet in CBV """
# from rest_framework import viewsets
#
#
# class PostViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
#
#     def list(self, request):
#         serializer = self.serializer_class(self.queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         post_obj = get_object_or_404(self.queryset, pk=pk)
#         serializer = self.serializer_class(post_obj)
#         return Response(serializer.data)
#
#     def create(self, request):
#         pass
#
#     def update(self, request, pk=None):
#         pass
#
#     def partial_update(self, request, pk=None):
#         pass
#
#     def destroy(self, request, pk=None):
#         post_obj = get_object_or_404(self.queryset, pk=pk)
#         post_obj.delete()
#         return Response({"detail": "item removed successfully"}, status=status.HTTP_204_NO_CONTENT)


""" Example for ModelViewSet in CBV """
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['category', 'author']
    filterset_fields = {'category': ["exact", "in"], 'author': ["exact", "in"], 'status': ["exact"]}
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination

    """ Extra action appears in url: http://127.0.0.1:8000/blog/api/v1/post/get_via_action/ """
    # @action(detail=False, methods=['get'])
    # def get_via_action(self, request):
    #     return Response({'detail': 'action is applied'})


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

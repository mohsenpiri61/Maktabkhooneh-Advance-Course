from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

"""Example for Function Based View"""
from rest_framework.decorators import api_view, permission_classes
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


class PostList(APIView):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        """retriveing a list of posts"""
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """creating a post with provided data"""
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PostDetail(APIView):
    """ getting detail of the post and edit plus removing it """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, id):
        """ retriveing the post data """
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, id):
        """ editing the post data """
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        """ deleting the post object """
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({"detail": "item removed successfully"}, status=status.HTTP_204_NO_CONTENT)

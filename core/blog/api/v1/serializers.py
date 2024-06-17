from rest_framework import serializers
from ...models import Post, Category
from core.accounts.models import Profile


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField(max_length=300)
#     status = serializers.BooleanField()
#     created_date = serializers.DateTimeField()

class PostSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(read_only=True)
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name="get_abs_url")
    category = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ["id", "author", "image", "title", "status", "category", "relative_url", "absolute_url", "content",
                  "snippet",
                  "created_date",
                  "published_date"]
        read_only_fields = ['author']

    def get_abs_url(self, obj):  # def's name must be same is defined in 'serializers.SerializerMethodField' under title 'method_name'
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        obtain_request = self.context.get("request")
        rep = super().to_representation(instance)
        if obtain_request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("content", None)
            
        rep["category"] = CategorySerializer(instance.category, context={"request": obtain_request}).data
        return rep

    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(user__id=self.context.get("request").user.id)
        return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

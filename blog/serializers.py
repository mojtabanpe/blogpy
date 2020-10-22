from datetime import datetime

from rest_framework import serializers

from blog.models import Article


class ArticleSerializer(serializers.Serializer):
    # _id = serializers.PKOnlyObject(read_only=True)
    title = serializers.CharField(required=False,max_length=128)
    cover = serializers.CharField(required=False,max_length=120)
    content = serializers.CharField(required=False,max_length=2055)
    create_at = serializers.DateTimeField(default=datetime.now)
    author_id = serializers.IntegerField(required=False,)
    category_id = serializers.IntegerField(required=False,)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        print('oomad to create')
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        print('oomad toupdate')
        instance.title = validated_data.get('title', instance.title)
        instance.cover = validated_data.get('cover', instance.cover)
        instance.content = validated_data.get('content', instance.content)
        instance.create_at = validated_data.get('create_at', instance.create_at)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()
        return instance

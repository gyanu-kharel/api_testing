from rest_framework import serializers
from post.models import Posts


class PostsSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    author = serializers.CharField(max_length=120)
    body = serializers.CharField(max_length=120)
    
    def create(self, validated_data):
        return Posts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance





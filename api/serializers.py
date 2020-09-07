from django.shortcuts import render
from rest_framework import serializers
from post.models import Posts
from django.contrib.auth.models import User

#for authentication
from django.contrib.auth import authenticate

#For exceptions
from rest_framework import exceptions


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

class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=120)
    password = serializers.CharField(max_length=25)

    def validate(self,data):
        username = data.get('username', '')
        password = data.get('password', '')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user']= user
                else:
                    raise exceptions.ValidationError({'detail':'User account is currently blocked.'})                
            else:
                raise exceptions.ValidationError({'detail':'Login credential is incorrect.'})            
        else:
            raise exceptions.ValidationError({'detail':'Fields cannot be blank.'})
        return data

from django.shortcuts import render
from post.models import Posts
from .serializers import PostsSerializers, LoginSerializers

# using APIView for class based function
from rest_framework.views import APIView

# For responses, errors and status
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

#For login, logout, token generation and token authentication
from django.contrib.auth import login as api_login, logout as api_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication



class post_list(APIView):
    def get(self, request):
        posts = Posts.objects.all()
        serializer = PostsSerializers(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class post_detail(APIView):
    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostsSerializers(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostsSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

                


class api_login(APIView):
    def post(self, request):
        serializer = LoginSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            api_login(user=user.username)
            token, created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key}, status=status.HTTP_201_CREATED)
   


class api_logout(APIView):
    authentication_classes = (TokenAuthentication)

    def post(self, request):
        api_logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


def login(request):
    return render(request, 'login.html')
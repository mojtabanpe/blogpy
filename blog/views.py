from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from . import serializers
from .serializers import ArticleSerializer
from .models import *


class IndexPage(TemplateView):

    def get(self, request, **kwargs):
        all_articles = Article.objects.all().order_by('-create_at')
        article_data = []
        for article in all_articles:
            article_data.append({
                'categoty': article.category.title,
                'title': article.title,
                'cover': article.cover.url,
                'create_at': article.create_at.date()
            })
        promote_data = []
        promote_articles = Article.objects.filter(promote=True)
        for article in promote_articles:
            promote_data.append({
                'categoty': article.category.title,
                'title': article.title,
                'cover': article.cover.url,
                'author': article.author.user.first_name,
                'avatar': article.author.avatar.url if article.author.avatar else None
            })

        context = {
            'article_data': article_data,
            'promote_data': promote_data
        }

        return render(request, 'index.html', context)


class ContactPage(TemplateView):
    template_name = "page-contact.html"


# class AllArticles(APIView):
#
#     def get(self, request, **kwargs):
#         try:
#             # data = []
#             all_articles = Article.objects.all()
#             serializer = ArticleSerializer(all_articles,many=True)
#             return JsonResponse(serializer.data,safe=False)
#             # for article in all_articles:
#             #     data.append({
#             #         'categoty': article.category.title,
#             #         'title': article.title,
#             #         'content': article.content,
#             #         'cover': article.cover.url,
#             #         'author': article.author.user.first_name,
#             #         'avatar': article.author.avatar.url if article.author.avatar else None
#             #     })
#             # return Response({'data': data}, status=status.HTTP_200_OK)
#
#         except:
#             return Response({'status': 'mese in ke ridim'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
# class GetArticle(APIView):
#
#     def get(self, request, format=None):
#         try:
#             article_title = request.GET['article_title']
#             article = Article.objects.filter(title=article_title)
#             print(article)
#             serialized_data = serializers.ArticleSerializer(article, many=True)
#             data = serialized_data.data
#
#             return Response({'data': data}, status=status.HTTP_200_OK)
#         except:
#             return Response({'status': 'mese inke ridim'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class SerachArticles(APIView):
    def get(self, request, format=None):
        try:
            query = request.GET['query']
            article = Article.objects.filter(Q(content__icontains=query))
            serialized_data = serializers.ArticleSerializer(article, many=True)
            data = serialized_data.data
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'mese inke ridim'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# class CreateArticles(APIView):
#     def post(self,request):
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
# class OneArticle(APIView):
#     #  Retrieve, update or delete an article
#     def get(self,request,pk):
#         try:
#             article = Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             return HttpResponse(status=404)
#
#         serializer = ArticleSerializer(article)
#         print(serializer.data)
#         return JsonResponse(serializer.data)
#
#
#     def put(self,request,pk):
#         try:
#             article = Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             return HttpResponse(status=404)
#         print(article.title)
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#
#     def delete(self,request,pk):
#         try:
#             article = Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             return HttpResponse(status=404)
#         article.delete()
#         return HttpResponse(status=204)

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
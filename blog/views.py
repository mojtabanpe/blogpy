from django.shortcuts import render
from django.views.generic import TemplateView

from .models import *


class IndexPage(TemplateView):

    def get(self, request, **kwargs):
        all_articles = Article.objects.all().order_by('-create_at')
        article_data = []
        for article in all_articles:
            article_data.append({
                'categoty' : article.category.title,
                'title' : article.title,
                'cover' : article.cover.url,
                'create_at' : article.create_at.date()
            })

        context = {
            'article_data': article_data
        }

        return render(request,'index.html', context)
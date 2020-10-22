from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    url(r'^contact$', views.ContactPage.as_view(), name='contact'),
    # url(r'^article/all$', views.AllArticles.as_view(), name='all_articles'),
    # url(r'^article/create$', views.CreateArticles.as_view(), name='create_articles'),
    # url(r'^article/do_on_one/<int:pk>$', views.OneArticle.as_view(), name='one_article'),
    path('article/article_list', views.ArticleList.as_view(), name='article_list'),
    path('article/article_one/<int:pk>', views.ArticleDetail.as_view(), name='one_article'),
    # url(r'^article/get_article/$', views.GetArticle.as_view(), name='get_article'),
    url(r'^article/serach_articles/$', views.SerachArticles.as_view(), name='serach_asrticles'),
    # path('', views.ContactPage.as_view(), name='contact')
]
# use for development state
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#     urlpatterns += static('contact/static', document_root = settings.STATIC_ROOT)

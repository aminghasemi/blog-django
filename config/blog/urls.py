from django.urls import path,include
from .views import api, ArticleList, ArticleDetail, CategoryList, AuthorList


app_name="blog"
urlpatterns = [
    path('blog', ArticleList.as_view(), name="home"),
    path('blog/page/<int:page>', ArticleList.as_view(), name="home"),
    path('api', api, name='api'),
    path('blog/article/<slug:slug>', ArticleDetail.as_view(), name="detail"),
    path('blog/category/<slug:slug>', CategoryList.as_view(), name="category"),
    path('blog/category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name="category"),
    path('blog/author/<slug:username>', AuthorList.as_view(), name="author"),
    path('blog/author/<slug:username>/page/<int:page>', AuthorList.as_view(), name="author"),
]
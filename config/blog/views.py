from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import Article, Category
from django.core.paginator import Paginator
# Create your views here.

class ArticleList(ListView):
    queryset=Article.objects.published()
    template_name= "blog/index.html"
    paginate_by=6

class ArticleDetail(DetailView):
    template_name="blog/detail.html"
    def get_object(self):
        slug=self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published() , slug=slug)


class CategoryList(ListView):
    def get_queryset(self):
        global category
        slug=self.kwargs.get('slug')
        category= get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()
    template_name= "blog/category.html"
    paginate_by=6
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['category']= category
        return context

class AuthorList(ListView):
    def get_queryset(self):
        global author
        username=self.kwargs.get('username')
        author= get_object_or_404(User, username=username)
        return author.articles.published()
    template_name= "blog/author_list.html"
    paginate_by=6
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['author']= author
        return context



###### These codes are the example of function based views ######
# def home(request, page=1):
#     
#     articles_list=Article.objects.published().order_by('-publish')
#     paginator= Paginator(articles_list,8)
#     articles = paginator.get_page(page)
#     context = {    
#         "articles": articles,
#         
#         
#     }
#     return render(request, "blog/index.html", context)
# 
# def detail(request,slug):
#     context = {
#         "articles": get_object_or_404(Article.objects.published() , slug=slug),
#         
#     }
#     return render(request, "blog/detail.html", context)
# 
# def category(request,slug,page=1):
#     category=get_object_or_404(Category, slug=slug, status=True)
#     articles_list=category.articles.published()
#     paginator= Paginator(articles_list,8)
#     articles = paginator.get_page(page)
#     context = {
#         "category": category,
#         "articles": articles,
#         
#     }
#     return render(request, "blog/category.html", context)




def api(request):
    data= {
        {
        "title": "posts1",
        "id": 20,
        "slug": first-article
        }
    }
    data= {
        {
        "title": "posts2",
        "id": 21,
        "slug": second-article
        }
    }
    data= {
        {
        "title": "posts3",
        "id": 22,
        "slug": third-article
        }
    }
    
    return JsonResponse(data)
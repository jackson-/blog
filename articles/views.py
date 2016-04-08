from django.shortcuts import render
from django.views.generic import View
from django.http import  JsonResponse
from articles.models.articles_model import Article

# Create your views here.
class IndexView(View):

    template_name = 'index.html'

    def get(self, request):
        articles = Article.objects.all()
        return render(request, self.template_name, {'articles':articles})



class ArticleView(View):

    template_name = 'article.html'

    def get(self, request, **kwargs):
        print kwargs
        article = Article.objects.get(slug=kwargs['slug'])
        return render(request, self.template_name, {'article':article})


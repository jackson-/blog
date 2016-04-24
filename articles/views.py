from django.shortcuts import render
from django.views.generic import View
from django.http import  JsonResponse
from articles.models.articles_model import Article
import operator

# Create your views here.
class IndexView(View):

    template_name = 'index.html'

    def get(self, request):
        articles = Article.objects.all().order_by('-published_date')
        # articles = sorted(articles, key=operator.attrgetter('published_date'))
        featured = Article.objects.latest("published_date")
        return render(request, self.template_name, {'articles':articles, 'featured':featured})



class ArticleView(View):

    template_name = 'article.html'

    def get(self, request, **kwargs):
        print kwargs
        article = Article.objects.get(slug=kwargs['slug'])
        return render(request, self.template_name, {'article':article})

class SubscribeView(View):

    template_name = 'subscribe.html'

    def get(self, request):
        return render(request, self.template_name)

class ResourcesView(View):

    template_name = 'resources.html'

    def get(self, request):
        return render(request, self.template_name)

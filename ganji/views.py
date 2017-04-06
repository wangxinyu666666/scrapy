from django.shortcuts import render
from ganji.models import ArtiInfo
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
# Create your views here.
def index(request):
    limit=4
    arti_info=ArtiInfo.objects[:1]
    paginator=Paginator(arti_info,limit)
    page=request.GET.get('page',1)
    loaded=paginator.page(page)
    context={
        'ArtiInfo':loaded
    }
    return render(request,'index.html',context)
class ArticleDetailView(DetailView):

     #model = Article
     template_name = 'index.html'
     context_object_name = 'article'
     pk_url_kwarg = 'article_id'

     def get_object(self, queryset=None):
         object = super(ArticleDetailView, self).get_object()
         return object

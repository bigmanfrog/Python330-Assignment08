from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

# Create your views here.
'''
def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    template = loader.get_template('blogging/list.html')
    context = {'posts': posts}
    body = template.render(context)
    return HttpResponse(body, content_type = 'text/html')
'''

class BloggingListView(ListView):
    #model= Post
    published = Post.objects.exclude(published_date__exact=None)
    queryset = published.order_by('-published_date')
    template_name = 'blogging/list.html'

'''
def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context) #using a shortcut here instead of the 4 lines above
'''
class BloggingDetailView(DetailView):
    model = Post
    #published = Post.objects.exclude(published_date__exact=None)
    try:
        queryset = Post.objects.exclude(published_date__exact=None)
    except Post.DoesNotExist:
        raise Http404
    template_name = 'blogging/detail.html'
    #pk_url_kwarg = 'post_id'

'''
def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" %i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")
'''

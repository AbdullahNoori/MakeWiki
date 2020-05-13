from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from wiki.models import Page
from .forms import PageForm


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })
    
class CreateWikiView(CreateView):
  model = Page

  def get(self, request):
    """ Returns a specific wiki page by slug. """
    form = PageForm()

    return render(request, 'new.html', {
      'form': form
    })

  def post(self, request):
    if request.method == "POST":
      form = PageForm(request.POST)
      
      if form.is_valid():
              
        wiki = form.save(commit=False)
        wiki.author = request.user
        wiki.save()

        return render(request, 'page.html', {'page': wiki})

    else:
      form = PageForm()

    context = {'form': form}

    return render(request, 'new.html', context)

  

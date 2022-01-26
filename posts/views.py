import os
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import DetailView, CreateView

from .models import Post, Idea

show_types = ["All", "Images", "Videos"]
sort_opts = ["Newest", "Oldest", "Alphabetic"]
sort_map = {'Newest': '-upload_date', 'Oldest':'upload_date', 'Alphabetic':'title'}

def home_basic(request):
    return home(request, "Newest", " ", "All")


class IdeaCreateView(CreateView):
    model = Idea
    template_name = 'posts/idea.html'
    fields = ['title', 'description', 'email']

    def get_success_url(self):
        return reverse('posts:home-basic')


    def get_absolute_url(self):
        return reverse(self.request, 'posts:home-basic')

def home(request, sort_option, search, show_type):
    matches = Post.objects.filter(title__contains=search.strip())
    matches = matches.order_by(sort_map[sort_option])
    if show_type == "Images":
        matches = [match for match in matches if match.video_name == ""]
    elif show_type == "Videos":
        matches = [match for match in matches if match.video_name != ""]

    available_sort_opts = sort_opts.copy()
    available_sort_opts.remove(sort_option)

    return render(request, 'posts/home.html',
            {'posts': matches,
            'sort_opts': available_sort_opts,
            'sort_opt': sort_option,
            'search':search,
            'show_types': show_types,
            'show_type': show_type}
            )

def search_home(request, sort_option, show_type):
    search = request.GET['searchtext']
    if not search: search = " "
    return home(request, sort_option, search, show_type)


def about(request):
    return render(request, 'posts/about.html')

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['object'].title
        return context


def blockdropper(request):
    return render(request, 'posts/blockdropper.html', {'posts':Post.objects.all().filter(block_dropper=True)})

def domino(request):
    return render(request, 'posts/domino.html')

def textgen(request):
    return render(request, 'posts/textgen.html')

def hire(request):
    return render(request, 'posts/hire.html')

def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    filepath = BASE_DIR + '/static/' + request.GET['filename']
    path = open(filepath, 'rb')

    # Not setting content type as the browser will handle the filetype
    # I see everybody using mimetypes.guess_type for this but mimetypes doesn't know webp
    # and others

    response = HttpResponse(path)

    response['Content-Disposition'] = "attachment; filename=%s" % \
        request.GET['filename'].split('/')[-1]
    return response

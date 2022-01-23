import os
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import DetailView, CreateView

from .models import Post, Idea

show_types = ["all", "image", "video"]
sort_opts = ["newest", "oldest", "alphabetic"]
sort_map = {'newest': 'upload_date', 'oldest':'-upload_date', 'alphabetic':'title'}

def home_basic(request):
    return home(request, "newest", " ", "all")


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
    if show_type == "image":
        matches = [match for match in matches if match.video_name == ""]
    elif show_type == "video":
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

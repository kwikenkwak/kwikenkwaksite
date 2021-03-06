import os
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import DetailView, CreateView

from .models import Post, Idea

show_types = ["All", "Images", "Videos"]
sort_opts = ["Newest", "Oldest", "Alphabetic"]
sort_map = {'Newest': '-upload_date', 'Oldest':'upload_date', 'Alphabetic':'title'}


class IdeaCreateView(CreateView):
    model = Idea
    template_name = 'posts/idea.html'
    fields = ['title', 'description', 'email']

    def get_success_url(self):
        return reverse('posts:home')

    def get_context_data(self, **kwargs):
        context = super(IdeaCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Submit your idea'
        return context


    def get_absolute_url(self):
        return reverse(self.request, 'posts:home')


def home(request):
    return render(request, 'posts/home.html',
            {'posts': Post.objects.all()})


def about(request):
    return render(request, 'posts/about.html', {'title':'About'})

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['object'].title
        return context


def blockdropper(request):
    return render(request, 'posts/blockdropper.html',
            {'posts':Post.objects.all().filter(block_dropper=True),
                'title':'Blockdropper add-on'
                }
            )

def domino(request):
    return render(request, 'posts/domino.html', {'title':'Domino add-on'})

def textgen(request):
    return render(request, 'posts/textgen.html', {'title':'TextGen add-on'})

def hire(request):
    return render(request, 'posts/hire.html', {'title':'Hire me'})

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

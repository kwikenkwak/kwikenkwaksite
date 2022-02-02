from . import views
from django.urls import path

app_name = 'posts'

urlpatterns = [
        path('', views.home, name='home'),

        path('detail/<pk>/', views.PostDetail.as_view(), name='detail'),
        path('download_file/', views.download_file, name='download'),
        path('about/', views.about, name='about'),
        path('blockdropper.html', views.blockdropper, name='blockdropper'),
        path('submitidea/', views.IdeaCreateView.as_view(), name='idea'),
        path('hireme/', views.hire, name='hire'),
        path('domino/', views.domino, name='domino'),
        path('textgen/', views.textgen, name='textgen'),
]

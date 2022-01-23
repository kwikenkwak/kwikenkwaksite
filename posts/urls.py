from . import views 
from django.urls import path

app_name = 'posts'

urlpatterns = [
        path('', views.home_basic, name='home-basic'),
        path('home/<str:sort_option>/<str:search>/<str:show_type>/',
            views.home, name='home'),

        path('home_search/<str:sort_option>/<str:show_type>/',
            views.search_home, name='home-search'),

        path('detail/<pk>/', views.PostDetail.as_view(), name='detail'),
        path('download_file/', views.download_file, name='download'),
        path('about/', views.about, name='about'),
        path('submitidea/', views.IdeaCreateView.as_view(), name='idea'),
]

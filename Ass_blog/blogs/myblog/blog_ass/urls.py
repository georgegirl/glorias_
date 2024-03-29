from django.urls import path
# from . import views
from .views import Homeview, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path ('', Homeview.as_view(), name ="home"),
    path('article/<int:pk>',  ArticleDetailView.as_view(), name ='article-detail'),
    path('add-post/', AddPostView.as_view(), name ='add-post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
    
]
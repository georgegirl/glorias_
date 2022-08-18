from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DetailView
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .models import post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


# Create your views here.

# def home(request):
#     return render(request, 'home.html',{})
class Homeview(ListView):#the list view is what put all our post on the main page
    model = post
    template_name='home.html'
    ordering = ['-Post_date']
    # ordering = ['-id']

class ArticleDetailView(DetailView):#the detail view is what gives detailed information on the post.it puts one blog on a page
    model = post
    template_name='article_detail.html'

class AddPostView(CreateView):
    model = post
    form_class = PostForm
    template_name='add-post.html'
    # fields= '__all__'#this puts all the fields from models.py into the "add post page". 

class UpdatePostView(UpdateView):
    model = post
    form_class = EditForm
    template_name = 'update-post.html'

class DeletePostView(DetailView):
    model = post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')
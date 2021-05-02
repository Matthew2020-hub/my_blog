from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
# def home(request):
#     return render(request, 'home.html', )
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = ('title', 'body')

class AddCommentView(CreateView):
    model = Post
    form_class = CommentForm
    template_name = 'add_comment.html'
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')
    #fields = '__all__'
    # fields = ('title', 'body')
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.views import LoginView
from django.contrib import messages



# Create your views here.
class BlogListView(ListView):
  model = Post
  template_name = 'home.html'
  
class BlogDetailView(CreateView):
  model = Comment
  template_name = 'post_detail.html'
  fields=['body']

  def form_valid(self, form):
    comment = form.save(commit=False)
    comment.author = User.objects.get(username=self.request.user)  # use your own profile here
    pk = self.kwargs['pk']
    comment.post = Post.objects.get(pk=pk)
    comment.save()
    return redirect(f"/post/{pk}")

  def get_context_data(self, *args, **kwargs):
    context=super(BlogDetailView, self).get_context_data(*args, **kwargs)
    pk = self.kwargs['pk']
    context['comment_list'] = Comment.objects.filter(post=pk)
    context['post'] = Post.objects.filter(pk=pk)[0]
    return context

class BlogCreateView(CreateView):
  model = Post
  template_name = 'post_new.html'
  fields = ['title', 'body']

  def form_valid(self, form):
    post = form.save(commit=False)
    post.author = User.objects.get(username=self.request.user)  # use your own profile here
    post.save()
    return redirect(Post.get_absolute_url(post))
  
class BlogEditView(UpdateView):
  model = Post
  template_name = 'post_edit.html'
  fields = ['title', 'body']

class BlogDeleteView(DeleteView):
  model = Post
  template_name = 'post_delete.html'
  success_url = reverse_lazy('home')
  
class BlogCommentView(CreateView):
  model = Comment
  template_name = 'post_detail.html'
  fields = ['body']

class UserRegisterView(CreateView):
  model = User
  form_class = UserCreationForm
  template_name = 'user_register.html'
  success_url =  reverse_lazy('user_login')


def login_request(request):
    form = AuthenticationForm(request=request, data=request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("home")
    return render(request=request, template_name='user_login.html', context={"form":form})

def logout_view(request):
    logout(request)
    return redirect("user_login")

class UserResetPassword(UpdateView):
  model = User
  form_class = PasswordResetForm(User)
  template_name = 'password_reset.html'
  success_url =  reverse_lazy('user_login')


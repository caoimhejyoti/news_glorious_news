from django.db import models
from django.forms.models import BaseModelForm
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import CustomUser
from .models import NewsStory, StoryComments
from .forms import CommentForm, StoryForm
# from .forms import ImageForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

# kwargs = keyword arguments. This is a named argument in your function. 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")[:2]
        context['all_stories'] = NewsStory.objects.all().order_by("-pub_date")[2:]
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
    # TODO:filter to only show dates in the past/today
    # only can view future if the author is yours. 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class AddStoryView(LoginRequiredMixin, generic.CreateView):
    login_url = "login"
    form_class = StoryForm
    context_object_name = 'storyform' #name used inside the template
    template_name='news/createStory.html'
    success_url = reverse_lazy('news:index') #on form success, take user back to index.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # def gallery(request):
    #     if request.method == 'POST':
    #         form = ImageForm(request.POST, request.FILES)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse('successfully uploaded')
    #     else:
    #         form = ImageForm()
    #     return render(request, "template/gallery.html", {"form": form})

# ------------ Update functionality -------------
class UpdateStoryView(LoginRequiredMixin, generic.UpdateView):
    model= NewsStory
    template_name = 'news/updateStory.html'
    fields = ['title', 'pub_date', 'image','content']
    success_url=reverse_lazy('news:index')

# ------------ FIXME: Delete functionality -------------
class DeleteStoryView(LoginRequiredMixin, generic.DeleteView):
    model= NewsStory
    template_name = 'news/deleteStory.html'
    success_url=reverse_lazy('news:index')

# ------------ FIXME: Search functionality -------------
def search_feature(request):
    if request.method =='POST':
        search_query = request.POST['search_query']
        stories = NewsStory.objects.filter(Q(title__icontains=search_query)|Q(author__email__icontains=search_query))
        # stories = NewsStory.objects.filter(Q(title__icontains=search_query) | Q(author__icontains=search_query))
        return render(request, 'news/search.html', {'query':search_query, 'stories':stories})
    else:
        return render(request, 'news/search.html', {})
    

# ------------ Comments functionality (taken from class demo) -------------
class AddCommentView(generic.CreateView):
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        return redirect("news:story", pk=self.kwargs.get("pk"))
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        pk= self.kwargs.get("pk")
        form.instance.story= get_object_or_404(NewsStory, pk=pk)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('news:story', kwargs={'pk':self.kwargs.get('pk')})

# ------------ Filtered Author view (taken from class demo) -------------
class AuthorView(generic.DetailView):
    model = CustomUser
    template_name = 'news/author.html'
    context_object_name = 'author'

    def get_object(self, *args, **kwargs):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().filter(author__id=self.object.id)
        return context
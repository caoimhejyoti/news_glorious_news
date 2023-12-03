from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import NewsStory
from .forms import StoryForm
from .forms import ImageForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

# kwargs = keyword arguments. This is a named argument in your function. 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")[:4]
        # context['latest_stories'] = NewsStory.objects.all()[:4]
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
    # TODO:filter to only show dates in the past/today
    # only can view future if the author is yours. 

class AddStoryView(LoginRequiredMixin, generic.CreateView):
    login_url = "login"
    form_class = StoryForm
    context_object_name = 'storyform' #name used inside the template
    template_name='news/createStory.html'
    success_url = reverse_lazy('news:index') #on form success, take user back to index.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def gallery(request):
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
        else:
            form = ImageForm()
        return render(request, "template/gallery.html", {"form": form})

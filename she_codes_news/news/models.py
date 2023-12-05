from django.db import models
from django.contrib.auth import get_user_model

def story_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.NewsStory.id, filename) 

class Image(models.Model):
    name = models.CharField(max_length=50, default=None)
    img = models.ImageField(upload_to='news_story_images/', default=None)
    def __str__(self):
        return self.name

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.URLField(null = True, blank = True)
    # image = models.ForeignKey(
    #     Image,
    #     on_delete=models.CASCADE,
    #     null = True,
    #     blank = True
    # )
    search_fields = ('title', 'author__username')
    def __str__(self):
        return self.title



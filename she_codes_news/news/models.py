from django.db import models
from django.contrib.auth import get_user_model

def story_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.NewsStory.id, filename) 

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    # image = models.URLField(null = True, blank = True)
    image = models.ImageField(null=True, blank=True,)



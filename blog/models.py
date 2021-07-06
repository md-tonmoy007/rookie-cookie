from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=100, default='uncategorized', blank=True, unique=True)

    def __str__(self):
        return self.title




STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    feauture_pic = models.ImageField(null=True, blank = True,)
    tag = models.ManyToManyField(Categories, default='uncategorized', blank=True)
    snippet = models.TextField(default='read this blog')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


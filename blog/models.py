from os import name
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify

# Create your models here.
class Profile(models.Model):
    image = models.ImageField(upload_to="media/",default="avatar.png")
    portfolio = models.URLField(blank=True)
    

    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name    
    

 
class User(AbstractUser):
    
    id = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    def __str__(self) -> str:
        return self.id
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=False)
    image = models.ImageField(upload_to="media/")
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    STATUS = (
        ("1","Draft"),
        ("2","Published"),
    )
    
    status = models.CharField(max_length=50,choices=STATUS)
    def slug(self):
        return slugify(self.title)
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
        
    
class Comment(models.Model):
    content = models.TextField(blank=False)
    time_stamp = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    
class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    
    
class PostView(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
   
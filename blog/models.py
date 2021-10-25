from os import name
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Profile(models.Model):
    image = models.ImageField(upload_to="media/",default="avatar.png")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='tutor_profile')
    bio = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return f"{self.user.username}'s Profile"

    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name    
    

    
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
   
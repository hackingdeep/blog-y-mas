from django.db import models
from users.models import User
import datetime
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100) 
    content = models.TextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField()
    
     
    def __str__(self) -> str:
        return self.title
    
   
    # @property
    # def  get_comment_count(self):
    #   return  Comment.objects.all().count()

    # @property
    # def  get_view_count(self):
    #     return PostView.objects.all().count()

    # @property
    # def  get_like_count(self):
    #     return Like.objects.all().count()
    
    
    

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self) -> str:
        return self.content
    
    class Meta:
        ordering = ['-timestamp']
    
   

class PostView(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
     
    def __str__(self) -> str:
        return self.user.username
    



class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='likes')

    def __str__(self) -> str:
        return self.user.username
    

class FollowersCount(models.Model):
    seguidor = models.ForeignKey(User,on_delete=models.CASCADE, related_name='siguiendo')
    siguiendo_a = models.ForeignKey(User,on_delete=models.CASCADE, related_name='seguidores')

    
    class Meta:
        unique_together = ('seguidor', 'siguiendo_a')

    def __str__(self)  :
        return  f'me sigue {self.seguidor}'
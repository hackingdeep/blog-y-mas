from django.contrib import admin
from .models import Post,PostView,User,Like,Comment,FollowersCount

admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(FollowersCount)

from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.title}, {self.content}'

    def get_absolute_detail_url(self):
        return reverse('post-detail', args=[str(self.id)])

    def get_absolute_update_url(self):
        return reverse('post-update', args=[str(self.id)])

    def get_absolute_url(self):
        return reverse('delete-post', args=[str(self.id)])

class Address(models.Model):
    pass

    class Meta:
        verbose_name_plural = 'Address'
# (env) C:\Users\user\Documents\dj-beginner\mysite>python manage.py shell
# Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from django.contrib.auth.models import User
# >>> from home.models import Post
# >>>
# >>>
# >>>
# >>> User.objects.all()
# <QuerySet [<User: user>, <User: test>]>
# >>> Post.objects.all()
# <QuerySet [<Post: first post, first post content>, <Post: 2nd post, 2nd post content>]>
# >>> user1 = User.objects.get(id=1)
# >>> user2 = User.objects.get(id=2)
# >>> user1
# <User: user>
# >>> user2
# <User: test>
# >>>
# >>>
# >>> post = Post.objects.get(id=1)
# >>> post
# <Post: first post, first post content>
# >>> post.author
# >>> post_set(author=user1)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'post_set' is not defined
# >>> post.author=user1
# >>> post.save()
# >>> post.author
# <User: user>
# >>> post2 = Post.objects.get(id=2)
# >>> post2.author=user2
# >>> post2.save()
# >>> post2.author
# <User: test>
# >>> user3 = User.objects.create(username='adam', email='adam12@gmail.com', password='adam12345')
# >>> user3.save()
# >>> User.objects.all()
# <QuerySet [<User: user>, <User: test>, <User: adam>]>
# >>> post3 = Post(title='3rd post title', content='3rd post content', author=user3)
# >>> post3.save()
# >>> for posts in Post.objects.all():
# ...     print(posts)
# ...
# first post, first post content
# 2nd post, 2nd post content
# 3rd post title, 3rd post content
# >>> for posts in Post.objects.all():
# ...     print(posts.author)
# ...
# user
# test
# adam
# >>> for posts in Post.objects.all():
# ...     print(posts.title)
# ...
# first post
# 2nd post
# 3rd p
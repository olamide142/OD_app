import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
import random
def randomId():
    characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for i in range(10):
        result += characters[random.randrange(len(characters))]
    return result

class Diary(models.Model):
    diary_id = models.CharField(max_length=10, null=True, blank=True)
    owner = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    about_me = models.CharField(max_length=140, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    # def save(self, *args, **kwargs):
    #     user = User(username=username)
    #     diary = Diary.objects.create(diary_id=randomId(),, about_me = "")
    #     diary.save()
    #
    #     super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.owner.username


class Post(models.Model):
    post_id = models.CharField(max_length=10, null=True, blank=True)
    diary = models.ForeignKey(Diary, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    body = models.CharField(max_length=1000, null=True)
    no_likes = models.BigIntegerField(null=True, default=0)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_id = models.CharField(max_length=10, null=True, blank=True)
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
    body = models.CharField(max_length=200, null=True)
    posted_by = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # pre_comment = models.ForeignKey('Comment', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.body

class Like(models.Model):
    CATEGORY = (
        ('Post', 'Post'),
        ('Comment', 'Comment')
    )
    liked_by = models.OneToOneField(Diary, null=True, on_delete=models.CASCADE)
    type = models.CharField(null=True, blank=True, choices=CATEGORY, max_length=10)
    item_id = models.CharField(null=True, blank=True, max_length=10)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return  str(self.item_id) +"-"+ str(self.type)





class Follower(models.Model):
    follower = models.ForeignKey(Diary, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(Diary, related_name='followers', on_delete=models.CASCADE)
    status = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return u'%s follows %s' % (self.follower, self.following)


class Tag(models.Model):
    name = models.CharField(max_length=200, null = True)
    def __str__(self):
        return self.name

# class Follow(models.Model)
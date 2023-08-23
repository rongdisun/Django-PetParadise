from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(verbose_name="帖子标题", max_length=255)
    content = RichTextField()
    add_time = models.DateTimeField(verbose_name="发布时间", auto_now=True)
    author = models.ForeignKey(verbose_name="发布者", to="user.User", on_delete=models.CASCADE)
    views = models.IntegerField(verbose_name="浏览量", default=0)
    thumb_up = models.PositiveIntegerField(verbose_name="点赞量", default=0)
    thumb_down = models.PositiveIntegerField(verbose_name="点踩数", default=0)

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=["views"])

    def increase_thumb_up(self):
        self.thumb_up += 1
        self.save(update_fields=["thumb_up"])

    def increase_thumb_down(self):
        self.thumb_down += 1
        self.save(update_fields=["thumb_down"])

    def get_absolute_url(self):
        return reverse("post:detail", args=[self.pk])

    class Meta:
        verbose_name = "帖子"
        verbose_name_plural = verbose_name

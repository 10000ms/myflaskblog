from django.db import models

from ..middleware.current_user import get_current_user
from utils.model_str import str_for_model
from ..manager import comment


class Comment(models.Model):

    title = models.CharField('标题', max_length=256)
    creator = models.ForeignKey('User', null=True, blank=True, on_delete=models.CASCADE, default=get_current_user)
    blog = models.ForeignKey('Blog', null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField('评论')

    objects = comment.CommentManager()

    def __str__(self):
        return str_for_model(self)

    class Meta:
        ordering = ['-id']

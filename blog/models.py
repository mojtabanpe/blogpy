from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension")


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to="files/user_avatar/",
                              blank=False, null=False, validators=[validate_file_extension])
    description = models.CharField(max_length=512, null=False, blank=False)

    def __str__(self):
        return self.user.first_name

class Article(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    cover = models.FileField(upload_to="files/article_cover/", blank=False, null=False, validators=[validate_file_extension])
    content = RichTextField()
    create_at = models.DateTimeField(default=datetime.now)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    cover = models.FileField(upload_to="files/category_cover/", blank=False, null=False, validators=[validate_file_extension])

    def __str__(self):
        return self.title
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150)  # title = Varchar
    content = models.TextField(blank=True)  # content = Text
    created_at = models.DateTimeField(auto_now_add=True)  # created_at = DateTime
    updated_at = models.DateTimeField(auto_now=True)  # updated_at = DateTime
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')  # photo = Image
    is_published = models.BooleanField(default=True)  # is_published = bool

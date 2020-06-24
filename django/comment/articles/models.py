from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    # blank = 유효성 검사시
    # null = DB상의 컬럼의 Null
    images = models.ImageField(blank=True, upload_to="%y/%m/%d/")
    image_thumbnail = ImageSpecField(
        source = 'images',
        processors = [Thumbnail(300, 300)],
        format = 'JPEG',
        options = {'quality' : 90}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}번째 글 - {self.title} : {self.content}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Article:{self.article}, {self.pk}-{self.content}'
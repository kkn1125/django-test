from django.db import models
from django.utils import timezone

# Create your models here.
class Board(models.Model):
    num = models.IntegerField(primary_key=True)
    # primary_key를 지정해줘야 ~~.id field error가 나지 않는다.
    title = models.CharField(max_length=50, null=True)
    content = models.CharField(max_length=500, null=True)
    author = models.CharField(max_length=50, null=True)
    regdate = models.DateTimeField('created', default=timezone.now, editable=False, null=False, blank=False)
    updates = models.DateTimeField('date published', default=timezone.now, editable=False, null=False, blank=False)

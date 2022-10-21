from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Book(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=264, null=True, blank=True)

    def __str__(self):
        return self.name


class Chapter(MPTTModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books')
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')
    name = models.CharField(max_length=50, null=True, blank=True)
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['publish']

    def __str__(self):
        return self.name



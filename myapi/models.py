from django.db import models

# Create your models here.


class Music(models.Model):

    class Meta:

        db_table = 'music'

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()

    def __str__(self):
        return self.title

class Categories(models.Model):

    class Meta:

        db_table = 'categories'

    name = models.CharField(max_length=200)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
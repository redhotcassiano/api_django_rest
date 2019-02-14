from django.db import models

""" winpty py manage.py createsuperuser """


class Categories(models.Model):

    class Meta:

        db_table = 'categories'

    name = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Music(models.Model):

    class Meta:

        db_table = 'music'

    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User', on_delete=True)
    category = models.ForeignKey('myapi.Categories', on_delete=True)

    def __str__(self):
        return self.title

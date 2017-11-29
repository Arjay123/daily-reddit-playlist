from django.db import models

# Create your models here.
class Person(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    fav_game = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='persons', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)



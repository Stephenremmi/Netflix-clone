from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Director(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def save_director(self):
        self.save()

class characters(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length =60)
    director = models.ForeignKey(User,on_delete=models.CASCADE,)
    story_line = models.TextField()
    characters = models.ManyToManyField(characters)
    rel_date = models.DateTimeField(auto_now_add=True) 


    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(rel_date__date = today)
        return netflix   
    @classmethod
    def days_news(cls,date):
        netflix = cls.objects.filter(rel_date__date=date)
        return netflix

    @classmethod
    def search_by_title(cls,search_term):
        netflix = cls.objects.filter(title__icontains=search_term)    
        return netflix



class NetflixLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    
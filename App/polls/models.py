import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    
    questions_text = models.CharField( max_length=200)
    pub_date = models.DateTimeField("pub_date")
    
    def __str__(self):
        return self.questions_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
    
class Choice(models.Model):
    
    questions_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField("choices_text", max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
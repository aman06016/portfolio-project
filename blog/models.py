from django.db import models

# Create your models here.
class Blog(models.Model):

    title=models.CharField(max_length=100)
    date=models.DateField(auto_now=False,auto_now_add=False)
    text=models.TextField()
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:100]
'''
    def pretty_time(self):
        return self.date.strftime('%b %e %Y')
'''

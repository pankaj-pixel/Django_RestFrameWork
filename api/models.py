from django.db import models


class Books(models.Model):
    Name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    Price = models.IntegerField()
    Published = models.DateField()
    
    class Meta:
        verbose_name_plural ='Books'


    def __str__(self):
        return self.Name
    


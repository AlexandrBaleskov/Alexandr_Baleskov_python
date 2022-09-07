
from django.db import models


class News(models.Model):
    title_news = models.CharField("Название статьи",max_length=200)
    data = models.DateField("Дата публикации")
    text = models.TextField("Текст статьи")
    image_front = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)
    image_add1 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100,blank=True)
    image_add2 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100,blank=True)
    image_add3 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100,blank=True)
    image_add4 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100,blank=True)
    image_add5 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100,blank=True)
    author = models.CharField("Автор статьи",max_length=100) 
     
    
    def __str__(self):
        return self.title_news
    
    class Meta():
        verbose_name = "Актуальные новости"
        
        

class Info(models.Model):
    term = models.CharField("Термин",max_length=200)
    description = models.TextField("Описание значения")
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100,blank=True)
    
    def __str__(self):
        return self.term
    
    class Meta():
        verbose_name = "Термины в Доп. Инфо"
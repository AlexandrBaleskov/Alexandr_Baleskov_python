from django.db import models


class Personnel(models.Model):
    surname = models.CharField("Фамилия",max_length=20)
    name = models.CharField("Имя",max_length=20)
    date_of_birth = models.CharField ("День Рождения",max_length=20)
    year_of_joining = models.CharField ("Количество лет в клубе",max_length=20)
    rank = models.CharField("Клубное Звание",max_length=20)
    status = models.CharField("Статус",max_length=20)
    vk = models.CharField("Страница в соц сетях",max_length=20, blank=True)
    phone_number = models.CharField("Контактный номер телефона",max_length=20, blank=True)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)
    
    def __str__(self):
        return self.surname
    
    class Meta():
        verbose_name = "Состав клуба"
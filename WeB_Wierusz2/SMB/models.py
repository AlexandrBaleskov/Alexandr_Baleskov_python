from django.db import models

class SMB_new_people(models.Model):
    surname = models.CharField("Фамилия",max_length=25)
    name = models.CharField("Имя",max_length=20)
    age = models.CharField("Возраст",max_length=3)
    gender = models.CharField("Пол",max_length=8)
    add_info = models.TextField("Противопоказания по физ.нагрузкам (если имеются)", blank=True)
    phone_number = models.CharField("Номер телефона",max_length=25)
    
    
    def __str__(self):
        return self.surname
    
    class Meta():
        verbose_name = "Заявки в секцию СМБ"
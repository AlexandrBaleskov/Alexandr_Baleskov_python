from .models import SMB_new_people

from django import forms

CHOICES = [('мужской', 'Мужской'),('женский', 'Женский')]

Gender = [('мужской', 'Мужской'),('женский', 'Женский'),]
class SMB_new_peopleForm(forms.Form):
    surname = forms.CharField(max_length=25)
    name = forms.CharField(max_length=20)
    age = forms.CharField(max_length=3)
    gender = forms.MultipleChoiceField(required=False, widget=forms.Select, choices=Gender)
    add_info = forms.CharField(max_length=10000, widget=forms.Textarea,required=False)
    phone_number = forms.CharField(max_length=20)
        
    surname.widget.attrs.update({
                'class': "form-control",
                'type':"text",
                "placeholder":"Фамилия",
                'autofocus size':"25",
                "required pattern":"^[А-Яа-яЁё]+$"
                })
    
    name.widget.attrs.update({
                'class': "form-control",
                'type':"text",
                "placeholder":"Имя",
                'autofocus size':"20",
                "required pattern":"^[А-Яа-яЁё]+$"
                })
    age.widget.attrs.update({
                'class': "form-control",
                'type':"text",
                "placeholder":"Возраст",
                
                
                })
    
    add_info.widget.attrs.update({
                'class': "form-control",
                "placeholder":" Противопоказания по физ.нагрузкам (если имеются)"
                
                })
    
    
    gender.widget.attrs.update({
                'class': "form-control",
                "placeholder":"Пол",
                
                })
    
    phone_number.widget.attrs.update({
                'class': "form-control",
                'type':"text",
                "placeholder":"Контактный номер телефона",
                'autofocus size':"13",
                "required pattern" : "+[0-9]{3}-[0-9]{2}-[0-9]{7}",
            
                })
    
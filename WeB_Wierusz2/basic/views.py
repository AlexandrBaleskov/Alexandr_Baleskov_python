
from django.shortcuts import render,redirect
from Personnel.models import Personnel
from SMB.models import SMB_new_people
from SMB.forms import SMB_new_peopleForm
from .models import News,Info


def news(request):
    news = News.objects.order_by('-data')[:3]
    return render (request,"basic/home.html", {'news':  news})

def aboute(request):
    return render (request,"basic/aboute.html")



# def personnel(request):
#     personnel = Personnel.objects.all()
#     return render (request,"basic/personnel.html", {'personnel_klub': personnel})

def personnel(request):
    personnel = Personnel.objects.all()
    desytnik = Personnel.objects.filter(rank = "Десятник")
    pehota = Personnel.objects.filter(rank = "Пехотинец")
    opolchenie = Personnel.objects.filter(rank = "Ополченец")
    kmet = Personnel.objects.filter(rank = "Кмет")
    data = {
            "desytnik": desytnik,
            "pehota": pehota,
            "opolchenie": opolchenie,
            "kmet":kmet,
            'personnel_klub': personnel
            }
    return render (request,"basic/personnel.html", data)

def info(request):
    info = Info.objects.all()
    return render (request,"basic/info.html", {'info': info})
    
    
    
def SMB(request):
    if request.method == 'GET':
        forms = SMB_new_peopleForm()
        data = {
            "form": forms,
            }
        return render (request,"basic/SMB.html",data)
    
    
    elif request.method == 'POST': 
        form = SMB_new_peopleForm(request.POST)
        
        new_people = SMB_new_people(
            
            surname =form.data['surname'],
            name = form.data['name'],
            age = form.data['age'],
            gender = form.data['gender'],
            add_info = form.data['add_info'],
            phone_number = form.data['phone_number'],
            )
        
        
        new_people.save()
        return redirect("SMB_Ok")
    
def SMB_Ok(request):
    return render (request,"basic/SMB_OK_form.html")


def contacts(request):
    return render (request,"basic/contacts.html")
            
            
            
    
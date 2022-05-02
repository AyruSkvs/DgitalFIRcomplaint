from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from FIR.models import memberdata


def home(request):
    return render(request,'page1.html')


def login(request):
    username=request.POST['txtname']
    password=request.POST['txtpass']
    if username=='surya' and password=='surya':
        return render(request,'page2.html')
    return render(request,'page1.html')


def insertpage(request):
    return render(request,'details_complaint.html')


def insert_data(request):
    sfullname=request.POST['txtname']
    sgender=request.POST['txtgn']
    sage=request.POST['txtage']
    sphone=request.POST['txtphone']
    scountry=request.POST['txtcon']
    sstate=request.POST['txtst']
    sdistrict=request.POST['txtdt']
    smandal=request.POST['txtmd']
    svillage=request.POST['txtvi']
    shouse_no=request.POST['txthn']
    spin_code=request.POST['txtpin']
    sNear_police_station=request.POST['txtpolice']
    stext_area=request.POST['txtarea']

    s1=memberdata()
    s1.fullname = sfullname
    s1.gender = sgender
    s1.age = sage
    s1.phone=sphone
    s1.country=scountry
    s1.state=sstate
    s1.district=sdistrict
    s1.mandal=smandal
    s1.village=svillage
    s1.pin_code=spin_code
    s1.house_no=shouse_no
    s1.Near_police_station=sNear_police_station
    s1.text_area=stext_area
    s1.save()
    return HttpResponse('inserted successfully')


def display_data(request):
    all_data=memberdata.objects.all()  #select* from memberdata
    return render(request,'display.html',{'data':all_data})


def hq_contacts(request):
    return render(request,'HQcontacts.html')


def update_data(request):
    return
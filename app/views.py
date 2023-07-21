from datetime import datetime
from django.shortcuts import redirect, render
from app.models import *
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login

# Create your views here.

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
    context = {}
    return render(request, 'login.html', context)

def home(request):
    customer = request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        classroom = request.POST.get('classroom')
        phonenumber = request.POST.get('phonenumber')
        if len(phonenumber) < 11:
            staff = Staffs(name= name, classroom= classroom, phonenumber= phonenumber, customer= customer)
            staff.save()
            messages.success(request, 'Đã thêm thành công!')
        else:
            messages.success(request, 'Không thành công do nhập sai thông tin!')
        return redirect('home')
    staffs = Staffs.objects.filter(customer= customer)
    numofstaff = len(staffs)
    events = Event.objects.filter(customer= customer)
    context = {'staffs': staffs, 'numofstaff': numofstaff, 'events': events}
    return render(request, 'home.html', context)

def acttendence(request):
    customer = request.user
    if request.method == 'POST':
        id_staffs = request.POST.getlist('checkbox')
        for id in id_staffs:
            acttendence = Acttendence.objects.get(staff__id= id)
            acttendence.status = True
            acttendence.save()
        return redirect('home')
    id = request.GET.get('id')
    event = Event.objects.get(id= id, customer= customer)
    act = Acttendence.objects.filter(event__id= id, event__customer= customer)
    events = Event.objects.filter(customer= customer)
    context = {'event': event ,'act': act, 'events': events}
    return render(request, 'acttendencepage.html', context)

def event(request):
    customer = request.user
    events = Event.objects.filter(customer= customer)
    context ={'events': events}
    return render(request, 'event.html', context)

def registerevent(request):
    customer = request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        date_str = request.POST.get('date')
        date = datetime.strptime(date_str, '%m/%d/%Y')
        date = date.strftime('%Y-%m-%d')
        event = Event(name= name, date= date, description= description, customer= customer)
        event.save()
        list_staff_reg = request.POST.getlist('checkbox')
        for staff_id in list_staff_reg:
            staff = Staffs.objects.filter(id= staff_id)[0]
            act = Acttendence(event= event, staff= staff)
            act.save()
        return redirect('event')
    staffs = Staffs.objects.filter(customer= customer)
    events = Event.objects.filter(customer= customer)
    context = {'staffs': staffs, 'events': events}
    return render(request, 'registerevent.html', context)

def logoutpage(request):
    logout(request)
    context={}
    return redirect('login')

def modifyevent(request):
    customer= request.user
    id_event = request.GET.get('id')
    event, create = Event.objects.get_or_create(id= id_event)
    id_staff_rig = Acttendence.objects.filter(event__id= id_event).values_list('staff__id', flat=True)
    staffs = Staffs.objects.filter(customer= customer)

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        date_str = request.POST.get('date')
        date = datetime.strptime(date_str, '%m/%d/%Y')
        date = date.strftime('%Y-%m-%d')

        event.name = name
        event.description = description
        event.date = date
        event.save()

        list_staff_reg = request.POST.getlist('checkbox')
        for staff_id in list_staff_reg:
            if str(staff_id) not in str(id_staff_rig):
                staff, create = Staffs.objects.get_or_create(id= staff_id)
                act,create = Acttendence.objects.get_or_create(event= event, staff= staff)
                act.save()
        
        for id in id_staff_rig:
            if str(id) not in str(list_staff_reg):
                act = Acttendence.objects.get(staff__id= id)
                act.delete()

        return redirect('event')

    events = Event.objects.filter(customer= customer)
    context= {'event': event, 'SRegistered': id_staff_rig, 'staffs': staffs, 'events': events}
    return render(request, 'modifyevent.html', context)
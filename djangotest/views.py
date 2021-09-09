from django.shortcuts import render, HttpResponseRedirect
from .forms import UserEntry
from .models import User
# Create your views here.


def index(request):
    return render(request, 'djangotest/index.html')


def addproject(request):
    if request.method == 'POST':
        obj = UserEntry(request.POST)
        if obj.is_valid():
            name = obj.cleaned_data['name']
            start_date = obj.cleaned_data['start_date']
            end_date = obj.cleaned_data['end_date']
            value = obj.cleaned_data['value']
            data = User(name=name, start_date=start_date, end_date=end_date, value=value)
            data.save()
            obj = UserEntry()
    else:
        obj = UserEntry()
    return render(request, 'djangotest/addproject.html', {'form': obj})


def show(request):
    alldata = User.objects.all()
    return render(request, 'djangotest/show.html', {'alldata': alldata})


def deletedata(request, id):
    if request.method == 'POST':
        deldata = User.objects.get(pk=id)
        deldata.delete()
    return HttpResponseRedirect('/')


def editdata(request, id):
    if request.method == 'POST':
        edit = User.objects.get(pk=id)
        obj = UserEntry(request.POST, instance=edit)
        if obj.is_valid():
            obj.save()
    else:
        edit = User.objects.get(pk=id)
        obj = UserEntry(instance=edit)
    return render(render, 'djangotest/editproject.html', {'form': obj})

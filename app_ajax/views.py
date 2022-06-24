from django.http import JsonResponse
from django.shortcuts import render
from . models import User
# Create your views here.
def index(request):
    alldata = User.objects.all()
    return render(request, 'index.html',{'alldata':alldata})

def add_data(request):
    User.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        mobile = request.POST['mobile']
    )
    alldata = list(User.objects.values())

    return JsonResponse({'alldata':alldata})

def delete_data(request):
    ddata = User.objects.get(id=request.GET['rid'])
    ddata.delete()
    alldata = list(User.objects.values())

    return JsonResponse({'alldata':alldata})
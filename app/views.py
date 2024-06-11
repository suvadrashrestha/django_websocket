from django.shortcuts import render
from .models import Group
# Create your views here.
def index(request,group_name):

    group= Group.objects.filter(name=group_name).first()
    if group:
        pass
    else:
        instance= Group(name=group_name)
        instance.save()
    return render(request,"app/index.html",{'group_name':group_name})
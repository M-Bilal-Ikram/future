from django.http import HttpResponse
from django.shortcuts import render 
def any(request):
    return HttpResponse("<h1>Assalam-o-Alaikum to my Web</h1>")
def sign(request):
    
    return render(request,"index.html")
def hm(request):
    home={
    'Name':['Zain','Bilal'],
    'Class':['8TH','10TH'],
    'Fav-Subject':['Science','Computer']
}
    return render(request,'zain.html',home)
     
    
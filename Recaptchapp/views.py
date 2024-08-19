from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm

# Create your views here.
def index(request):
    form = MyForm()
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            return HttpResponse("You are Human")
        else:
            return HttpResponse("You are not Human")
    return render(request,"Recaptchapp/index.html",{"form":form})
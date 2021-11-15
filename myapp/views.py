from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image
# Create your views here.
def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect(request.path)
    else:
        form = ImageForm()
        img = Image.objects.all()
        return render (request, 'index.html',{'form':form,'img':img})
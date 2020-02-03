from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return render('index.html')

def gallery(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    location = Location.objects.all()
    return render(request, 'gallery.html', locals())
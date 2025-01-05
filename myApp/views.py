from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookForm

def home(request):
    context = {}
    return render (request,"myApp/home.html",context)


def book_data(request):
    form = BookForm()
    return render(request, 'myApp/book.html', {'form': form})

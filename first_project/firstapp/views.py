from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Topic , AccessRecord

# Create your views here.
def index(request):
    Topic = AccessRecord.objects.order_by('date')
    context = {"name":Topic}
    return render(request,'firstapp\index.html' ,context)


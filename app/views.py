from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,"index.html")

def input(request):
    return render(request,"input.html")

def add(request):
    data = request.POST['html_data']
    print(data)
    return HttpResponse("add.html",{"html_data":data})
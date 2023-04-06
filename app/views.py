from django.shortcuts import render

# Create your views here.
def parent(request):
    return render(request,'parent.html')

def child(request):
    return render(request,'child.html')

def p1(request):
    return render(request,'p1.html')

def c1(request):
    return render(request,'c1.html')
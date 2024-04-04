from django.shortcuts import render

# Create your views here.
def if_else(request):
    d={'a':100,'b':200}
    return render(request,'if_else.html',d)

def if_elif_else(request):
    d={'a':100,'b':200,'c':300}
    return render(request,'if_elif_else.html',d)

def nestedif(request):
    d={'a':100,'b':200,'c':500,'d':400}
    return render(request,'nestedif.html',d)
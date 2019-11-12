from django.http import HttpResponseRedirect
from django.views.decorators.cache import cache_control
from django.shortcuts import render,redirect
from django.shortcuts import redirect
from .models import EmployeeModel

def showIndex(request):
    try:
        if eval(request.COOKIES["status"]):
            email = request.COOKIES["value"]
            res = EmployeeModel.objects.get(email=email)
            return render(request,"welcome.html",{"data":res})
        else:
            return render(request,"index.html")
    except KeyError:
        return render(request, "index.html")


def showRegister(request):
    return render(request,"register.html")


def saveEmployee(request):
    e = request.POST["email"]
    f = request.FILES["image"]
    p = request.POST["password"]
    EmployeeModel(email=e,password=p,image=f).save()
    return redirect('main')


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def loginCheck(request):
    em = request.POST["email"]
    pa = request.POST["password"]
    try:
        res = EmployeeModel.objects.get(email=em,password=pa)
        #HttpResponsePermanentRedirect(request,"welcome.html")
        response = render(request,"welcome.html",{"data":res})
        response.set_cookie("status",True)
        response.set_cookie("value",em)
        return response
    except EmployeeModel.DoesNotExist:
        return render(request,"index.html",{"err_message":"Invalid User"})




@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def logout(request):
    #response = render(request,"index.html")
    response = HttpResponseRedirect("/index/")
    response.set_cookie("status", False)
    response.set_cookie("value", None)
    return response
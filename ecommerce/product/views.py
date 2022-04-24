from django.shortcuts import render
from .models import category,product
def home(request):
    allcategory = category.objects.all()
    allproducts = product.objects.all()
    return render(request,'pages/home.html',{"allproducts":allproducts,"allcategory":allcategory})

def Category(request,categoryid):
    allcategory = category.objects.all()
    mycategory = category.objects.get(id=categoryid)
    allproducts = product.objects.all().filter(category_id = categoryid )
    return render(request,'pages/category.html',{"allproducts":allproducts,"allcategory":allcategory,"mycategory":mycategory})


def Product(request,productid):
    allcategory = category.objects.all()
    myproduct = product.objects.get(id=productid)
    return render(request,'pages/product.html',{"allcategory":allcategory,"myproduct":myproduct})

def newproducts(request):
    allcategory = category.objects.all()
    allproducts = product.objects.all().order_by("-id")
    return render(request,'pages/newproducts.html',{"allproducts":allproducts,"allcategory":allcategory})

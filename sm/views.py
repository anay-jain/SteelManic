from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from mainview.models import Item, Query
from django.core.paginator import Paginator

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request ,'about.html')
def contact(request):
    thank = False
    if request.method == "POST":
       itemjson=request.POST.get('itemjson','')
       name=request.POST.get('name','')
       email=request.POST.get('email','')
       sub=request.POST.get('sub','')
       phone=request.POST.get('phone','')
       desc=request.POST.get('desc','')
       query = Query(itemjson=itemjson ,name=name , email=email,sub=sub, phone=phone , desc=desc)
       query.save()
       return HttpResponseRedirect('contact_success/')
    return render(request, 'contact.html',{'thank': thank })

def shop(request):
    all_items = Item.objects.all()
    paginator = Paginator(all_items , 2)
    page = request.GET.get('page')
    all_items = paginator.get_page(page)
    context = {
        'all_items' : all_items,
    }
    return render(request, 'shop.html',context) 

def products(request ,item_id):
    item=get_object_or_404(Item , item_id=item_id)

    return render(request , 'shop-details.html',{'item' :item})


def cart(request):
    return render(request,'cart.html')   

def kitchenware(request):
    return render(request,'shop/kitchenware.html')
def tableware(request):
    return render(request,'shop/tableware.html')
def barware(request):
    all_items = Item.objects.filter(item_category='barware')
    paginator = Paginator(all_items , 2)
    page = request.GET.get('page')
    all_items = paginator.get_page(page)
    context = {
        'all_items' : all_items,
    }
    return render(request, 'shop/barware.html',context)

def contact_success(request):
    return render(request,'contact/contact_success.html')        
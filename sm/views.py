from django.shortcuts import render 
from mainview.models import Item
from django.core.paginator import Paginator
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request ,'about.html')

def shop(request):
    all_items = Item.objects.all()
   
    paginator = Paginator(all_items , 2)
    page = request.GET.get('page')
    all_items = paginator.get_page(page)
    context = {
        'all_items' : all_items
    }
    return render(request, 'shop.html',context)    
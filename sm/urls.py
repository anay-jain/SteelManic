"""sm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.index , name='index'),
    path('mainview/' , include('mainview.urls')),
    path('about/',views.about , name='about'),
    path('shop/' , views.shop , name='shop'),
    path('contact/',views.contact ,name="contact" ),
    path('cart/',views.cart , name='cart'),
    path('shop/kitchenware/',views.kitchenware,name="kitchenware"),
    path('shop/tableware/' ,views.tableware,name="tableware"),
    path('shop/barware/' , views.barware,name="barware"),
    path('products/<str:item_id>/',views.products,name="products"),
    path('contact/contact_success/' , views.contact_success , name='contact_success'),
    path('shop/cutlery/',views.cutlery , name="cutlery"),
    path('shop/homedecor' , views.homedecor , name="homedecor"),
    path('blogs/' , views.blogs, name="blogs"),
    path('shop/dogpots/' ,views.dogpots,name="dogpots"),

] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

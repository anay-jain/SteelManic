from django.db import models

class Item(models.Model):
    item_id=models.CharField(max_length=30 , primary_key=True)
    item_title=models.CharField(max_length=30)
    item_description=models.TextField()
    item_image=models.ImageField(upload_to='media',default=True)
    item_price=models.DecimalField(max_digits=10 , decimal_places=2,default=1.0)
    item_category=models.CharField(max_length=30,default="cutlery")

    def __str__(self):
        return self.item_title

class Query(models.Model):
    msg_id = models.AutoField(primary_key=True)
    itemjson =models.CharField(max_length=5200,blank=True)
    name= models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    sub=models.CharField(max_length=200)
    phone=models.CharField(max_length=12)
    desc=models.TextField()

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email=models.EmailField(unique=True)


    def __str__(self):
        return self.email
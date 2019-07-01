from django.db import models

class Item(models.Model):
    item_title=models.CharField(max_length=30)
    item_description=models.TextField()
    item_image=models.ImageField(upload_to='media',blank=True)
    item_price=models.DecimalField(max_digits=10 , decimal_places=2,default=1.0)
    item_category=models.CharField(max_length=30,default="cutlery")

    def __str__(self):
        return self.item_title

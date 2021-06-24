from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    catagory = models.CharField(max_length=50)
    subcatagory = models.CharField(max_length=50)
    price = models.IntegerField()
    des = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images")                                                                                                                                                                                                                                                                                                                                                                                                             

    def __str__(self):
        return self.product_name

class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111, default="")        


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    desc = models.CharField(max_length=5000)
    

    def __str__(self):
        return self.name


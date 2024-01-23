from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length = 225)
    description = models.TextField()
    slug = models.SlugField()
    price = models.IntegerField()
    is_new = models.BooleanField()
    is_discounted = models.BooleanField(default = False)
    thumb = models.ImageField(default='default_product.png', null=True)
    category = models.ForeignKey('Category',default=None, on_delete=models.CASCADE)
    brand = models.ForeignKey("Brand",default=None, on_delete=models.CASCADE )

    def __str__(self) :
        return self.title
    
    def sale_product_price(self):
        if self.is_discounted:
            return self.price * 0.8

    class Meta:
        db_table = 'shop_products'




class Category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
    

    class Meta:
        db_table = 'shop_categories'



class Brand(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'shop_barnds'


class Slide(models.Model):
    image = models.ImageField()


class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title
    
    def total_price(self):
        return self.product.price * self.quantity
    
class Order(models.Model):
    address = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 255)
    total_price = models.IntegerField()
    customer = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return 'Order # %s' % (str(self.id))
    

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name = 'order_products')
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    amount = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return '%s x%s-%s' % (self.product, self.amount, self.order.customer.username)
    

RATE_CHOICES =  [
    (1, '1 - Trash'),
    (2, '2 - Bad'),
    (3, '3 - Ok'),
    (4, '4 - Good'),
    (5, '5 - Perfect')
]

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    text = models.TextField(max_length = 3000, blank = True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null = True)

    def __str__(self):
        return self.username
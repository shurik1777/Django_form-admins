from django.db import models as m


class Client(m.Model):
    name = m.CharField(max_length=32)
    email = m.EmailField(unique=True)
    phone = m.CharField(max_length=15)
    address = m.CharField(max_length=128)
    date_of_register = m.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(m.Model):
    title = m.CharField(max_length=128)
    content = m.TextField()
    price = m.DecimalField(max_digits=64, decimal_places=2, default=0)
    amount = m.PositiveIntegerField(default=0)
    date = m.DateField(auto_now_add=True)
    photo = m.ImageField(upload_to='product_photos/', blank=True, null=True)
    # upload_to='products/photos/%Y/%m/%d' - такой строкой можно подгружать в разные директории от разных дат

    def __str__(self):
        return f"Title: {self.title}, price: {self.price}, amount: {self.amount}"


class Order(m.Model):
    client = m.ForeignKey(Client, on_delete=m.CASCADE, related_name='orders')
    products = m.ManyToManyField(Product, related_name='orders')
    price = m.DecimalField(max_digits=5, decimal_places=2)
    date_of_order = m.DateField()

    def __str__(self):
        return f"Client: {self.client}, price: {self.client.name}"

    def calculate_total_price(self):
        total_price = sum([product.price for product in self.products.all()])
        self.price = total_price
        self.save()

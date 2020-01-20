from django.db import models
from backend.apps.utils.models import ModelBase


class InventoryItem(ModelBase):
    title = models.CharField(max_length=60)
    price = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Inventory item'
        verbose_name_plural = 'Inventory items'


class OrderItem(ModelBase):
    quantity = models.FloatField()
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'


class OrderItemHistory(ModelBase):
    amount = models.PositiveIntegerField()
    state = models.CharField(max_length=45)
    notes = models.TextField()
    timestamp = models.DateTimeField()
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'


class Address(ModelBase):
    name = models.CharField(max_length=120)
    add1 = models.CharField(max_length=120)
    add2 = models.CharField(max_length=120)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    zip = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class Invoice(ModelBase):
    creation_date = models.DateTimeField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'


class InvoiceHistory(ModelBase):
    state_desc = models.CharField(max_length=45)
    notes = models.TextField()
    timestamp = models.DateTimeField()
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Invoice history'
        verbose_name_plural = 'Invoice histories'

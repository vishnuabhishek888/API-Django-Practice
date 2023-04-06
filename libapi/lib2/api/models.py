from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
    # libId = models.IntegerField()

class Library(models.Model):
    name = models.CharField(max_length=50)
    writer = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)

    def issue_book(self, num_books):
        if self.quantity >= num_books:
            self.quantity -= num_books
            self.save()
            return True
        else:
            return False


class IssuedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Library, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

@receiver(pre_save, sender=IssuedBook)
def decrease_book_quantity(sender, instance, **kwargs):  
    if instance.pk:  # if the instance already exists
        old_instance = sender.objects.get(pk=instance.pk)
        if old_instance.quantity != instance.quantity:  # if the quantity has been changed
            quantity_diff = old_instance.quantity - instance.quantity
            instance.book.quantity -= quantity_diff
            instance.book.save()
    else:  # if it's a new instance
        instance.book.quantity -= instance.quantity
        instance.book.save()

    

from django.db import models


# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=50)
    amount = models.PositiveIntegerField()
    copies = models.PositiveIntegerField()
    image = models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.book_name

# ORM
# ref=modelName(property=value,pr...)
# ref.save()
# qs=Books(book_name="aa",....)queries
# qs.save()

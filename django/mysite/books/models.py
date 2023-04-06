from django.db import models
import pylint.pyreverse as pr
import datetime

# Create your models here.
from django.utils import timezone


class Book(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(null=True)
    pub_date = models.DateTimeField(blank=True)

    # price = models.FloatField(5, 3)

    def __str__(self):
        return self.name

    # 是否在当前发布的问卷
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Author(models.Model):
    author = models.CharField(max_length=30)
    product = models.ForeignKey(Book, on_delete=models.CASCADE)


    # 在 Django中是 多對一(many-to-one)的關聯
    # 而前方的參數代表的意思就是對應到哪一個類別，這裡對應到的是 Vendor
    # 而後方的 on_delete 代表的是當對應的類別被刪除之後，這些對應到別人的資料要怎麼被處理，而 CASCADE 就是一倂刪除

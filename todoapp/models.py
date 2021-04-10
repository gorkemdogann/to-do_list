from django.db import models
from django.contrib.auth.models import User


class ToDo(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Kullanıcı')
  title = models.CharField(max_length=200,null=True,blank=True,verbose_name='Başlık')
  description = models.TextField(null=True,blank=True,verbose_name='Açıklama')
  complete = models.BooleanField(default=False,verbose_name='Tamamlandı')
  created = models.DateTimeField(auto_now_add=True,verbose_name='Oluşturulma Tarihi')
  last_date = models.DateField(auto_now_add=False, verbose_name="Yetiştirilme Tarihi 'Gün/Ay/Yıl'",null=True)


  def __str__(self):
    return self.title

  class Meta:
    order_with_respect_to = 'user'
    verbose_name_plural = 'ToDo'
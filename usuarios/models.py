from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    whatsapp = models.CharField(max_length=16)
    data_criacao = models.DateTimeField(auto_now=True)
    
    def get_data_criacao(self):
        return self.data_criacao.strftime('%d/%m/%Y as %H:%M hs')

    
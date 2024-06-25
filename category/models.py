from django.db import models
from django.forms import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nome da Categoria')
    
    
    
    class Meta:
        db_table = 'category'

    def __str__(self):
        return str(self.name)

    def clean(self):
        # Verificar se uma categoria com o mesmo nome já existe
        if Category.objects.filter(name=self.name).exists():
            raise ValidationError({'name': 'Esta categoria já existe.'})

    class Meta:
        verbose_name_plural = "Categories"
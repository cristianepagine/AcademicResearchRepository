from django.db import models
from django.core.exceptions import ValidationError
from category.models import Category
from django.contrib.auth.models import User

class Registers(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    title = models.CharField(max_length=200, verbose_name='Titulo Referência')
    autor = models.CharField(max_length=300, blank=True, null=True,  verbose_name='Autor')
    year = models.PositiveIntegerField(verbose_name='Ano')
    objectives = models.CharField(max_length=600, verbose_name='Objetivos')
    database = models.CharField(max_length=150, verbose_name='Base de Dados')
    results = models.CharField(max_length=600, verbose_name='Resultados')
    limitations = models.CharField(max_length=600, verbose_name='Limitações')
    referencies = models.CharField(max_length=600, verbose_name='Referencias')
    dataacess = models.DateTimeField(auto_now=True, verbose_name='Data de Acesso')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')

    class Meta:
        db_table = 'registers'

    def __str__(self):
        return str(self.title)

    def clean(self):
        import datetime

        # Validação para garantir que o ano está entre 1900 e o ano atual
        if self.year < 1900 or self.year > datetime.datetime.now().year:
            raise ValidationError({'year': f'{self.year} não é um ano válido.'})

    def get_data(self):
        return self.dataacess.strftime('%d/ %m/ %Y %H:%M')     

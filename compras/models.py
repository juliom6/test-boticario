from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import RegexValidator


class Compra(models.Model):
    STATUS = (
        ('E', 'Em avaliação'),
        ('A', 'Aprovado'),
    )

    codigo      = models.CharField(max_length=40)
    valor       = models.DecimalField(blank=True, null=True, max_digits=15,  decimal_places=5)
    data        = models.DateTimeField(auto_now_add=True)
    status      = models.CharField(max_length=1, choices=STATUS)
    revendedor  = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo + ' - ' + str(self.data)

    def get_absolute_url(self):
        return reverse('compra_detail', args=[str(self.id)])

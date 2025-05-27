from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone




class Feedback(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    linha = models.IntegerField()
    horario = models.TimeField()
    data = models.DateField()
    avtransport = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
    help_text= "Avaliacao 1 a 5 estrelas"
    )
    avsite = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
    help_text= "Avaliacao 1 a 5 estrelas"
    )
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.email} - {self.telefone} - {self.linha} - {self.horario} - {self.data} - {self.avtransport} - {self.avsite}"



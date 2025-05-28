from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
GENERO_CHOICES = [
    ('masculino', 'Masculino'),
    ('feminino', 'Feminino'),
    ('outro', 'Outro'),
]

IDADE_CHOICES = [
    ('18-25', '18 a 25'),
    ('25-40', '25 a 40'),
    ('40-60', '40 a 60'),
    ('61+', '61 ou mais'),
]


class Feedback(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES, blank=False, null=False)
    idade = models.CharField(max_length=10, choices=IDADE_CHOICES, blank=False, null=False)
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
        return f"{self.nome} - {self.email} - {self.genero} - {self.idade} - {self.telefone} - {self.linha} - {self.horario} - {self.data} - {self.avtransport} - {self.avsite}"



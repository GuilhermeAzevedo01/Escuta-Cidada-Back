from rest_framework import serializers # Importa o ModelSerializer do Django REST Framework, que facilita a criação de serializers baseados em modelos
from .models import Feedback  # Importa o modelo Feedback que você criou

class FeedbackSerializer(serializers.ModelSerializer): # Define um serializer para o modelo Feedback

    class Meta: # A classe Meta é usada para configurar o serializer
        model = Feedback  # Diz qual modelo esse serializer vai usar como base
        fields = '__all__'  # Inclui todos os campos do modelo no serializer

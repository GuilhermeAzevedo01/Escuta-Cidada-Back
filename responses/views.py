from rest_framework import viewsets
from .models import Feedback
from .serializers import FeedbackSerializer


# ViewSet que permite listar, criar, atualizar e deletar feedbacks
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()  # Consulta todos os registros
    serializer_class = FeedbackSerializer  # Usa o serializer criado

    
from rest_framework import viewsets
from .models import Feedback
from .serializers import FeedbackSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# ViewSet que permite listar, criar, atualizar e deletar feedbacks
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()  # Consulta todos os registros
    serializer_class = FeedbackSerializer  # Usa o serializer criado

@api_view(['GET'])
def feedback_list(request):
    feedbacks = Feedback.objects.all()
    serializer = FeedbackSerializer(feedbacks, many=True)
    return Response(serializer.data)
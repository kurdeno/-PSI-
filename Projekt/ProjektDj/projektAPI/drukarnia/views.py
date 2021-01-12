from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Klient
from .serializers import KlientSerializer


@api_view(['GET', 'POST'])
def index(request, format=None):
    if request.method == 'GET':
        questions = Klient.objects.all()
        serializer = KlientSerializer(questions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = KlientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from django.http import HttpResponse
#
#
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
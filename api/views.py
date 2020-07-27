from rest_framework.response import Response
from rest_framework.views import APIView
from howtomaketea.api.tea.ToDoTea import To_Do_Tea
from .serializers import TeaComponents


class HowToMakeTea(APIView):
    def post(self, request):
        try:
            serializer = TeaComponents(data=request.POST)
            serializer.is_valid()
            sugar = serializer.data.get('sugar')
            if sugar and sugar > 0:
                tea = To_Do_Tea(serializer.data['type'], serializer.data['water'], serializer.data['temp'], serializer.data['sugar'])
            else:
                tea = To_Do_Tea(serializer.data['type'], serializer.data['water'], serializer.data['temp'], 0)
            res = tea.conclusion()
        except KeyError:
            res = {
                "error": True,
                "message": "Please enter all info"
            }
        return Response(res)

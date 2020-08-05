from rest_framework.response import Response
from rest_framework.views import APIView
from .tea.TeaMachine import Tea_Machine
# from howtomaketea.api.tea.ToDoTea import To_Do_Tea
from .serializers import PrepareTea, PrepareAdd
from .models import Add, MakeTea
from rest_framework import viewsets


class TeaMachine(APIView):
    def post(self, request):
            machine = PrepareTea(data=request.data)
            if machine.is_valid():
                machine.save()
                temp = machine.data['temp']
                water = machine.data['water']
                addWeRecive = machine.data['adds']
                teaType = machine.data['typeoftea']
                tea = Tea_Machine(water, temp, teaType, addWeRecive)
                res = tea.returnIngr
                result = {
                    "errors": False,
                    "message": res
                }
            else:
                result = {
                    "errors": True,
                    "message": machine.errors
                }
            return Response(result)

    '''Return Tea'''

    def get(self, request):
        res = MakeTea.objects.all()
        serializer = PrepareTea(res, many=True)
        return Response(serializer.data)


'''Return Add'''
class AddGet(APIView):
    def get(self, request):
        addWeRecive = Add.objects.all()
        serializer = PrepareAdd(addWeRecive, many=True)
        return Response(serializer.data)




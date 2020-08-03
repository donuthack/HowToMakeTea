from rest_framework.response import Response
from rest_framework.views import APIView
from .tea.TeaMachine import Tea_Machine
# from howtomaketea.api.tea.ToDoTea import To_Do_Tea
from .serializers import PrepareTea


# class HowToMakeTea(APIView):
#     def post(self, request):
#         try:
#             serializer = TeaComponents(data=request.POST)
#             serializer.is_valid()
#             sugar = serializer.data.get('sugar') #TODO переробити, поставити змінну sugar default = 0
#             if sugar and sugar > 0:
#                 tea = To_Do_Tea(serializer.data['type'], serializer.data['water'], serializer.data['temp'], serializer.data['sugar'])
#             else:
#                 tea = To_Do_Tea(serializer.data['type'], serializer.data['water'], serializer.data['temp'], 0)
#             res = tea.conclusion()
#         except KeyError:
#             res = {
#                 "error": True,
#                 "message": "Please enter all info"
#             }
#         return Response(res)


class TeaMachine(APIView):
    def post(self, request):
        # try:
        #     serializer = PrepareTea(data=request.data)
        #     serializer.is_valid()
        #     print(serializer.is_valid())
        #     x = Tea_Machine(serializer.data['temp'], serializer.data['water'], serializer.data['adds'], serializer.data['typeoftea'])
        #     res = x.returnIngr()
        # except KeyError:
        #     res = {
        #         "error": True,
        #         "message": "Please enter all info"
        #     }
        # return Response(res)


        # serializer = PrepareTea(data=request.data)
        # serializer.is_valid()
        # print(serializer.is_valid())
        # print(serializer.errors)
        # temp = request.data['temp']
        # water = request.data['water']
        # addWeRecive = request.data['adds']
        # teaType = request.data['typeoftea']
        # prepare = Tea_Machine(water, temp, teaType, addWeRecive)
        # res = prepare.returnIngr
        # return Response(res)

        machine = PrepareTea(data=request.data)
        if machine.is_valid():
            temp = machine.data['temp']
            print(567, machine.data)
            water = machine.data['water']
            addWeRecive = machine.data['adds']
            teaType = machine.data['typeoftea']
            tea = Tea_Machine(water, temp, teaType, addWeRecive)
            res = tea.returnIngr
            result = {
                "errors": False,
                "message": res
            }
            # machine.save()
        else:
            result = {
                "errors": True,
                "message": machine.errors
            }
        return Response(result)

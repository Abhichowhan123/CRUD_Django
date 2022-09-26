
from rest_framework.response import Response
from .models import Employee
from .serializers import*
from rest_framework.views import APIView

class EmployeeAPI(APIView):
    def get(self,request,pk = None,format = None):
        id=pk
        if id is not None:
            emp = Employee.objects.get(pk=id)
            serializer= EmployeeSerializer(emp)
            return Response(serializer.data)
        emp = Employee.objects.all()
        serializer= EmployeeSerializer(emp,many = True)
        return Response(serializer.data)

    def post(self,request,format = None):
        serializer= EmployeeSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'data is created'})
        return Response(serializer.errors)
    
    def put(self,request,pk,format = None):
        id=pk
        emp = Employee.objects.get(pk=id)
        serializer= EmployeeSerializer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'data update'})
        return Response(serializer.errors)

    def patch(self,request,pk,format = None):
        id=pk
        emp = Employee.objects.get(id=id)
        serializer= EmployeeSerializer(emp,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'partial data update'})
        return Response(serializer.errors)

    def delete(self,request,pk = None,format = None):
        id=pk
        emp = Employee.objects.get(id=id)
        emp.delete()
        return Response({'message':'data deleted'})

# post
#  {
# "First_name":"abhishek",
# "Last_name":"chowhan",
# "Phone": "8521475647",
# "Email": "abhishek@gmail.com",
# "Department": "math"
# }
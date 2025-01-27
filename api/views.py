from django.shortcuts import render
from . serializers import Bookserilizer
from . models import Books
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

# authentications and permission
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


#Applying Throttle in api to limits the number of request made by annoated,users
from rest_framework.throttling import ScopedRateThrottle # for particular view
from rest_framework.throttling import UserRateThrottle   # for authenticated User
from rest_framework.throttling import AnonRateThrottle   # for non authentucated User



class BookView(APIView):

    #authentication_classes =[BasicAuthentication]
    #authentication_classes =[JWTAuthentication]
    #permission_classes =[IsAuthenticated]

    #throttle_classes =[ScopedRateThrottle]
    
    def get(self,request):
        query = Books.objects.all()
        print(query)
        serilizer = Bookserilizer(query,many=True)
        return Response(serilizer.data)
    
    def post(self, request):
        serializer = Bookserilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BookViewDetails(APIView):
    def get(self,request,pk):
        try:
            query = Books.objects.get(pk=pk)
            serilizer = Bookserilizer(query)
            return Response(serilizer.data)
        except:
            return Response('Not exist') 
    def put(self,request,pk):
        try:
            query =Books.objects.get(pk=pk)
            serilizer = Bookserilizer(query,data = request.data)
            if serilizer.is_valid():
                serilizer.save()
                return Response(serilizer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(f'{id} Not exist') 
        
    def delete(self,request,pk):
        query = Books.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

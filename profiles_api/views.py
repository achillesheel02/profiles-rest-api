from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloAPIView(APIView):
    '''test API vieww'''
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        '''returns a list of APIView features'''
        an_apiview=[
        'Uses HTTP methods as function (get,post,patch,put,delete)',
        'Is similar to traditional django vieww',
        'gives you the most control',
        'is mapped manually to urlsusing=self._db',
        ]

        return Response({'message':'Hello!','an_apivieww':an_apiview})

    def post(self,request):
        '''createa hello message'''
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        '''handle updating'''
        return Response({'method':'PUT'})

    def patch (self,request,pk=None):
        '''handle a partial update'''
        return Response({'method':'PATCH'})

    def delete (self,request,pk=None):
        '''deletean object'''
        return Response({'method':'DELETE'})

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    '''test API vieww'''

    def get(self,request,format=None):
        '''returns a list of APIView features'''
        an_apiview=[
        'Uses HTTP methods as function (get,post,patch,put,delete)',
        'Is similar to traditional django vieww',
        'gives you the most control',
        'is mapped manually to urlsusing=self._db',
        ]

        return Response({'message':'Hello!','an_apivieww':an_apiview})

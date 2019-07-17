from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    '''serializerz'''
    name=serializers.CharField(max_length=10)
    

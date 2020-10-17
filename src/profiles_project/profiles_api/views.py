from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test api view."""

    def get(self,request,format=None):
        """returns a list of APIView features."""

        an_apiview = [
            'Uses http methodsas function(get,post,put,patch,delete)',
            'It is similar to a traditional Django View',
            'Gives you the most control over logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'hello!','an_apiview':an_apiview})

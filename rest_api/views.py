from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MountainDataSerializer
from .models import MountainData


# Create your views here.
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/mountain-list/',
        'Create': '/mountain-create/',
        'Update': '/mountain-update/<str:pk>/',
        'Details': '/mountain/<str:pk>/',
        'Delete': '/mountain-delete/',
    }
    return Response(api_urls)


@api_view(['GET'])
def mountain_list(request):
    mountain_data =MountainData.objects.all().order_by('-id')
    print(mountain_data)
    serializer = MountainDataSerializer(mountain_data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_mountain_data(request):
    try:
        serializer = MountainDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except KeyError as e:
        print(e)


@api_view(['GET'])
def per_mountain_data(request, pk):
    mountain_data = MountainData.objects.get(id=pk)
    serializer = MountainDataSerializer(mountain_data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def update_mountain_data(request, pk):
    mountain_data = MountainData.objects.get(id=pk)
    print(mountain_data)
    serializer = MountainDataSerializer(instance=mountain_data,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def delete_mountain_data(request, pk):
    mountain_data = MountainData.objects.get(id=pk)
    mountain_data.delete()
    return Response('Mountain data deleted successfully')





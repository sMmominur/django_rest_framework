from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from home.models import EiinTbl
from .serializers import EIINSerializer

# Create (POST)
@api_view(['POST'])
def store_eiin(request):
    serializer = EIINSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status_code": status.HTTP_201_CREATED, "payload": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"status_code": status.HTTP_422_UNPROCESSABLE_ENTITY, "errors": serializer.errors, "message": "Validation failed"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

# Read (GET)
@api_view(['GET'])
def home(request):
    eiin = EiinTbl.objects.all()
    serializer = EIINSerializer(eiin, many=True)
    return Response({"status_code": status.HTTP_200_OK, "payload": serializer.data}, status=status.HTTP_200_OK)

# Read Single Item (GET)
@api_view(['GET'])
def get_eiin(request, pk):
    try:
        eiin = EiinTbl.objects.get(pk=pk)
    except EiinTbl.DoesNotExist:
        return Response({"status_code": status.HTTP_404_NOT_FOUND, "message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EIINSerializer(eiin)
    return Response({"status_code": status.HTTP_200_OK, "payload": serializer.data}, status=status.HTTP_200_OK)

# Update (PUT)
@api_view(['PUT'])
def update_eiin(request, pk):
    try:
        eiin = EiinTbl.objects.get(pk=pk)
    except EiinTbl.DoesNotExist:
        return Response({"status_code": status.HTTP_404_NOT_FOUND, "message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = EIINSerializer(eiin, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status_code": status.HTTP_200_OK, "payload": serializer.data}, status=status.HTTP_200_OK)
    return Response({"status_code": status.HTTP_422_UNPROCESSABLE_ENTITY, "errors": serializer.errors, "message": "Validation failed"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

# Delete (DELETE)
@api_view(['DELETE'])
def delete_eiin(request, pk):
    try:
        eiin = EiinTbl.objects.get(pk=pk)
    except EiinTbl.DoesNotExist:
        return Response({"status_code": status.HTTP_404_NOT_FOUND, "message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    eiin.delete()
    return Response({"status_code": status.HTTP_204_NO_CONTENT, "message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from home.models import EiinTbl
from .serializers import EIINSerializer

# Create (POST)
@api_view(['POST'])
def store_eiin(request):
    """
    Creates a new EiinTbl object.
    Returns a 201 response with the created object if successful.
    Returns a 422 response with validation errors if validation fails.
    """
    serializer = EIINSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status_code": status.HTTP_201_CREATED, "payload": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"status_code": status.HTTP_422_UNPROCESSABLE_ENTITY, "errors": serializer.errors, "message": "Validation failed"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

# Read (GET)
@api_view(['GET'])
def get_eiins(request):
    """
    Retrieves a paginated list of EiinTbl objects filtered by optional query parameters:
    'eiin', 'code', 'name', 'district', and 'upazila'.
    Filters are applied dynamically based on the presence of these query parameters in the request.
    The results are paginated and serialized before being returned in the response.
    """
    # Define a mapping of query parameters to model fields
    filter_params = {
        'eiin': 'eiin',
        'code': 'code',
        'name': 'name__icontains',
        'district': 'district',
        'upazila': 'upazila'
    }
    
    # Build the filter criteria dynamically
    filter_criteria = {field: request.query_params.get(param) for param, field in filter_params.items() if request.query_params.get(param) is not None}

    # Filter queryset based on criteria
    eiin_queryset = EiinTbl.objects.filter(**filter_criteria)

    # Paginate queryset
    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(eiin_queryset, request)

    # Serialize data and return response
    serializer = EIINSerializer(result_page, many=True)
    return paginator.get_paginated_response({
        "status_code": status.HTTP_200_OK, 
        "payload": serializer.data
    })

# Read Single Item (GET)
@api_view(['GET'])
def get_eiin(request, pk):
    """
    Retrieves a single EiinTbl object by its primary key (pk).
    Returns a 404 response if the object is not found.
    """
    try:
        eiin = EiinTbl.objects.get(pk=pk)
    except EiinTbl.DoesNotExist:
        return Response({"status_code": status.HTTP_404_NOT_FOUND, "message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EIINSerializer(eiin)
    return Response({"status_code": status.HTTP_200_OK, "payload": serializer.data}, status=status.HTTP_200_OK)

# Update (PUT)
@api_view(['PUT'])
def update_eiin(request, pk):
    """
    Updates an existing EiinTbl object identified by its primary key (pk).
    Returns a 404 response if the object is not found.
    Returns a 200 response with the updated object if successful.
    Returns a 422 response with validation errors if validation fails.
    """
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
    """
    Deletes a single EiinTbl object by its primary key (pk).
    Returns a 404 response if the object is not found.
    """
    try:
        eiin = EiinTbl.objects.get(pk=pk)
    except EiinTbl.DoesNotExist:
        return Response({"status_code": status.HTTP_404_NOT_FOUND, "message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    eiin.delete()
    return Response({"status_code": status.HTTP_204_NO_CONTENT, "message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

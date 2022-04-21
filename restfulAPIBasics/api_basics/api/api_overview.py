from rest_framework.decorators import api_view
from rest_framework.response import Response    # throw the response in the DRF UI



@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'API Overview': 'api/',
        'Func-based-views': 'api/func-based/',
        'Class-based-views': 'api/class-based/',
    }
    return Response(api_urls)

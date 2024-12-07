from rest_framework.views import APIView, Response

from .serializers import SupplierSerializer
from .models import Supplier
# Create your views here.
class SupplierList(APIView):
  def get(self, request):
    queryset = Supplier.objects.all()
    suppliers = SupplierSerializer(queryset, many=True)
    return Response(suppliers.data)
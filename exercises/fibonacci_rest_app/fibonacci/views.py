from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .fibonacci_numbers import get_fibonacci_numbers


class FibonacciNumbersView(APIView):
    def get(self, request, **kwargs):
        try:
            n = int(request.query_params.get("n"))
        except (ValueError, TypeError) as e:
            return Response({"error_message": str(e)}, status=HTTP_400_BAD_REQUEST)
        return Response({"fibinacci_numbers": get_fibonacci_numbers(n),
                         "n": n})


class FibonacciNumbersNInPathView(APIView):
    def get(self, request, n, **kwargs):
        return Response({"fibinacci_numbers": get_fibonacci_numbers(n), "n": n})

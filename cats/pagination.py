from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CatsPagination(PageNumberPagination):
    page_size = 5

    # def paginate_queryset(self, queryset, request, view=None):
    #     print(queryset, request)
    def get_paginated_response(self, data):
        return Response({
            'response': data
        })
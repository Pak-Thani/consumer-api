from rest_framework import pagination

class CustomPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'limit'
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return {
            'products': data,
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total_element': self.page.paginator.count,
            'total_page': self.page.paginator.num_pages,
        }
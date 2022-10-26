

from django.core.exceptions import PermissionDenied
import time

class FilterIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.counter = 0

    def __call__(self, request):

        # allowed_ips = ['127.0.0.1']
        allowed_ips = []
        ip = request.META.get('REMOTE_ADDR')
        # if ip not in allowed_ips:

        if ip in allowed_ips:
            raise PermissionDenied
        # time.sleep(0.5)
        response = self.get_response(request)
        # time.sleep(1)

        # if self.counter == 3:
        #     time.sleep(2)
        #     self.counter = 0
        # else:
        #     self.counter += 1

        return response

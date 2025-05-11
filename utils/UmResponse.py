import json

from django.http import HttpResponse, JsonResponse


class UmResponse:
    status_200 = 200
    status_500 = 500

    @staticmethod
    def gen(status, data):
        return HttpResponse(json.dumps({
            "status": status,
            "data": data
        }), content_type="application/json")

    @staticmethod
    def convert_data(data):
        rst_list = []
        for m in data:
            rst_list.append(m.__str__())
        return rst_list

    @staticmethod
    def jr_gen(status, data):
        return JsonResponse({"status": status, "data": data}, safe=False)

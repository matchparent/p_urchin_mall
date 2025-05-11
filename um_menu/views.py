import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from um_menu.models import MainMenu, SubMenu
from utils.UmResponse import UmResponse


# Create your views here.
class MainMenuView(View):

    def get(self, request):
        menu_m = MainMenu.objects.all()
        rst_list = []
        rst_json = {}
        for m in menu_m:
            rst_list.append(m.__str__())
        rst_json['status'] = 200
        rst_json['data'] = rst_list
        return HttpResponse(json.dumps(rst_json), content_type="application/json")
        # return HttpResponse('menu get')

    def post(self, request):
        return HttpResponse('menu post')


class SubMenuView(View):
    def get(self, request):
        menu = SubMenu.objects.filter(main_menu_id=request.GET["main_menu_id"])
        rst_list = []
        for m in menu:
            rst_list.append(m.__str__())
        return UmResponse.gen(UmResponse.status_200, rst_list)
        # return HttpResponse('menu get')

    def post(self, request):
        return HttpResponse('sub menu post')

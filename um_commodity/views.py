import json

from django.shortcuts import render
from rest_framework.views import APIView

from um_commodity.models import Goods, GoodsSerializer
from um_comment.models import Comment
from utils.UmResponse import UmResponse
from copy import deepcopy
from utils.Encoders import DecimalEncoder
from urchin_mall.settings import IMAGE_URL

PageCount = 20


# Create your views here.
class CommodityCategoryAPIView(APIView):
    def get(self, request, cateid, page):
        cursor_start = (page - 1) * PageCount
        cursor_end = page * PageCount
        data = Goods.objects.filter(type_id=cateid).all()[cursor_start:cursor_end]
        return UmResponse.gen(UmResponse.status_200, UmResponse.convert_data(data))


class CommodityDetailAPIView(APIView):
    def get(self, request, sku_id):
        data = Goods.objects.filter(sku_id=sku_id).first()
        rst = GoodsSerializer(instance=data)
        c = Comment.objects.filter(sku_id=sku_id).count()
        return UmResponse.gen(UmResponse.status_200, {"list": rst.data, "comment_count": c})


class CommodityFlashSaleAPIView(APIView):

    def get(self, request):
        data = Goods.objects.filter(find=1).all()
        rst = GoodsSerializer(instance=data, many=True)
        result = deepcopy(rst.data)
        for item in result:
            if 'image' in item and isinstance(item['image'], str):
                item['image'] = item['image'].replace('http://127.0.0.1:8000', IMAGE_URL)

        return UmResponse.gen(UmResponse.status_200, result)


class CommoditySearchAPIView(APIView):
    order_dict = {
        1: "g.name",
        2: "r.comment_count",
        3: "g.p_price"
    }

    def get(self, request, keyword, page, order_by):
        page_from = (page - 1) * 15
        from django.db import connection
        from django.conf import settings

        sql = """
        select r.comment_count,concat('{}',g.image) as img,g.name,g.p_price,g.shop_name,g.sku_id from goods g
            left join(
            select count(c.sku_id) as comment_count,c.sku_id from comment c group by c.sku_id
            ) r
            on g.sku_id=r.sku_id
            where g.name like"%{}%"
            order by {} desc limit {},15;

        """.format(settings.IMAGE_URL, keyword, self.order_dict[order_by], page_from)

        with connection.cursor() as cursor:
            cursor.execute(sql)
            res = self.fetch_all(cursor)
            rst = []
            for item in res:
                rst.append(json.dumps(item, cls=DecimalEncoder, ensure_ascii=False))

        sql = "select count(*) from goods where name like '%{}%'".format(keyword)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            num = cursor.fetchone()
            total_count = num[0]

        # return UmResponse.gen(UmResponse.status_200, {"list": rst, "maxpage": ((total_count // 15) + 1)})
        return UmResponse.gen(UmResponse.status_200, {"list": rst, "count": total_count})

    def fetch_all(self, cursor):
        desc = cursor.description
        return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]

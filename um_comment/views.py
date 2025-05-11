from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination

from um_comment.models import Comment, CommentSerializer
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


class CommentPagination(PageNumberPagination):
    page_size = 15
    page_query_param = 'page'  # 默认就是 'page'，写出来更清晰
    max_page_size = 100


# ViewSetMixin has to be the first, for that GenericAPIView.as_view() don't take parameters
# dispatch() is not in ViewSetMixin, so GenericAPIView or APIView or View must be extended
class CommentGAV(ViewSetMixin, GenericAPIView, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
                 DestroyModelMixin,
                 ListModelMixin):
    queryset = Comment.objects
    serializer_class = CommentSerializer

    def singlee(self, request, pk):
        return self.retrieve(request, pk)

    # def listt(self, request):
    #     return self.list(request)
    # def listt(self, request):
    #     return Response({"status": 200, "data": self.list(request).data})

    pagination_class = CommentPagination  # ✅ 指定分页器

    def listt(self, request):
        # 可选参数过滤（如 ?sku_id=xxx）
        queryset = self.filter_queryset(self.get_queryset())

        sku_id = request.GET.get('sku_id')
        if sku_id:
            queryset = queryset.filter(sku_id=sku_id)

        # 分页处理
        try:
            page = self.paginate_queryset(queryset)
        except NotFound:
            return Response({"status": 500, "data": "page not found"})

        # only when pagination_class not set, page can be none. if can't find anything, page = []
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return Response({
                "status": 200,
                "data": serializer.data
            })

        # # 无分页 fallback
        # serializer = self.get_serializer(queryset, many=True)
        # return Response({
        #     "status": 500,
        #     "data": serializer.data
        # })

    def editt(self, request, pk):
        return self.update(request, pk)

    def createe(self, request):
        return self.create(request)

    def delette(self, request, pk):
        return self.destroy(request, pk)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@CreateTime    : 2019/6/27
@Author  : Easou Chen
@file:  ServerInfoView
@for :
"""
from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.views import APIView
from server_info.models import ServerInfo, AppTypes
from utils.share_view import ShareView


# 服务器应用类型
class ServerAppView(ShareView):
    def get(self, request):
        rd = {'error_code': '200', 'error_message': '请求成功'}
        data = AppTypes.objects.all().values("name", "parent_id", "parent__name","is_active", "description")
        rd['results'] = data
        return Response(rd)

    def get_model(self):
        model = AppTypes
        return model



class ServerInfoView(APIView):
    """
        服务器基础信息
    """
    def post(self, request):
        rd = {'error_code': '200', 'error_message': '请求成功'}
        data = request.data
        if "id" not in data.keys():
            ServerInfo.objects.get_or_create(**data)
        else:
            data = ServerInfo.objects.filter(**data)
            if data.exists():
                rd['error_code'] = '4000'
                rd['error_message'] = '数据已存在，无需更新'
            else:
                data['update_time'] = now()
                ServerInfo.objects.filter(id=data.pop('id')).update(**data)
        return Response(rd)






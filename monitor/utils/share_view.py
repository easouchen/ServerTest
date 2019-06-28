#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@CreateTime    : 2019/6/27
@Author  : Easou Chen
@file:  share_view
@for :  这个是公用的view, 简单一些的post接口，可以直接使用本view
"""
from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.views import APIView
from server_info.models import ServerInfo


class ShareView(APIView):
    def post(self, request):
        rd = {'error_code': '200', 'error_message': '请求成功'}
        data = request.data
        my_model = self.get_model()
        if "id" not in data.keys():
            my_model.objects.get_or_create(**data)
        else:
            data = my_model.objects.filter(**data)
            if data.exists():
                rd['error_code'] = '4000'
                rd['error_message'] = '数据已存在，无需更新'
            else:
                data['update_time'] = now()
                my_model.objects.filter(id=data.pop('id')).update(**data)
        return Response(rd)

    def get_model(self, model=None):
        return model

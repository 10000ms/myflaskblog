# -*- coding: utf-8 -*-
import datetime

from django.db import models

from ip_region import search


class RegionRecordManager(models.Manager):

    def _today_record(self, region):
        c = self.filter(date=datetime.date.today(), region__id=region.id)
        if not c.exists():
            m = self.create()
            m.region.add(region)
        else:
            m = c[0]
        return m

    def add_ip(self, ip):
        s = search.Ip2Region().search(ip)
        city_id = s['city_id']
        if city_id != 0:
            region_manage = self.model.region.field.remote_field.model.objects
            region = region_manage.city_from_city_id(city_id)
            if region is not None:
                m = self._today_record(region)
                m.count += 1
                m.save()
            else:
                # TODO
                pass

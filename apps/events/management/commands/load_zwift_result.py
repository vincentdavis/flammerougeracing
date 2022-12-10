import logging
import sys

import requests
from django.core.management import BaseCommand

from apps.events.api.serailizers import ZwiftResultSerializers
from apps.events.models import ZwiftResult
from apps.events.zwiftAPI import ZwiftPowerAPI


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('zwift_id', type=int, help='help for n')

    def handle(self, *args, **options):
        zwift_id = options.get('zwift_id', None)
        if zwift_id:
            zp_api = ZwiftPowerAPI()
            zp_api.load_result(zwift_id)
            # ZwiftResult.objects.filter(zwift_id=zwift_id).delete()
            # re = requests.get(f"https://zwiftapi.weracehere.org/results_view?zid={zwift_id}&refresh=true")
            # zs = ZwiftResultSerializers(data=re.json().get('data', []), many=True)
            # if zs.is_valid(raise_exception=True):
            #     zs.save(zwift_id=zwift_id)
            # for result in re.json().get('data', []):
            #     print(result)
            #     break



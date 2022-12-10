import requests

from apps.events.api.serailizers import ZwiftResultSerializers
from apps.events.models import ZwiftResult


class ZwiftPowerAPI():
    def load_result(self, zp_event_id):
        ZwiftResult.objects.filter(zwift_id=zp_event_id).delete()
        re = requests.get(f"https://zwiftapi.weracehere.org/results_view?zid={zp_event_id}&refresh=true")
        zs = ZwiftResultSerializers(data=re.json().get('data', []), many=True)
        if zs.is_valid(raise_exception=True):
            zs.save(zwift_id=zp_event_id)
from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer

from apps.advert.models import AdvertModel
from apps.advert.serializers import AdvertSerializer


class AdvertConsumer(GenericAsyncAPIConsumer):
    def __init__(self, *args, **kwargs):
        self.room_name = 'adverts'
        super().__init__(*args, **kwargs)

    async def connect(self):
        if not self.scope['user']:
            await self.close()
            return

        await self.accept()
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name,
        )

    @model_observer(AdvertModel, serializer_class=AdvertSerializer)
    async def adverts_activity(self, message, action, subscribing_req_id, **kwargs):
        for req_id in subscribing_req_id:
            await self.reply(data=message, action=action, request_id=req_id)

    @action()
    async def sub_to_advers_activity(self, req_id, **kwargs):
        await self.adverts_activity.subscribe(req_id=req_id)

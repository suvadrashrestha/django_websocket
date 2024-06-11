from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import Chat,Group
from channels.db import database_sync_to_async
class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
  # The connect method doesnot take any arguments 
    async def connect(self):
        self.group_name=self.scope['url_route']["kwargs"]['groupname']
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()
    # the content aspects json formatted message so that it could deserialize it
    async def receive_json(self, content, **kwargs): 
       group=await database_sync_to_async( Group.objects.get)(name=self.group_name)
       chat= Chat(content=content['message'],group=group)

       await database_sync_to_async(chat.save)()
       # sending data to group
       await self.channel_layer.group_send(self.group_name,{
           "type":"chat.message",
            "message":content
       })
 # sending data to one
    async def chat_message(self,content):
        await self.send_json(content['message'])

          
        

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name,self.channel_name)
        print('disonneted',code)
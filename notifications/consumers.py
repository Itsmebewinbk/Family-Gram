import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "notification__room"
        self.room_group_name = "notification_group"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({"message": "connected"}))

    def receive(self, text_data):
        print(text_data)
        self.send(
            text_data=json.dumps({"message": "we have bought your datas"})
        )

    def disconnect(self, close_code):
        print("disconnected")

    def send_notification(self, event):
        print(event)

        self.send(text_data=event.get("value"))

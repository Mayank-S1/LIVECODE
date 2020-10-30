from django.db import models
from django.core.validators import MinLengthValidator


class User(models.Model):
    room_name = models.CharField(max_length=50)
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    def get_user_by_roomname(room_name):
        try:
            return User.objects.get(room_name=room_name)
        except:
            return False

    def get_user_by_password(password):
        try:
            return User.objects.get(password=password)
        except:
            return False


    def isExists(self):
        if User.objects.filter(room_name=self.room_name):
            return True

        return False

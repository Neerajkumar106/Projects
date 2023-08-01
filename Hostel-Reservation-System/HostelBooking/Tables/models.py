from django.db import models
import uuid
from django.contrib.auth.models import User
    
class Website(models.Model):
    brand_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    brand_name = models.CharField(max_length=100)
    def __str__(self):
        return self.brand_name
    
class FLOOR(models.Model):
    floor_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    floor_no = models.IntegerField()
    def __str__(self):
        return str(self.floor_no)
    
class ROOM(models.Model):
    room_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    room_no = models.IntegerField()
    room_status = models.BooleanField(default='true')
    floor = models.ForeignKey(FLOOR, on_delete=models.CASCADE,)
    def __str__(self):
        return str(self.room_no)
    
class REQ_ROOM(models.Model):
    req_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ROOM, on_delete=models.CASCADE ,default='')
    def __str__(self):
        return self.user.first_name

class Complaint(models.Model):
    stu_name = models.CharField(max_length=20)
    stu_email = models.EmailField(max_length=200)
    room_no = models.ForeignKey(ROOM, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=500)
    def __str__(self):
        return self.stu_name.stu_email
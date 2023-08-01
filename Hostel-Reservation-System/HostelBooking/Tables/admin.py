from django.contrib import admin

from .models import ROOM,FLOOR,Website,REQ_ROOM

@admin.register(ROOM)
class room_admin(admin.ModelAdmin):
    list_display=['room_no','room_status','room_id']
    search_fields=['room_no',]
    list_filter=['room_status',]

@admin.register(FLOOR)
class floor_admin(admin.ModelAdmin):
    list_display=['floor_no',]

@admin.register(Website)
class web_admin(admin.ModelAdmin):
    list_display=['brand_name',]

@admin.register(REQ_ROOM)
class req_admin(admin.ModelAdmin):
    list_display=['req_id',]
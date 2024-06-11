from django.contrib import admin

# Register your models here.
from .models import Chat,Group
class ChatAdmin(admin.ModelAdmin):
    list_display=['content','group',]
class GroupAdmin(admin.ModelAdmin):
    list_display=['name',]

admin.site.register(Chat,ChatAdmin)
admin.site.register(Group,GroupAdmin)
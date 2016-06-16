from django.contrib import admin
from .models import CategoriesNeeds, Room, ChatMessage

admin.site.register(
    CategoriesNeeds,
    list_display=["name"],

)

admin.site.register(
	Room,
	list_display=["name","user_req", "slug", "need"],
	prepopulated_fields={"slug": ("name",)},

)

admin.site.register(
	ChatMessage,
	list_display=["author","date", "room", "text"],

)
# Register your models here.

from django.contrib import admin

from .models import Items, Bid, Comments, User
# Register your models here.
class ItemsAdmin(admin.ModelAdmin):
    list_display = ("title","description", "image", "startingBid")

# class CommentAdmin(admin.ModelAdmin):
#     filter_horizontal = ("items",)

admin.site.register(Items, ItemsAdmin)
admin.site.register(Bid)
admin.site.register(Comments)
admin.site.register(User)

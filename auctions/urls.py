from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:Items_id>", views.items, name="item_page"),
    path("commet/<int:Items_id>", views.comment, name="comment"),
    path("delete/<int:Items_id>", views.delete, name="delete_item"),
    path("finished/<int:Items_id>", views.finished, name="auction_finished"),
    path("add", views.add, name = "add"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")

]

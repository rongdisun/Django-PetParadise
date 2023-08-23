from django.urls import path
from .views import *

app_name = "pet"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("pet_detail/<int:pk>", PetDetailView.as_view(), name="pet_detail"),
    path("apply_adopt/<int:pk>", apply_adopt, name="apply_adopt"),
    path("adopt_log/", AdoptLog.as_view(), name="adopt_log"),
    path("add_image_for_pet/", add_image_for_pet, name="add_image_for_pet"),

    # 商城视图
    path("mall_index/", PetMall.as_view(), name="mall_index"),
    path("goods_detail/<pk>", GoodsDetail.as_view(), name="goods_detail"),
    path("goods_favorite/", goods_favorite, name="goods_favorite"),
    path("submit_order_view/<goods_pk>", submit_order_view, name="submit_order_view"),
    path("submit_order/", submit_order, name="submit_order"),
    path("favorite_list/", FavoriteListView.as_view(), name="favorite_list"),
    path("order_list/", OrderListView.as_view(), name="order_list"),


    # 管理员视图
    path("admin_add_pet/", AdminAddPet.as_view(), name="admin_add_pet"),
    path("admin_all_pet/", AdminAllPet.as_view(), name="admin_all_pet"),
    path("admin_pet_detail/<pk>", AdminPetDetail.as_view(), name="admin_pet_detail"),
    path("admin_pet_update/<pk>", AdminPetUpdate.as_view(), name="admin_pet_update"),
    path("admin_delete_pet/<pk>", admin_delete_pet, name="admin_delete_pet"),
    path("admin_all_adopt_pet/", AdminAllAdoptPetView.as_view(), name="admin_all_adopt_pet"),
    path("admin_manage_user_apply_adopt/", admin_manage_user_apply_adopt, name="admin_manage_user_apply_adopt"),
    path("admin_all_pet_goods/", AdminAllPetGoods.as_view(), name="admin_all_pet_goods"),
    path("admin_add_pet_goods/", AdminAddPetGoods.as_view(), name="admin_add_pet_goods"),
    path("admin_pet_goods_detail/<pk>", AdminPetGoodsDetail.as_view(), name="admin_pet_goods_detail"),
    path("admin_pet_goods_update/<pk>", AdminPetGoodsUpdate.as_view(), name="admin_pet_goods_update"),
    path("admin_all_order/", AdminAllOrder.as_view(), name="admin_all_order"),

    path("admin_all_user/", AdminAllUserView.as_view(), name="admin_all_user"),
    path("admin_user_status_change/", admin_user_status_change, name="admin_user_status_change"),
    path("admin_delete_user/<user_id>", admin_delete_user, name="admin_delete_user"),
    path("adin_all_post/", AdminAllPost.as_view(), name="admin_all_post"),
    path("admin_delete_post/<pk>", admin_delete_post, name="admin_delete_post")


]

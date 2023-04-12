from django.urls import path
from .views import OrderView, OrderItemView, ItemView, SingleItemView, CartView, CategoryView, SingleOrderView
from .views import ManagersView, DeliveryCrewsView, SingleManagerView, SingleDeliveryCrewView

urlpatterns=[
    path('orders/', OrderView.as_view()),
    path('orders/<int:pk>/',  SingleOrderView.as_view()),
    path('orders/items/', OrderItemView.as_view()),
    path('items/', ItemView.as_view()),
    path('items/<int:pk>/', SingleItemView.as_view()),
    path('carts/', CartView.as_view()),
    path('categorys/', CategoryView.as_view()),
    path('groups/manager/users/', ManagersView.as_view()),
    path('groups/manager/users/<int:pk>/', SingleManagerView.as_view()),
    path('groups/delivery-crew/users/', DeliveryCrewsView.as_view()),
    path('groups/delivery-crew/users/<int:pk>/', SingleDeliveryCrewView.as_view()),
]
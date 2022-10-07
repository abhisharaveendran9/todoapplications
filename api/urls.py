from django.urls import path
from api.views import TodosView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("todos",TodosView,basename="todos")

urlpatterns=[

]+router.urls
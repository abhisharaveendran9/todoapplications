from django.urls import path
from todoapp import views

urlpatterns=[
    path("signup",views.SignUpView.as_view(),name="register"),
    path("",views.LoginView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="index"),
    path("signout",views.SignOutView.as_view(),name="signout"),
    path("todos/add",views.TodoAddView.as_view(),name="add-todo"),
    path("todos/all",views.TodoListView.as_view(),name="todos-list"),
    path("todos/remove/<int:id>",views.delete_todo,name="remove-todo"),
    path("todos/details/<int:id>",views.TodoDetailView.as_view(),name="todo-detail"),
    path("todos/change/<int:id>",views.TodoEditView.as_view(),name="edit-todo")
]
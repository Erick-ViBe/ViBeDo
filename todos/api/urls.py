from django.urls import path

from todos.api import views as ViewsTodos

urlpatterns = [
    path(
        "create/todo/",
        ViewsTodos.TodoCreateAPIView.as_view(),
        name="todo-create",
    ),
    path(
        "todos/",
        ViewsTodos.TodoListAPIView.as_view(),
        name="todo-list"
    ),
    path(
        "todo/<int:pk>/",
        ViewsTodos.TodoRetrieveUpdateDestroyAPIView.as_view(),
        name="todo-detail"
    ),
    path(
        "state/todo/<int:pk>/",
        ViewsTodos.TodoChangeDoneStateAPIView.as_view(),
        name="todo-change-state"
    ),
]

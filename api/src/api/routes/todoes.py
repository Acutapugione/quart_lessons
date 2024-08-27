from dataclasses import dataclass
from datetime import datetime
from quart_schema import validate_request, validate_response
from .. import app


@dataclass
class TodoIn:
    task: str
    due: datetime | None


@dataclass
class Todo(TodoIn):
    id: int


todoes = dict()


@app.post("/todos/")
@validate_request(TodoIn)
@validate_response(Todo)
async def create_todo(data: TodoIn) -> Todo:
    todo = Todo(id=len(todoes), task=data.task, due=data.due)
    todoes.update({todo.id: todo})
    return todo


@app.get("/todos/<int:id>", defaults={"id": 0})
async def get_todo(id: int) -> Todo:
    return todoes.get(id)


# @validate_request(Todo)

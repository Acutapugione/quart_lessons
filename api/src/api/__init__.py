from quart import Quart
from quart_schema import QuartSchema


app = Quart(__name__)
QuartSchema(app)

from .routes import TodoIn


def run() -> None:
    app.run()

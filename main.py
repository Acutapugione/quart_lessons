from quart import Quart, render_template, websocket

app = Quart(__name__)


@app.get("/")
async def index():
    return await render_template("index.html")


@app.get("/api")
async def api():
    return {"hello": "world"}


@app.websocket("/ws")
async def ws():
    await websocket.accept()
    await websocket.send("hello from backend")
    await websocket.send_json({"hello from": "backend"})


if __name__ == "__main__":
    app.run()

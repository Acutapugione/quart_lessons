from quart import request
from .. import app


@app.post("/echo")
async def echo():
    """returns back your request data"""
    data = await request.get_json()
    return {"input": data, "extra": True}

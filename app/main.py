from fastapi import FastAPI
import router
import asyncio

app = FastAPI()

@app.get("/")
async def hello():
    return {'message': 'Hello world'}

app.include_router(router.route)
asyncio.create_task(router.consume())
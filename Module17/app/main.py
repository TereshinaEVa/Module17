from fastapi import FastAPI
from .routers.task import router as tr
from .routers.user import router as ur

app = FastAPI(swagger_ui_parameters={'tryItOutEnabled': True})


@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(tr)
app.include_router(ur)

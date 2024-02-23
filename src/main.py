from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn

from models.models import ButtonModel, ButtonsStage

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

stage = ButtonsStage(one = False, two = False)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html")

@app.get('/state')
async def state():
    return stage

@app.post('/change')
async def change(data: ButtonModel):
    
    match data.id:
        case 'one':
            stage.one = bool(data.on)
        case 'two':
            stage.two = bool(data.on)

    return {'status': 'OK'}

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0')
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.models.models import ButtonModel, ButtonsStage
# from src.config import settings

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/static"), name="static")


templates = Jinja2Templates(directory="src/templates")

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

    print(f"[INFO!] State {data.id}: Сhanged from '{not stage.one}' to '{stage.one}'")

    return {'status': 'OK'}
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models.models import ButtonModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

buttons = {
    'one': True,
    'two': False
}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context=buttons)

@app.get('/state')
async def state():
    return {'one': buttons["one"], 'two': buttons["two"]}

@app.post('/change')
async def change(data: ButtonModel):
    buttons[data.id] = bool(data.on)
    print(data.id, data.on)

    print(buttons)
    return {'status': 'OK'}
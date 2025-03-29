from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="views")

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/historial", response_class=HTMLResponse)
def show_historial(request: Request):
    return templates.TemplateResponse("historial.html", {"request": request})

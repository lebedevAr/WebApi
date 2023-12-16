from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import models

from database import engine
from routes import router_websocket, router_categories, router_items

# Создание таблиц в БД
models.Base.metadata.create_all(bind=engine)

# Templates
templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="WebSocketChatCRUDNotify",
    summary="WebSocket Chat + Notifications of CRUD operations!",
    version="0.0.1",
)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    server_urn = f"{request.scope.get('server')[0]}:{request.scope.get('server')[1]}"
    return templates.TemplateResponse("index.html", {"request": request, "server_urn": server_urn})


# Подключаем созданные роутеры в приложение
app.include_router(router_websocket)
app.include_router(router_categories)
app.include_router(router_items)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import models
import uvicorn
from database import engine
from routes import router_websocket, router_categories, router_items


models.Base.metadata.create_all(bind=engine)

# Templates
templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="WebSocketChatCRUDNotify",
    summary="WebSocket | Chat | Notifications of CRUD operations",
    version="0.0.1",
)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    http_protocol = request.headers.get("x-forwarded-proto", "http")
    ws_protocol = 'ws'

    if http_protocol == 'https':
        ws_protocol = 'wss'

    server_urn = request.url.netloc
    return templates.TemplateResponse("index.html",
                                      {"request": request,
                                       "http_protocol": http_protocol,
                                       "ws_protocol": ws_protocol,
                                       "server_urn": server_urn})


app.include_router(router_websocket)
app.include_router(router_categories)
app.include_router(router_items)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)

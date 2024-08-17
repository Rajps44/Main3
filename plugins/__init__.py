from aiohttp import web
from .route import routes


async def web_server():
    web_app = web.Application(client_max_size=4294967296)  # 4 GB in bytes
    web_app.add_routes(routes)
    return web_app


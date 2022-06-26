import sys

from backend.app import get_app
from hypercorn.asyncio import serve
from hypercorn.config import Config
import asyncio

if sys.platform == "win32" and sys.version_info >= (3, 8, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def run_api():
    config = Config()
    config.bind = ['localhost:8001']

    app = get_app()

    await serve(app=app, config=config)


async def main():
    await run_api()

if __name__ == '__main__':
    asyncio.run(main())

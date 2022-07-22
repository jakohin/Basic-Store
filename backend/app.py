import datetime

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from db.db_handler import DatabaseHandler


def get_app():
    dbh = DatabaseHandler("db/data/db.sqlite")
    app = FastAPI()
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    @app.get('/items/all')
    def get_all_items():
        try:
            return JSONResponse(dbh.get_all_items())
        except Exception as e:
            return JSONResponse({"error": f"{e}"})

    @app.get('/items/{_id}')
    def get_item(_id: int):
        try:
            return JSONResponse(dbh.get_item(_id))
        except Exception as e:
            return JSONResponse({"error": f"{e}"})

    @app.put('/items/create')
    def create_item(name: str, desc: str, price: float, stock: int, images, release_date=None):
        if not release_date:
            release_date = datetime.datetime.now().date()
        # TODO: Implement authorization
        # if password == "":
        try:
            dbh.create_item(name, desc, price, stock, images)
        except Exception as e:
            print(e)
            return JSONResponse({"error": f"{e}"})
        return JSONResponse({"code": "success"})
        # return JSONResponse({"error": "Not authorized"})

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app

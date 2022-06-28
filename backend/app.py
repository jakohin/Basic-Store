from fastapi import FastAPI
from fastapi.responses import JSONResponse
import sqlite3 as sq3

from fastapi.middleware.cors import CORSMiddleware


def create_db(conn: sq3.Connection):
    cur = conn.cursor()
    cur.execute(r"create table if not exists images("
                r"id integer primary key autoincrement not null,"
                r"url text not null,"
                r"item_id integer not null,"
                r"foreign key (item_id) references items(id));")
    cur.execute(r"create table if not exists items("
                r"id integer primary key autoincrement not null,"
                r"name text not null,"
                r"desc text not null,"
                r"price float not null,"
                r"stock integer not null,"
                r"sold integer not null)")


def item_to_dict(item, images):
    return {
        "id": item[0],
        "name": item[1],
        "desc": item[2],
        "price": item[3],
        "stock": item[4],
        "sold": item[5],
        "images": images[0] if len(images) > 0 else []
    }


def get_app():
    db_file = "db/db.sqlite"
    try:
        conn = sq3.connect(db_file, check_same_thread=False)
    except sq3.OperationalError:
        open(db_file, 'a').close()
        conn = sq3.connect(db_file, check_same_thread=False)

    app = FastAPI()

    @app.get('/items/all')
    def get_all_items():
        items = []
        try:
            cur = conn.cursor()
            cur.execute("Select * from items")
            items = []
            for item in cur.fetchall():
                cur.execute("Select url from images where item_id == ?", [item[0]])
                images = cur.fetchall()
                items.append(item_to_dict(item, images))
            return JSONResponse({"items": items})
        except Exception as e:
            return JSONResponse({"error": f"{e}"})

    @app.get('/items/{_id}')
    def get_item(_id: int):
        try:
            cur = conn.cursor()
            cur.execute("Select * from items where id == ?", [int(_id)])
            item = cur.fetchone()
            cur.execute("Select url from images where item_id == ?", [int(_id)])
            images = cur.fetchall()
            if len(item) > 0:
                return JSONResponse({"item": item_to_dict(item, images)} if item else {})
        except Exception as e:
            return JSONResponse({"error": f"{e}"})

    @app.put('/items/create')
    def create_item(name: str, desc: str, price: float, stock: int):
        # if password == "asgdUIGERFLIjshgDkjshhkh":
        try:
            print(name, desc, price, stock)
            cur = conn.cursor()
            cur.execute("insert into items (name, desc, price, stock, sold)"
                        f"values (?, ?, ?, ?, 0)", [str(name), str(desc), float(price), int(stock)])
            conn.commit()
        except Exception as e:
            print(e)
            return JSONResponse({"error": f"{e}"})
        return JSONResponse({"code": "success"})
        # return JSONResponse({"error": "Not autherized"})

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app




if __name__ == '__main__':
    create_db(sq3.connect("db/db.sqlite"))

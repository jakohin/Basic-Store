import sqlite3 as sq3


class DatabaseHandler (object):
    def __init__(self, db_file):
        try:
            self.conn = sq3.connect(db_file, check_same_thread=False)
        except sq3.OperationalError:
            open(db_file, 'w').close()
            self.conn = sq3.connect(db_file, check_same_thread=False)


    def create_db(self):
        cur = self.conn.cursor()
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
        self.conn.commit()

    def get_all_items(self):
        items = []
        cur = self.conn.cursor()
        cur.execute("Select * from items")
        for item in cur.fetchall():
            cur.execute("Select url from images where item_id == ?", [item[0]])
            images = cur.fetchall()
            items.append(item_to_dict(item, images))
        return {"items": items}

    def get_item(self, item_id):
        cur = conn.cursor()
        cur.execute("Select * from items where id == ?", [int(item_id)])
        item = cur.fetchone()
        if len(item) <= 0:
            return {"error": f"No item with id '{item_id}' exists!"}
        cur.execute("Select url from images where item_id == ?", [int(item_id)])
        images = cur.fetchall()
        return {item_to_dict(item, images)}

    def create_item(self, name, desc, price, stock, images):
        cur = self.conn.cursor()

        cur.execute("insert into items (name, desc, price, stock, sold)"
                    f"values (?, ?, ?, ?, 0)", [str(name), str(desc), float(price), int(stock)])
        self.conn.commit()
        cur.execute('select seq from sqlite_sequence where name="items"')
        item_id = cur.fetchone()
        for image in images:
            cur.execute("insert into images (url, item_id) values (?, ?)", [str(image), int(item_id)])
        self.conn.commit()


def item_to_dict(item: list, images: list):
    return {
        "id": item[0],
        "name": item[1],
        "desc": item[2],
        "price": item[3],
        "stock": item[4],
        "sold": item[5],
        "thumbnail": images[0] if len(images) > 0 else "https://via.placeholder.com/240x240",
        "images": images if len(images) > 0 else []
    }




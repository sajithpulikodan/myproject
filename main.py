from sanic import Sanic
from sanic.response import json
import asyncpg

from config import DB_URL
import controllers.products.ratings as ratings
from libs.place_holder import Global

app = Sanic()


@app.listener('before_server_start')
async def before_start(app, uvloop):
    Global.db = await asyncpg.create_pool(DB_URL, loop=uvloop)

@app.listener('before_server_stop')
async def close_db(app, loop):
    print('Server shutdown')
    await Global.db.close()

app.add_route(ratings.get_ratings,
              "products/<product_id>/ratings", methods=['GET'])

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)
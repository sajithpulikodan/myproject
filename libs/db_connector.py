from libs.place_holder import Global
import libs.queries as queries

async def fetch_rating(product_id):
    """Fetch product ratings"""
    try:
        sum = 0
        count = 0
        average = 0
        con = await Global.db.acquire()
        ratings = dict(await con.fetch(queries.fetch_ratings, product_id))
        # only 5 items, so it will be in constant time
        for key, value in ratings.items():
            sum = sum + key * value
            count = count + value
        average = sum/count
       
    except Exception as e:
        pass
        #log the error message and return error
    finally:
        await Global.db.release(con)
    return ratings, average
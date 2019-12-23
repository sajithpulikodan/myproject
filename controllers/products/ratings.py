import sanic
from libs.db_connector import fetch_rating

#add decorator for authentication
async def get_ratings(request, product_id):
    ratings, average_rating = await fetch_rating(int(product_id))
    response_data = {
        'ratings' : ratings,
        'average_rating' : average_rating
    }
    return sanic.response.json(
            {'data': response_data}, status=200)
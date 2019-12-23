fetch_ratings = "select rating, count(rating) from ratings where product_id = $1 group by rating "

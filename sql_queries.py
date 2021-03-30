
def list_top_n_movies_by_gross_revenue(sql_sort, sql_limit):
    query = f"""
        SELECT 
        Title,
        Year,
        Distributor 'Production House',
        Budget,
        Worldwide_BOC GrossCollections,
        CAST( CAST(Worldwide_BOC AS UNSIGNED) + (Budget/-1) AS SIGNED) 'Profit/Loss'
        FROM
        Movie
        ORDER BY GrossCollections {sql_sort}
        LIMIT {sql_limit};"""
    return query


def billion_dollar_movies(sql_sort, sql_limit):
    query = f"""
        SELECT 
        Title,
        Year,
        Distributor 'Production House',
        Budget,
        Worldwide_BOC GrossCollections,
        (Worldwide_BOC - Budget) Profit
    FROM
        Movie
    WHERE
        Worldwide_BOC > 1000000000
    ORDER BY GrossCollections {sql_sort}
    LIMIT {sql_limit};"""
    return query


def list_of_movies_with_biggest_losses(sql_sort, sql_limit):
    query = f"""
        SELECT 
        Title 'Movie Title',
        Year,
        Distributor 'Production House',
        Budget,
        Worldwide_BOC AS 'Gross Collections',
        CAST( CAST(Worldwide_BOC AS UNSIGNED) + (Budget/-1) AS SIGNED) 'Profit/Loss'
        FROM
        Movie
        WHERE
        (Worldwide_BOC + (Budget / - 1)) < 0
        ORDER BY 5 {sql_sort}
        LIMIT {sql_limit};"""
    return query


def highest_rated_movies(sql_sort, sql_limit):
    query = f"""
        SELECT 
        Title,
        Year,
	    Distributor 'Production House',
        CAST( CAST(Worldwide_BOC AS UNSIGNED) + (Budget/-1) AS SIGNED) 'Profit/Loss',
        user_rating Ratings
        FROM
        Movie
        ORDER BY user_rating {sql_sort}
        LIMIT {sql_limit};"""
    return query


def actor_know_for(name, sql_sort, sql_limit):
    query = f"""
    SELECT DISTINCT
    M.title Movie, M.Year
    FROM
    movie M,
    Cast_Crew CC
    WHERE
    M.ID IN (SELECT 
            C.movie_id
        FROM
            Cast_Crew CC
                INNER JOIN
            CC_knownfor C ON cc.id = c.cast_crew_id
        WHERE
            cc.id = (SELECT 
                    ID
                FROM
                    Cast_crew
                WHERE
                    Name LIKE '%{name}%'))
   ORDER BY year {sql_sort}
    LIMIT {sql_limit};
    """
    return query


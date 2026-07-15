import pandera.pandas as pa

ratings_schema = pa.DataFrameSchema(
    {
        "userId": pa.Column(int),
        "movieId": pa.Column(int),
        "rating": pa.Column(float),
        "timestamp": pa.Column(int),
    },
    strict=True,
)

movies_schema = pa.DataFrameSchema(
    {
        "movieId": pa.Column(int),
        "title": pa.Column(str),
        "genres": pa.Column(str),
    },
    strict=True,
)
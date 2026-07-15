from pathlib import Path

import pandas as pd
from pandas import test

from src.common.file_utils import validate_file
from src.ingestion.split import temporal_split
from src.common.config import Config
from src.common.logger import logger
from src.common.exceptions import DataIngestionException
from src.validation.schema import (
    ratings_schema,
    movies_schema,
)



class DataIngestion:

    def __init__(self):

        self.cfg = Config().get()

        self.dataset_root = Path(self.cfg["dataset"]["root"])

    def load_csv(self, filename):

        path = self.dataset_root / filename

        if not path.exists():
            raise DataIngestionException(f"{path} not found.")

        logger.info(f"Loading {filename}")
        validate_file(path)

        return pd.read_csv(path)
    
    def save_processed_data(self, train, validation, test):

        processed = Path("data/processed")
        processed.mkdir(parents=True, exist_ok=True)

        train.to_parquet(
            processed / "train.parquet",
            index=False,
        )

        validation.to_parquet(
            processed / "validation.parquet",
            index=False,
        )

        test.to_parquet(
            processed / "test.parquet",
            index=False,
        )

        logger.info("Processed parquet files saved.")

    def run(self):

        ratings = self.load_csv(self.cfg["dataset"]["ratings"])
        movies = self.load_csv(self.cfg["dataset"]["movies"])

        ratings["timestamp"] = pd.to_datetime(ratings["timestamp"]).astype("int64") // 10**9
        ratings_schema.validate(ratings)
        movies_schema.validate(movies)

        logger.info("Schema validation successful")

        logger.info(f"Users : {ratings.userId.nunique()}")
        logger.info(f"Movies : {ratings.movieId.nunique()}")
        logger.info(f"Ratings : {len(ratings)}")
        logger.info(f"Average Rating : {ratings.rating.mean():.2f}")

        logger.info(ratings.isnull().sum())

        logger.info(movies.isnull().sum())

        logger.info(ratings.duplicated().sum())

        train, validation, test = temporal_split(ratings)

        self.save_processed_data(
            train,
            validation,
            test,
        )

        return train, validation, test, movies
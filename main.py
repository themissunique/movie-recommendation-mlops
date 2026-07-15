from src.ingestion.data_ingestion import DataIngestion


def main():

    ingestion = DataIngestion()

    # The *_ will catch any remaining returned values automatically
    ratings, movies, *_ = ingestion.run()

    print(ratings.head())

    print(movies.head())


if __name__ == "__main__":
    main()
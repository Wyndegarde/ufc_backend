import pandas as pd
from sqlalchemy import create_engine


def main():
    SQLALCHEMY_DATABASE_URL = "sqlite:///./ufc_db.db"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

    df = pd.read_csv("./data/next_event_truncated.csv")
    df.to_sql("next_event_truncated", con=engine, if_exists="replace")


if __name__ == "__main__":
    main()

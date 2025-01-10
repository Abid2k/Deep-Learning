import sqlalchemy as sa

engine = sa.create_engine('postgresql+psycopg2://username:password@localhost/dbname')
import sqlalchemy as sa

engine = sa.create_engine('postgresql+psycopg2://postgres:joeychandler.@localhost/SQLAlchemy')

connection = engine.connect()

metadata = sa.MetaData()

user_tabel = sa.Table(
    
    'abid',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('User Name', sa.String(255), nullable=False),
    sa.Column('email', sa.String(255), nullable=False),
    )

metadata.create_all(engine)

connection.close()
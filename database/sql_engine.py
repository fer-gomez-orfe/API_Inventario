from sqlmodel import SQLModel, Session, create_engine

# Create the SQLite database engine
URL_DATABASE = "mysql+pymysql://MonUser:MONUser1357$@192.168.0.196:3306/inventario"
engine = create_engine(URL_DATABASE)
SQLModel.metadata.create_all(engine)


# Dependency: Get the session
def get_session():
    with Session(engine) as session:
        yield session
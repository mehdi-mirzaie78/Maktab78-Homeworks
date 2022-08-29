import psycopg2
import psycopg2.extras
from core.models import DBModel
from configs import DB_CONNECTION
from psycopg2._psycopg import connection, cursor
from core.utils import logger

logger.name = 'DBManager'


class DBManager:
    # Database requirements
    HOST = DB_CONNECTION["HOST"]
    USER = DB_CONNECTION["USER"]
    PORT = DB_CONNECTION["PORT"]
    PASSWORD = DB_CONNECTION["PASSWORD"]
    DATABASE = DB_CONNECTION['DATABASE']

    def __init__(self, database=DATABASE, user=USER, host=HOST, port=PORT, password=PASSWORD) -> None:
        self.database = database
        self.user = user
        self.host = host
        self.port = port
        self.password = password

        self.conn: connection = \
            psycopg2.connect(dbname=self.database, user=self.user, host=self.host, port=self.port, password=password)

    def __del__(self):
        self.conn.close()  # Close the connection on delete

    def __get_cursor(self) -> cursor:
        # Changing the fetch output from Tuple to Dict utilizing RealDictCursor cursor factory
        return self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def create(self, model_instance: DBModel) -> int:
        """return id of created model instance from table"""

        with self.conn:
            assert isinstance(model_instance, DBModel)
            curs = self.__get_cursor()
            model_vars = vars(model_instance)
            models_fields_str = ",".join(model_vars.keys())

            model_values_str = ",".join(["%s"] * len(model_vars))
            models_values_tuple = tuple(model_vars.values())
            with curs:
                curs.execute(f"""INSERT INTO {model_instance.TABLE} ({models_fields_str}) 
                VALUES ({model_values_str}) RETURNING ID;""", models_values_tuple)

                id = int(curs.fetchone()['id'])
                setattr(model_instance, 'id', id)
                logger.info(f"Added {model_instance}")
                return id

    def read(self, model_class: type, pk) -> DBModel:
        """returns an instance of the Model with inserted values"""
        assert issubclass(model_class, DBModel)
        with self.conn:
            curs = self.__get_cursor()
            with curs:
                curs.execute(f"""SELECT * FROM {model_class.TABLE} WHERE {model_class.PK} = {pk};""")
                res = curs.fetchone()
                obj = model_class(**dict(res))
                logger.info(f"Fetched from {DBModel.__name__} {obj}")
                return obj

    def update(self, model_instance: DBModel) -> None:
        """update instance in db table by get all model_instance attrs"""

        assert isinstance(model_instance, DBModel)
        with self.conn:
            curs = self.__get_cursor()
            with curs:
                model_vars = vars(model_instance)
                model_pk_value = getattr(model_instance, model_instance.PK)
                model_set_values = [f"{field} = %s" for field in model_vars]
                model_values_tuple = tuple(model_vars.values())
                curs.execute(f"""UPDATE {model_instance.TABLE} SET {','.join(model_set_values)} 
                WHERE {model_instance.PK} = {model_pk_value};""", model_values_tuple)
                logger.info(f"Updated {model_instance}")

    def delete(self, model_instance: DBModel) -> None:
        """delete instance method"""
        assert isinstance(model_instance, DBModel)
        with self.conn:
            curs = self.__get_cursor()
            with curs:
                model_pk_value = getattr(model_instance, model_instance.PK)
                curs.execute(f"""DELETE FROM {model_instance.TABLE} WHERE {model_instance.PK} = {model_pk_value};""")
                delattr(model_instance, 'id')
                logger.info(f"Deleted {model_instance}")

db = DBManager()

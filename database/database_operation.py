import psycopg2


class Data:
    def __init__(self):
        print('Test')

    def create_tables(self):
        commands = (
            """
            CREATE TABLE IF NOT EXISTS Organizations (
                Index SERIAL PRIMARY KEY,
                Organization_id VARCHAR(255) NOT NULL,
                Name VARCHAR(255) NOT NULL,
                Website VARCHAR(255) NOT NULL,
                Country VARCHAR(255) NOT NULL,
                Description VARCHAR(255) NOT NULL,
                Founded INTEGER NOT NULL,
                Industry VARCHAR(255) NOT NULL,
                Number_of_employee INTEGER NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS vendors (
                vendor_id SERIAL PRIMARY KEY,
                vendor_name VARCHAR(255) NOT NULL
            )
            """,
            """ CREATE TABLE IF NOT EXISTS parts (
                    part_id SERIAL PRIMARY KEY,
                    part_name VARCHAR(255) NOT NULL
                    )
            """,
            """
            CREATE TABLE IF NOT EXISTS part_drawings (
                    part_id INTEGER PRIMARY KEY,
                    file_extension VARCHAR(5) NOT NULL,
                    drawing_data BYTEA NOT NULL,
                    FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS vendor_parts (
                    vendor_id INTEGER NOT NULL,
                    part_id INTEGER NOT NULL,
                    PRIMARY KEY (vendor_id, part_id),
                    FOREIGN KEY (vendor_id)
                        REFERENCES vendors (vendor_id)
                        ON UPDATE CASCADE ON DELETE CASCADE,
                    FOREIGN KEY (part_id)
                        REFERENCES parts (part_id)
                        ON UPDATE CASCADE ON DELETE CASCADE
            )
            """
            )

        conn = None

        try:
            # connect to the PostgreSQL server
            conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", port="5432",
                                    host="localhost")
            cur = conn.cursor()
            # create table one by one
            for command in commands:
                cur.execute(command)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


if __name__ == '__main__':
    Data().create_tables()




    #""" CREATE TABLE Organizations
     #   (Index SERIAL PRIMARY KEY,Organization_id VARCHAR(255) NOT NULL,
     #   Name VARCHAR(255) NOT NULL,Website VARCHAR(255) NOT NULL,Country VARCHAR(255) NOT NULL,Description VARCHAR(
    #    255) NOT NULL,Founded INTEGER NOT NULL,Industry VARCHAR(255) NOT NULL,Number_of_employee INTEGER NOT NULL) """

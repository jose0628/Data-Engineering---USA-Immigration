import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def execute_queries(cur, conn, query_list):
    """Drops tables
    :param cur (:obj:`psycopg2.extensions.cursor`): Cursor for connection
    :param con (:obj:`psycopg2.extensions.connection`): database connection
    :param query_list (list): list of queries to executed
    """
    for query in query_list:
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e:
            print("Error executing query: " + query)
            print(e)


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}" \
                            .format(*config['CLUSTER'].values()))

    cur = conn.cursor()
    execute_queries(cur, conn, drop_table_queries)
    execute_queries(cur, conn, create_table_queries)
    conn.close()


if __name__ == "__main__":
    main()

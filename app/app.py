from flask import Flask, request
import psycopg2
import os

app = Flask(__name__)

db_connection = psycopg2.connect(
    host=os.environ['DB_HOST'],
    dbname=os.environ['DB_NAME'],
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'])

cur = db_connection.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS params (name varchar(64) PRIMARY KEY, value varchar (150) NOT NULL);')

db_connection.commit()

def try_query(query):
    try:
        cur.execute(query)
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
        print(f'Query: {cur.query}')
        db_connection.rollback()
        return False
    else:
        db_connection.commit()
        return True


@app.route('/set', methods=['GET'])
def set_param():
    arg = next(iter(request.args))  # get only first argument
    cur.execute(f'SELECT value FROM params WHERE name LIKE \'{arg}\';')     # check if param already exists in db
    res = cur.fetchone()
    if res:
        if try_query(f'UPDATE params SET value=\'{request.args.get(arg)}\' WHERE name LIKE \'{arg}\';'):
            return '', 200
    else:
        if try_query(f'INSERT INTO params VALUES(\'{arg}\', \'{request.args.get(arg)}\');'):
            return '', 200
    return '', 400


@app.route('/get', methods=['GET'])
def get_param():
    arg = request.args.get('param')  # get param argument
    cur.execute(f'SELECT value FROM params WHERE name LIKE \'{arg}\';')
    res = cur.fetchone()
    if res:
        return res[0], 200
    else:
        return '', 404


@app.route('/delete', methods=['GET'])
def del_param():
    arg = request.args.get('param')  # get param argument
    if try_query(f'DELETE FROM params WHERE name LIKE \'{arg}\';'):
        return '', 200
    else:
        return '', 404


if __name__ == '__main__':
    app.run()

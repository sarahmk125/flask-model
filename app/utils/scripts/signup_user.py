import argparse
import psycopg2
import app.utils.secrets as secrets

from werkzeug.security import generate_password_hash


"""
Overview:   This is a script to signup a user. The signup page has been taken
            out of the app for security, so not just anyone could signup.
            The password is encrypted in this script before writing to the database.
"""


def signup_user(email, password):
    print(f'Attempting to signup user {email}...')

    # Hash the pass
    password = generate_password_hash(password, method='sha256')

    # Connect to the DB
    conn_string = f"host='{secrets.PROD_POSTGRES_HOST}' dbname='postgres' user='{secrets.PROD_POSTGRES_USER}' password='{secrets.PROD_POSTGRES_PASS}'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute(f"""
        insert into "user"
            select max_id + 1 as id, '{email}' as email, '{password}' as password, null as username
            from (select max(id) as max_id from "user") as a; """)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # Setup parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--email', required=True, dest='email', help='Email of the user')
    parser.add_argument('-p', '--password', required=True, dest='password', help='Password for the user')

    args = parser.parse_args()
    email = args.email
    password = args.password

    signup_user(email, password)

    

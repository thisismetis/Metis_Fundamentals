import sys
try:
    import psycopg2 as pg
except ImportError:
    print("You should install psycopg2 with the command")
    print("  conda install psycopg2")
    sys.exit(0)

ip_address = input("Please enter you aws ip address:")
ip_address = ip_address.strip()

connection_args = {
    'host': ip_address, # You'll have to update this to your IP
    'user': 'ubuntu',    # username
    'dbname': 'sites',   # DB that we are connecting to
    'port': 5432         # port we opened on AWS
}

connection = pg.connect(**connection_args)

# make a cursor
cursor = connection.cursor()

# make a query (sets the cursor pointing at the first record)
cursor.execute("SELECT * FROM locations;")

location_list = cursor.fetchall()

print(f"Found {len(location_list)} metis locations -- connection successful")

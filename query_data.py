import sqlite3
import pandas as pd

conn = sqlite3.connect("database.sqlite")

# Caminho do banco de dados
DB_PATH = "database.sqlite"


# SELECT
df_from_db = pd.read_sql("SELECT * FROM bus", conn)
print("BUS")
print(df_from_db)

df_from_db = pd.read_sql("SELECT * FROM line", conn)
print("LINE")
print(df_from_db)

df_from_db = pd.read_sql("SELECT * FROM driver", conn)
print("DRIVER")
print(df_from_db)

df_from_db = pd.read_sql("SELECT * FROM stop", conn)
print("STOPS")
print(df_from_db)

df_from_db = pd.read_sql("SELECT * FROM trip", conn)
print("TRIPS")
print(df_from_db)

df_from_db = pd.read_sql("SELECT * FROM tariff", conn)
print("TARIFF")
print(df_from_db)

df_from_db = pd.read_sql("SELECT * FROM line_stop", conn)
print("LINE_STOPS")
print(df_from_db)


#INNER JOIN - BUS AND LINE
print("INNER JOIN")
query_inner = """
SELECT bus.number AS bus_number, bus.license_plate, line.code AS line_code
FROM trip
INNER JOIN line ON trip.line_id = line.id
INNER JOIN bus ON trip.bus_id = bus.id;
"""
inner_join_df = pd.read_sql(query_inner, conn)
print(inner_join_df)

#INNER JOIN - LINE and LINE_STOPS
print("INNER JOIN")
query_inner = """
SELECT line.code AS line_code, stop.name
FROM line_stop
INNER JOIN line ON line_stop.line_id = line.id
INNER JOIN stop ON line_stop.stop_id = stop.id;
"""
inner_join_df = pd.read_sql(query_inner, conn)
print(inner_join_df)

#LEFT JOIN - BUS and LINE
print("LEFT JOIN")
query_left = """
SELECT  bus.number AS bus_number, line.code AS line_code
FROM bus
LEFT JOIN trip ON bus.id = trip.bus_id
LEFT JOIN line ON trip.line_id = line.id;
"""
left_join_df = pd.read_sql(query_left, conn)
print(left_join_df)


#LEFT JOIN - line and DRIVER
print("LEFT JOIN")
query_left = """
SELECT  line.code AS line_code, driver.name AS driver_name
FROM line
LEFT JOIN trip ON trip.line_id = line.id
LEFT JOIN driver ON trip.driver_id = driver.id;
"""
left_join_df = pd.read_sql(query_left, conn)
print(left_join_df)

#LEFT JOIN - line and stops
print("LEFT JOIN")
query_left = """
SELECT stop.name AS stop_name, line.code AS line_code
FROM stop
LEFT JOIN line_stop ON stop.id = line_stop.stop_id
LEFT JOIN line ON line_stop.line_id = line.id;
"""
left_join_df = pd.read_sql(query_left, conn)
print(left_join_df)

#INNER JOIN - BUS AND LINE WHERE COLOR = VERMELHO
print("INNER JOIN")
query_inner = """
SELECT line.code AS line_code, bus.number AS bus_number, bus.color
FROM trip
INNER JOIN line ON trip.line_id = line.id
INNER JOIN bus ON trip.bus_id = bus.id
WHERE bus.color = 'Vermelho';
"""
inner_join_df = pd.read_sql(query_inner, conn)
print(inner_join_df)

# Fechar conexão
conn.close()




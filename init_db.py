import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect("database.sqlite")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

# Criar tabela

cursor.execute("""
CREATE TABLE IF NOT EXISTS stop (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tariff (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cash FLOAT NOT NULL,
    card FLOAT NOT NULL,
    student FLOAT NOT NULL,
    elderly FLOAT NOT NULL,
    voucher FLOAT NOT NULL

)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS line (
    id INTEGER PRIMARY KEY AUTOINCREMENT,       
    first_stop_id INTEGER NOT NULL,
    last_stop_id INTEGER NOT NULL,
    code TEXT NOT NULL,
    name TEXT NULL,
    avg_travel_time_minutes INT NULL,
    status TEXT NOT NULL,
    frequency_minutes INT NULL,
    tariff_id INTEGER NOT NULL,
    FOREIGN KEY (first_stop_id) REFERENCES stop(id) ON DELETE CASCADE,
    FOREIGN KEY (last_stop_id) REFERENCES stop(id) ON DELETE CASCADE,
    FOREIGN KEY (tariff_id) REFERENCES tariff(id) ON DELETE CASCADE    
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS bus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER NULL,
    license_plate CHAR NULL,
    year_manufacture INTEGER NOT NULL,
    passenger_capacity INT NOT NULL,
    color TEXT NULL,
    status TEXT NOT NULL,
    model TEXT NOT NULL,
    acquisition_date DATE NOT NULL,
    accessibility BOOLEAN NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS driver (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    date_of_birth DATE NOT NULL,
    phone_number TEXT NOT NULL,
    email TEXT NOT NULL,
    license_number TEXT NOT NULL,
    license_category TEXT NOT NULL,
    license_expiry_date DATE NOT NULL,
    status TEXT NOT NULL,
    salary FLOAT NULL,
    shift TEXT NOT NULL, 
    street TEXT NOT NULL,
    house_number TEXT NOT NULL, 
    complement TEXT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL    
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS trip (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    driver_id INTEGER NOT NULL,
    line_id INTEGER NOT NULL,
    bus_id INTEGER NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (driver_id) REFERENCES driver(id) ON DELETE CASCADE,
    FOREIGN KEY (line_id) REFERENCES line(id) ON DELETE CASCADE,
    FOREIGN KEY (bus_id) REFERENCES bus(id) ON DELETE CASCADE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS line_stop (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    line_id INTEGER NOT NULL,
    stop_id INTEGER NOT NULL,
    sequence INTEGER NOT NULL,
    FOREIGN KEY (line_id) REFERENCES line(id) ON DELETE CASCADE,
    FOREIGN KEY (stop_id) REFERENCES stop(id) ON DELETE CASCADE
)
""")

# Salvar e fechar conexão
conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")

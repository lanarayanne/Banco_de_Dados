import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect("database.sqlite")

# Criar um DataFrame 
df_bus = pd.DataFrame({
    "number": [2309, 2320, 2239, 1227, 3279],
    "license_plate": ["FST2319", "FJN0630", "EZU5232", "CUC5473", "GAF4310"],
    "year_manufacture": [2014, 2014, 2013, 2009, 2015],
    "passenger_capacity": [37, 37, 34, 35, 30],
    "color": ["Vermelho", "Vermelho", "Vermelho", "Azul", "Amarelo"],
    "status": ["Ativo", "Ativo", "Ativo", "Ativo", "Ativo"],
    "model": ["M.BENZ/MPOLO TORINO U", "M.BENZ/MPOLO TORINO U", "M.-BENZ INDUSCAR APACHE U", "M.-BENZ MARCOPOLO SEN MIDI ON", "M.BENZ/MPOLO TORINO U" ] ,
    "acquisition_date": ["20/10/2014", "20/10/2014", "05/09/2013", "10/12/2009", "02/02/2016"],
    "accessibility": [1,1,0,0,1]
})

df_line = pd.DataFrame({
    #CHAVE ESTRANGEIRA
    #CHAVE ESTRANGEIRA
    "code" : [434, 731, 420, 275, 732],
    "name": ["Terminal São João / Centro (Via Cumbica)", "Terminal Pimentas/Pça da Saudade (via Cecap)", "Jd. Santa Paula / Centro (via Monteiro)", "Cocaia - Shopping Internacional", "Terminal Pimentas / Centro (via Jd. Angélica e Jd. Santo Afonso)"],
    "avg_travel_time_minutes": [193, 218, 231, 108, 210],
    "status": ["Ativo", "Ativo", "Ativo", "Ativo", "Ativo"],
    "frequency_minutes": [30, 30, 20, 15, 30],
    #CHAVE ESTRANGEIRA
})

df_driver = pd.DataFrame({
    "name": ["Alana Rayanne Araujo Freitas", "Vitor Matheus de Azevedo Martins","Daniela Alves de Araujo Freitas", "Renato Severino de Freitas", "Eduarda Rayanne Araujo Freitas"],
    "cpf": ["546.853.255-54", "514.326.987-65", "284.122.365-98", "147.554.987-99", "321.411.768-54", "741.214.233-64"],
    "date_of_birth": ["10/12/1999", "07/04/1998", "09/07/1978", "06/03/1974", "12/03/2004"],
    "phone_number": ["(81)982041282", "(82)999939067", "(11)971881243", "(11)974914015", "(11)950641214"],
    "email": ["alanafreitas@gmail.com", "vitormartins@gmail.com", "danielaaraujo@gmail.com", "renatofreitas@gmail.com", "eduardarayanne@gmail.com"],
    "license_number": ["28980275904", "42889148902", "17423172287", "66178403045", "7568293003"],
    "license_category": ["BD", "ABD", "BCD", "BCDE", "BD"],
    "license_expiry_date": ["22/04/2030", "03/05/2027", "14/09/2034", "06/07/2030", "21/08/2026"],
    "status": ["Ativo", "Ativo", "Ativo", "Ativo", "Ativo"],
    "salary": [2500.00, 2500.00, 2500.00, 2500.00, 2500.00  ],
    "shift": ["Manhã", "Manhã", "Tarde", "Noite", "Tarde"],
    "street": ["Rua Pomerode", "Rua Monte Claro", "Rua 12 de Abril", "Rua Antonieta", "Rua da Paz" ],
    "house_number": [154, 21, 71, 411, 140],
    "complement": [None, None, "apto 81 t2", None, "apto 602 bloco b"],
    "city": ["Guarulhos", "Arapiraca", "Guarulhos", "Guarulhos", "Recife"],
    "state": ["SP", "AL", "SP", "SP", "PE"],
    "zip_code": ["07273150", "57843020", "07012055", "50752535"]
})

df_stop = pd.DataFrame({
    "name": ["Terminal São João", "Rua Jardim Alegre", "Terminal Pimentas", "Praça da Saudade", "Rua Manuel Antonio Major", "Rua Nossa Senhora Mãe dos Homens", "Av. Brigadeiro Faria Lima", "Rua Camilo Olivetti", "Av. Monteiro Lobato nº339"],
    "location": ["-23458333, -46.537500", "-23.4625, -46.5333", 
                 "-23.4775, -46.5122", "-23.4536917, -46.5407659",
                 "-23.4058324, -46.4212578", "-23.4620709 -46.5383149",
                 "-23.4396783 -46.5225094", "-23.4877750 -46.5473650",
                 "-23.4620709 -46.5383149"]

})

df_trip = pd.DataFrame({
    #FOREIGN KEY (driver_id) REFERENCES driver(id) ON DELETE CASCADE,
    #FOREIGN KEY (line_id) REFERENCES line(id) ON DELETE CASCADE,
    #FOREIGN KEY (bus_id) REFERENCES bus(id) ON DELETE CASCADE,
    "start_time": ["07:00", "08:00", "15:00", "20:00", "05:00"],
    "end_time": ["10:30", "11:13", "18:51", "23:38", "08:51"],
    "status": ["Ativo", "Ativo", "Ativo", "Ativo", "Ativo"]

})

df_tariff = pd.DataFrame({
    "cash": [4.00, 5.30, 4.30, 5.00, 4.00]
    "card": [4.00, 4.45, 4.30, 5.00, 3.49]
    "student":  [2,00, 2,55, 2,15, 2,50, 0,00]
    "elderly": [2,00
2,55
2,15
2,50
2,00]
    "voucher": [4,00
6,20
4,30
5,49
4,00]
})



cursor.execute("""
CREATE TABLE IF NOT EXISTS tariff (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    

)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS line_stop (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY (line_id) REFERENCES line(id) ON DELETE CASCADE,
    FOREIGN KEY (stop_id) REFERENCES stop(id) ON DELETE CASCADE,
    sequence INTEGER NOT NULL
)
""")




# Inserir o DataFrame na tabela SQLite
df_bus.to_sql("bus", conn, if_exists="append", index=False)

# Consultar os dados de volta usando pandas
df_from_db = pd.read_sql("SELECT * FROM bus", conn)
print("\nDados no banco:")
print(df_from_db)

# Fechar conexão
conn.close()

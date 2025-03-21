import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect("database.sqlite")

# Criar DataFrame 

df_stop = pd.DataFrame({
    "name": ["Terminal São João", "Rua Jardim Alegre", "Terminal Pimentas", "Praça da Saudade", "Rua Manuel Antonio Major", "Rua Nossa Senhora Mãe dos Homens", "Av. Brigadeiro Faria Lima", "Rua Camilo Olivetti", "Av. Monteiro Lobato nº339"],
    "location": ["-23458333, -46.537500", 
                 "-23.4625, -46.5333", 
                 "-23.4775, -46.5122", 
                 "-23.4536917, -46.5407659",
                 "-23.4058324, -46.4212578", 
                 "-23.4620709 -46.538314",
                 "-23.4396783 -46.5225094", 
                 "-23.4877750 -46.5473650",
                 "-23.4620709 -46.538314"]

})

df_tariff = pd.DataFrame({
    "cash": [4.00, 5.30, 4.30, 5.00, 4.00],
    "card": [4.00, 4.45, 4.30, 5.00, 3.49],
    "student": [2.00, 2.55, 2.15, 2.50, 0.00],
    "elderly": [2.00, 2.55, 2.15, 2.50, 2.00],
    "voucher": [4.00, 6.20, 4.30, 5.49, 4.00]
})

df_line = pd.DataFrame({
    "first_stop_id": [1, 3, 5, 7, 3],
    "last_stop_id": [2, 4, 6, 8, 9],
    "code" : [434, 731, 420, 275, 732],
    "name": ["Terminal São João / Centro (Via Cumbica)", "Terminal Pimentas/Pça da Saudade (via Cecap)", "Jd. Santa Paula / Centro (via Monteiro)", "Cocaia - Shopping Internacional", "Terminal Pimentas / Centro (via Jd. Angélica e Jd. Santo Afonso)"],
    "avg_travel_time_minutes": [193, 218, 231, 108, 210],
    "status": ["Ativo", "Ativo", "Ativo", "Ativo", "Ativo"],
    "frequency_minutes": [30, 30, 20, 15, 30],
    "tariff_id": [3,3,3,3,3]
})

df_bus = pd.DataFrame({
    "number": [2309, 2320, 2239, 1227, 3279],
    "license_plate": ["FST2319", "FJN0630", "EZU5232", "CUC5473", "GAF4310"],
    "year_manufacture": [2014, 2014, 2013, 2009, 2015],
    "passenger_capacity": [37, 37, 34, 35, 30],
    "color": ["Vermelho", "Vermelho", "Vermelho", "Azul", "Amarelo"],
    "status": ["Ativo", "Ativo", "Ativo", "Ativo", "Ativo"],
    "model": ["M.BENZ/MPOLO TORINO U", "M.BENZ/MPOLO TORINO U", "M.-BENZ INDUSCAR APACHE U", "M.-BENZ MARCOPOLO SEN MIDI ON", "M.BENZ/MPOLO TORINO U" ] ,
    "acquisition_date": ["20-10-2014", "20-10-2014", "05-09-2013", "10-12-2009", "02-02-2016"],
    "accessibility": [1,1,0,0,1]
})

df_driver = pd.DataFrame({
    "name": ["Alana", "Vitor", "Daniela", "Renato", "Eduarda"],
    "cpf": ["546.853.255-54", "514.326.987-65", "284.122.365-98", "147.554.987-99", "321.411.768-54"],
    "date_of_birth": ["11-09-1999", "06-02-1998", "07-08-1978", "06-11-1974", "30-10-2004"],
    "phone_number": ["(81)982054582", "(82)998929077", "(11)977831243", "(11)974317015", "(11)957641234"],
    "email": ["alana@gmail.com", "vitor@gmail.com", "daniela@gmail.com", "renato@gmail.com", "eduarda@gmail.com"],
    "license_number": ["28980275904", "42889148902", "17423172287", "66178403045", "7568293003"],
    "license_category": ["BD", "ABD", "BCD", "BCDE", "BD"],
    "license_expiry_date": ["22/04/2030", "03/05/2027", "14/09/2034", "06/07/2030", "21/08/2026"],
    "status": ["Ativo", "Ativo", "Ativo", "Ativo", "Ativo"],
    "salary": [2500.00, 2500.00, 2500.00, 2500.00, 2500.00  ],
    "shift": ["Manhã", "Manhã", "Tarde", "Noite", "Tarde"],
    "street": ["Rua Pomerode", "Rua Monte Claro", "Rua 12 de Abril", "Rua Antonieta", "Rua da Paz" ],
    "house_number": [154, 21, 71, 411, 140],
    "complement": [None, None, "apto 81", None, "apto 6"],
    "city": ["Guarulhos", "Arapiraca", "Guarulhos", "Guarulhos", "Recife"],
    "state": ["SP", "AL", "SP", "SP", "PE"],
    "zip_code": ["07273150", "57843020", "07012055", "07525535", "50757535"]
})

df_trip = pd.DataFrame({
    "driver_id": [1, 2, 3, 4, 5],
    "line_id": [5, 1, 4, 2, 3],
    "bus_id": [5, 1, 4, 5, 3],
    "start_time": ["07:00", "08:00", "15:00", "20:00", "05:00"],
    "end_time": ["10:30", "11:13", "18:51", "23:38", "08:51"],
    "status": ["Ativo", "Ativo", "Ativo", "Ativo", "Ativo"]

})

df_line_stop = pd.DataFrame({
    "line_id": [1, 1, 1, 1, 1],
    "stop_id": [1, 9, 6, 2, 9],
    "sequence": [1, 9, 16, 18, 30]
})

# Inserir o DataFrame na tabela SQLite
df_bus.to_sql("bus", conn, if_exists="append", index=False)
df_line.to_sql("line", conn, if_exists="append", index=False)
df_driver.to_sql("driver", conn, if_exists="append", index=False)
df_stop.to_sql("stop", conn, if_exists="append", index=False)
df_trip.to_sql("trip", conn, if_exists="append", index=False)
df_tariff.to_sql("tariff", conn, if_exists="append", index=False)
df_line_stop.to_sql("line_stop", conn, if_exists="append", index=False)


# Fechar conexão
conn.close()

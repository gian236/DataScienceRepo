import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 100k clientes, 12 observaciones, y el csv
clients = 100000
months = 12
csv = "credit_score_data.csv"

# generar los IDs de clients
clients_ids = np.arange(1, clients + 1)

# generar fechas de observación
start_date = datetime(2024, 1, 1)
observation_dates = [start_date + timedelta(days=30*i) for i in range(months)]

# generación de datos usando np.random
records = []
for client_id in clients_ids:
    for date in observation_dates:
        credit_utilization = round(np.random.uniform(0, 1), 2)  # porcentaje del crédito disponible que ha utilizado el cliente
        payment_history = np.random.choice([0, 1], p=[0.1, 0.9])  # si históricamente ha hecho pagos a tiempo o tardíos, 1 = Pago a tiempo, 0 = Pago tardío
        num_accounts = np.random.randint(1, 10)  # cantidad de cuentas activas
        inquiries_last_6m = np.random.randint(0, 5)  # consultas de crédito en los últimos 6 meses
        annual_income = np.random.randint(20000, 150000)  # ingreso anual en USD
        
        records.append([
            client_id,
            date.strftime('%Y-%m-%d'),
            credit_utilization,
            payment_history,
            num_accounts,
            inquiries_last_6m,
            annual_income
        ])

# crear DataFrame
df = pd.DataFrame(records, columns=[
    "client_id", "observation_date", "credit_utilization", "payment_history", 
    "num_accounts", "inquiries_last_6m", "annual_income"
])

# guardar en CSV
df.to_csv(csv, index=False)

print(f"Archivo CSV generado: {csv}")

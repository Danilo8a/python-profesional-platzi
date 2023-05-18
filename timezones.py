from datetime import datetime
import pytz


bogota_timezone = pytz.timezone("America/Bogota")
caracas_timezone = pytz.timezone("America/Caracas")

bogota_date = datetime.now(bogota_timezone)
caracas_date = datetime.now(caracas_timezone)

print(f"Hora Bogotá: {bogota_date.time()}\nHora Caracas: {caracas_date.time()}")

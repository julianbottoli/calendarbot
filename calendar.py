import requests
import discord
import schedule
import time

# Tu token de Discord
TOKEN = "MTA3NDQyMjA5ODczMjI2NTUzMw.G-1zLd.k5UhJ0flA61ZvXxAIoKhX43GCI6fXNJxIcWiIU"

# ID del canal de Discord al que deseas enviar los mensajes
CHANNEL_ID = "950210195353665609"

# URL de la API de Forex Factory
FOREX_FACTORY_API = "https://api.forexfactory.com/calendar.php?start=2022-12-31&end=2023-12-31&timezone=America/New_York"

# Inicializa el cliente de Discord
client = discord.Client()

# Función que envía los eventos económicos a Discord
def send_forex_events():
    # Obtiene los eventos económicos desde la API de Forex Factory
    response = requests.get(FOREX_FACTORY_API)
    events = response.json()['events']

    # Filtra los eventos económicos de hoy
    today = time.strftime("%Y-%m-%d")
    today_events = [event for event in events if event['date'].startswith(today)]

    # Si hay eventos económicos de hoy, envía un mensaje por evento a Discord
    if today_events:
        for event in today_events:
            message = f"{event['currency']}: {event['event']} ({event['impact']})\n"
            channel = client.get_channel(CHANNEL_ID)
            await channel.send(message)

# Programa la función para que se ejecute todos los días a las 9:00 AM
schedule.every().day.at("9:00").do(send_forex_events)

@client.event
async def on_ready():
    print(f"{client.user} ha iniciado sesión")

# Inicia el bot de Discord
client.run(TOKEN)

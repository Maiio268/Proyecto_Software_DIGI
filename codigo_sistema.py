import logging
import sqlite3
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from tabulate import tabulate

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Connect to the database
conn = sqlite3.connect("horarios.db", check_same_thread=False)
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS horarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    dia TEXT,
    hora_inicio TEXT,
    hora_fin TEXT,
    materia TEXT,
    aula TEXT
)''')
conn.commit()

# Allowed class hours with break
HORAS_CLASES = ["08:00", "09:00", "10:00", "11:30", "12:30", "13:30"]

# Function to start the bot
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "¡Bienvenido al bot de horarios escolares! 📅\n"
        "Comandos disponibles:\n"
        "✅ /agregar_horario - Añadir un horario manualmente.\n"
        "✅ /ver_horarios - Ver el horario semanal en tabla.\n"
        "🗑 /eliminar_horarios - Eliminar todos los horarios guardados."
    )

# Function to start the process of adding a schedule
async def agregar_horario(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Vamos a agregar un horario. Introduce el día (Lunes - Viernes):")
    context.user_data["estado"] = "esperando_dia"

# Handle user messages
async def manejar_mensaje(update: Update, context: CallbackContext) -> None:
    usuario_id = update.message.from_user.id
    texto = update.message.text

    if "estado" not in context.user_data:
        return

    estado = context.user_data["estado"]
    
    if estado == "esperando_dia":
        context.user_data["dia"] = texto
        context.user_data["materias"] = []
        context.user_data["estado"] = "esperando_materia"
        await update.message.reply_text("Introduce la materia:")
    
    elif estado == "esperando_materia":
        context.user_data["materia"] = texto
        await update.message.reply_text("Introduce el aula:")
        context.user_data["estado"] = "esperando_aula"
    
    elif estado == "esperando_aula":
        aula = texto
        dia = context.user_data["dia"]
        materia = context.user_data["materia"]
        idx = len(context.user_data["materias"])
        hora_inicio = HORAS_CLASES[idx]
        hora_fin = f"{int(hora_inicio[:2]) + 1}:00"
        context.user_data["materias"].append((materia, aula, hora_inicio, hora_fin))
        
        # Save in the database
        conn = sqlite3.connect("horarios.db")
        c = conn.cursor()
        c.execute("INSERT INTO horarios (usuario_id, dia, hora_inicio, hora_fin, materia, aula) VALUES (?, ?, ?, ?, ?, ?)",
                  (usuario_id, dia, hora_inicio, hora_fin, materia, aula))
        conn.commit()
        conn.close()

        if len(context.user_data["materias"]) < 6:
            await update.message.reply_text("✅ Materia guardada. Introduce otra materia:")
            context.user_data["estado"] = "esperando_materia"
        else:
            await update.message.reply_text("✅ Día completo. Si deseas agregar otro día usa /agregar_horario.")
            context.user_data.clear()

# Function to view saved schedules
async def ver_horarios(update: Update, context: CallbackContext) -> None:
    usuario_id = update.message.from_user.id
    conn = sqlite3.connect("horarios.db")
    c = conn.cursor()
    c.execute("SELECT dia, hora_inicio, hora_fin, materia, aula FROM horarios WHERE usuario_id = ? ORDER BY CASE dia WHEN 'Lunes' THEN 1 WHEN 'Martes' THEN 2 WHEN 'Miércoles' THEN 3 WHEN 'Jueves' THEN 4 WHEN 'Viernes' THEN 5 END, hora_inicio", (usuario_id,))
    horarios = c.fetchall()
    conn.close()

    if not horarios:
        await update.message.reply_text("No tienes horarios guardados.")
        return

    tabla = tabulate(horarios, headers=["Día", "Inicio", "Fin", "Materia", "Aula"], tablefmt="grid")
    mensaje = f"📅 Horario semanal:\n```{tabla}```"
    await update.message.reply_text(mensaje, parse_mode="MarkdownV2")

# Function to delete all schedules
async def eliminar_horarios(update: Update, context: CallbackContext) -> None:
    usuario_id = update.message.from_user.id
    conn = sqlite3.connect("horarios.db")
    c = conn.cursor()
    c.execute("DELETE FROM horarios WHERE usuario_id = ?", (usuario_id,))
    conn.commit()
    conn.close()
    await update.message.reply_text("🗑 Todos tus horarios han sido eliminados correctamente.")

# Bot configuration
def main():
    application = Application.builder().token("8080929287:AAHMjVw55BZgf5m_Uzw8AY50ZtQHjawX1Uo").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("agregar_horario", agregar_horario))
    application.add_handler(CommandHandler("ver_horarios", ver_horarios))
    application.add_handler(CommandHandler("eliminar_horarios", eliminar_horarios))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))

    application.run_polling()

if __name__ == '__main__':
    main()

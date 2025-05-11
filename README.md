# Project Description
🤖📱 The project consists of the creation of a software that creates and modifies weekly school schedules without conflicts. This is developed with a Python file that includes all the necessary code and, regarding user interaction, a Telegram bot has been created through which the user can create and delete these schedules.

# Proyect Motivation
📚📅 Creating school schedules can be a difficult task, especially when trying to avoid conflicts between subjects, teachers, and classrooms. This project was born to simplify and automate that process. With a user-friendly Telegram bot interface, anyone can easily create, view, and delete weekly schedules without needing technical knowledge. The system ensures there are no time conflicts and respects break times, providing a smart and accessible way to manage school timetables.

# ¿What does the code do?
🔧⚙️ The Python code in the file codigo_sistema.py does the following:
It allows users to manage schedules easily. Users can add, view, and delete schedules through Telegram commands. The bot stores the information in a SQLite database and organizes the subjects while respecting class times and a break.
The available commands in the code are:
- **/start:** Displays a welcome message with the available commands.
- **/agregar_horario:** Allows the user to enter days, subjects, and classrooms.
- **/ver_horarios:** Displays the schedule created by the user in table format.
- **/eliminar_horarios:** Deletes all schedules created by the user.

# Deployment on Different Platforms
## PC 💻
1) **Clone the repository:**

```
git clone <URL_DEL_REPOSITORIO>
cd Proyecto_Software_DIGI
```
2) **Install dependencies:**

```
pip install -r requirements.txt
```

3) **Run the bot:**
To run the bot, open the terminal and type the following command:
```
python codigo_sistema.py
```
IMPORTANT: Make sure you are in the project folder.

4) **Now log in to your Telegram account and type the bot's name in the search bar (located at the top of the Telegram app screen): SmartHorarioBot.**

5) **Now you can interact with the bot using the available commands.**

## Mobile Phone 📱
To use the Telegram bot on your mobile phone, you must **start the bot on your computer first** (follow the steps explained before in the deployment on PC).
Once the bot is running:
1) Open the Telegram app on your mobile device. 
2) Search for the bot by its name: SmartHorarioBot.
3) Start a conversation and use the available commands.

# License
🌐💬 The project is licensed under the [MIT License](./LICENSE). You are free to use, modify, and distribute the code for both commercial and non-commercial purposes.

# Contributing
🛠️🤝 If you are eager to contribute to the project or have any ideas to help with its development, [Check out the CONTRIBUTING file](./CONTRIBUTING.md) and feel free to add any suggestions or improvements you think might be useful. We welcome new ideas, bug fixes, feature additions, and anything else that can help make the project better.



GitHub Page


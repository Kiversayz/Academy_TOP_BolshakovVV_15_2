import pyodbc
from dotenv import load_dotenv
import os

# Проверка доступных драйверов
print(pyodbc.drivers())

# Загрузка переменных окружения
load_dotenv()
LOGIN = os.getenv("LOGIN")
PASS = os.getenv("PASS")
SERVER = os.getenv("SERVER")
# Параметры подключения
server = SERVER  # Имя сервера SQL Server Express
driver = "ODBC Driver 17 for SQL Server" #Название необходимого драйвера
username = LOGIN
password = PASS

def execute_query(query, db_name=None, autocommit=False):
    try:
        if db_name:
            conn_str = (
                f"DRIVER={{{driver}}};"
                f"SERVER={server};"
                f"DATABASE={db_name};"
                f"UID={username};"
                f"PWD={password}"
            )
        else:
            conn_str = (
                f"DRIVER={{{driver}}};"
                f"SERVER={server};"
                f"DATABASE=master;"
                f"UID={username};"
                f"PWD={password}"
            )
        
        with pyodbc.connect(conn_str, autocommit=autocommit) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            
            if "SELECT" in query:
                rows = cursor.fetchall()
                columns = [column[0] for column in cursor.description]
                return [dict(zip(columns, row)) for row in rows]
            
            cursor.close()
    
    except pyodbc.Error as e:
        print(f"Ошибка: {e}")

# 1. Создание БД (автокоммит включен)
execute_query("CREATE DATABASE QA_Tracker;", db_name="master", autocommit=True)

# 2. Проверка создания БД
result = execute_query("SELECT name FROM sys.databases WHERE name = 'QA_Tracker';", db_name="master")
if result:
    print("БД создана успешно")
else:
    print("Ошибка: БД не создана")
    exit()

# 3. Назначение пользователя в новой БД
execute_query(
    f"""
    USE QA_Tracker;
    CREATE USER {LOGIN} FOR LOGIN {LOGIN};
    EXEC sp_addrolemember 'db_owner', '{LOGIN}';
    """,
    db_name="QA_Tracker"
)

# 4. Создание таблицы
create_table_query = """
CREATE TABLE Bugs (
    BugID INT PRIMARY KEY,
    Title NVARCHAR(100),
    Description NVARCHAR(500),
    Severity NVARCHAR(50),
    Status NVARCHAR(50),
    AssignedTo NVARCHAR(100),
    CreatedDate DATE
);
"""
execute_query(create_table_query, db_name="QA_Tracker")

# 5. Вставка данных
insert_data_query = """
INSERT INTO Bugs (BugID, Title, Description, Severity, Status, AssignedTo, CreatedDate)
VALUES
(1, 'Ошибка авторизации', 'Пользователь не может войти после обновления', 'High', 'Open', 'Иван Петров', '2024-03-10'),
(2, 'Страница не загружается', 'Главная страница зависает при загрузке', 'Critical', 'In Progress', 'Мария Иванова', '2024-03-11');
"""
execute_query(insert_data_query, db_name="QA_Tracker")

# 6. Выборка данных
result = execute_query("SELECT * FROM Bugs;", db_name="QA_Tracker")

if result:
    print("Список открытых багов:")
    for bug in result:
        print(f"ID: {bug['BugID']}")
        print(f"Заголовок: {bug['Title']}")
        print(f"Описание: {bug['Description']}")
        print(f"Сeverity: {bug['Severity']}")
        print(f"Статус: {bug['Status']}")
        print(f"Ответственный: {bug['AssignedTo']}")
        print(f"Дата создания: {bug['CreatedDate']}")
        print("------------------------------")
else:
    print("Нет данных")
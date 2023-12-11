import pymysql
from cofigure import host, user, password, db_name


#Создаём таблицы
while True:
    print('Cписок команд: ' '\n' '1.Создать таблицы в mySQL' '\n'  '2.Добавить номер аудитории и сохранить файл' '\n' '3.Добавить информацию о стульях' '\n' '4.Добавить информацию о столах' '\n' '5.Добавить информацию о моноблоках' '\n' '6.Вывести данные из таблицы''\n' '7.Удалить данные о стульях из таблицы''\n' '8.Удалить данные о столах из таблицы''\n' '9.Удалить данные о моноблоках из таблицы''\n' '10.Выйти из консоли')
    command = input('Введите команду: ')
    if (command == '1'):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Подключение установлено")

            with connection.cursor() as cursor:
                cursor.execute( 'CREATE TABLE IF NOT EXISTS chairs (count_chairs INT, company_name_chairs TEXT, year_chairs INT)')
                cursor.execute( 'CREATE TABLE IF NOT EXISTS tables (count_tables INT, company_name_tables TEXT, year_tables INT)')
                cursor.execute( 'CREATE TABLE IF NOT EXISTS monoblocks (count_monoblocks INT, company_name_monoblocks TEXT, year_monoblocks INT, OZY INT, mark TEXT, HDD INT)')
                connection.commit()
                print('Таблицы созданы')
        finally:
            connection.close()
    # Создаём файл
    if (command == '2'):
        num = input('Введите номер аудитории: ')
        new_file = open("C:/Users/215525/Desktop/" + num + ".txt", "a+")
        new_file.close()
        print('Файл создан')

    # Добавляем данные о стульях
    if (command == '3'):
        count_chairs = input('count_chairs: ')
        company_name_chairs = input('company_name_chairs: ')
        year_chairs = input('year_chairs: ')
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )

            with connection.cursor() as cursor:
                cursor.execute('''INSERT INTO chairs(count_chairs,company_name_chairs, year_chairs) VALUES (%s, %s, %s) ''', (count_chairs,company_name_chairs, year_chairs))
                connection.commit()
                print('Информация о стульях добавлена')

        finally:
            connection.close()

    # Добавляем данные о столах
    if (command == '4'):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Подключение установлено")
            count_tables = input('count_tables: ')
            company_name_tables = input('company_name_tables: ')
            year_tables = input('year_tables: ')
            with connection.cursor() as cursor:
                cursor.execute('''INSERT INTO tables(count_tables,company_name_tables, year_tables) VALUES (%s, %s, %s) ''', (count_tables,company_name_tables, year_tables))
                connection.commit()
                print('Информация о столах добавлена')
        finally:
            connection.close()

    # Добавляем данные о моноблоках
    if (command == '5'):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Подключение установлено")
            count_monoblocks = input('count_monoblocks: ')
            company_name_monoblocks = input('company_name_monoblocks: ')
            year_monoblocks = input('year_monoblocks: ')
            OZY = input('OZY: ')
            mark = input ('mark: ')
            HDD = input ('HDD: ')
            with connection.cursor() as cursor:
                cursor.execute('''INSERT INTO monoblocks(count_monoblocks,company_name_monoblocks, year_monoblocks, OZY, mark, HDD) VALUES (%s, %s, %s, %s, %s, %s) ''', (count_monoblocks, company_name_monoblocks, year_monoblocks, OZY, mark, HDD))
                connection.commit()
                print('Информация о моноблоках добавлена')

        finally:
            connection.close()

    # Выводим все таблицы
    if (command == '6'):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )

            select_movies_query = "SELECT * FROM chairs "
            with connection.cursor() as cursor:
                cursor.execute(select_movies_query)
                result = cursor.fetchall()
                for row in result:
                    print(row)


            select_movies_query = "SELECT * FROM tables "
            with connection.cursor() as cursor:
                cursor.execute(select_movies_query)
                result = cursor.fetchall()
                for row in result:
                    print(row)

            select_movies_query = "SELECT * FROM monoblocks "
            with connection.cursor() as cursor:
                cursor.execute(select_movies_query)
                result = cursor.fetchall()
                for row in result:
                    print(row)

        finally:
            connection.close()

    # Удаляем таблицу о стульях
    if (command == '7'):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )

            with connection.cursor() as cursor:
                cursor.execute("TRUNCATE TABLE chairs")
                print('Taблица о стульях удалена')
        finally:
            connection.close()

    # Удаляем таблицу о столах
    if (command == '8'):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )

            with connection.cursor() as cursor:
                cursor.execute("TRUNCATE TABLE tables")
                print('Таблица о столах удалена')
        finally:
            connection.close()
    # Удаляем таблицу о моноблоках
    if (command == '9'):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )

            with connection.cursor() as cursor:
                cursor.execute("TRUNCATE TABLE monoblocks")
                print('Taблица о моноблоках удалена')
        finally:
            connection.close()

    if (command == '10'):
        break



host = 'localhost'
user = 'root'
password = 'vpstudent'
db_name = 'TEST'

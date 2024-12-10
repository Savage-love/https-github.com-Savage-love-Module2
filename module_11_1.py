import pandas as pd

try:
    # Загрузка данных из CSV-файла
    df = pd.read_csv('data.csv')

    # Простой анализ данных
    print("Первые 5 строк:\n", df.head())
    print("\nОписание данных:\n", df.describe())
    print("\nКоличество пропущенных значений:\n", df.isnull().sum())

    #Пример анализа -  находим среднее значение числового столбца (при условии, что есть числовой столбец)
    numeric_cols = df.select_dtypes(include=['number'])
    if not numeric_cols.empty:
        print("\nСредние значения числовых столбцов:\n", numeric_cols.mean())


    #Пример группировки данных по какому-либо столбцу (если такой столбец есть)
    categorical_cols = df.select_dtypes(include=['object', 'category'])
    if not categorical_cols.empty:
        first_cat_col = categorical_cols.columns[0]  #берем первый категориальный столбец
        print(f"\nГруппировка по столбцу '{first_cat_col}':\n", df.groupby(first_cat_col).size())


except FileNotFoundError:
    print("Файл data.csv не найден.")
except pd.errors.EmptyDataError:
    print("Файл data.csv пустой.")
except pd.errors.ParserError:
    print("Ошибка при разборе файла data.csv. Проверьте формат файла.")
except Exception as exs:
    print(f"Произошла ошибка: {exs}")
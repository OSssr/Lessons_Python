# ============================================================
# Умный регистратор (версия для терминала)
# ============================================================

print("=" * 45)
print("          УМНЫЙ РЕГИСТРАТОР")
print("=" * 45)
print()

# --- Получаем данные ---
name = input("Введите имя: ").strip()
surname = input("Введите фамилию: ").strip()
age_str = input("Введите возраст: ").strip()
city = input("Введите город: ").strip()

print()

# --- Проверка на пустые поля ---
if not name or not surname or not age_str or not city:
    print("Ошибка! Все поля должны быть заполнены.")
else:
    # --- Проверка, что возраст — число ---
    if not age_str.isdigit():
        print("Ошибка! Возраст должен быть числом.")
    else:
        age = int(age_str)

        # --- Обработка строк ---
        name = name.capitalize()
        surname = surname.capitalize()
        city = city.capitalize()

        # --- Определение статуса ---
        if age < 14:
            status = "Слишком молод для регистрации"
            access = False
        elif age < 18:
            status = "Регистрация с ограничениями"
            access = True
        else:
            status = "Полный доступ"
            access = True

        # --- Генерация логина ---
        login = name[0].lower() + "." + surname.lower() + str(age)

        # --- Дополнительная информация ---
        name_reversed = name[::-1]
        name_length = len(name)
        has_a = "а" in name.lower() or "a" in name.lower()

        # --- Вывод результата ---
        print("-" * 45)
        print("           ПРОФИЛЬ СОЗДАН")
        print("-" * 45)
        print(f"Имя:            {name}")
        print(f"Фамилия:        {surname}")
        print(f"Возраст:        {age}")
        print(f"Город:          {city}")
        print(f"Статус:         {status}")
        print(f"Логин:          {login}")
        print("-" * 45)
        print(f"Имя наоборот:   {name_reversed}")
        print(f"Букв в имени:   {name_length}")

        if has_a:
            print("В имени есть буква «а»")
        else:
            print("В имени нет буквы «а»")

        print("-" * 45)

        if access:
            print(f"\nДобро пожаловать, {name} {surname}!")
        else:
            print("\nК сожалению, регистрация невозможна.")
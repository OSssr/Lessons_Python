# ============================================================
# Умный регистратор — версия с графическим интерфейсом (tkinter)
# ============================================================

import tkinter as tk
from tkinter import messagebox

def register():
    # Получаем данные из полей ввода
    name = entry_name.get().strip()
    surname = entry_surname.get().strip()
    age_str = entry_age.get().strip()
    city = entry_city.get().strip()

    # Проверка на пустые поля
    if not name or not surname or not age_str or not city:
        messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
        return

    # Проверка, что возраст — число
    if not age_str.isdigit():
        messagebox.showerror("Ошибка", "Возраст должен быть числом!")
        return

    age = int(age_str)

    # Обработка строк
    name = name.capitalize()
    surname = surname.capitalize()
    city = city.capitalize()

    # Определение статуса
    if age < 14:
        status = "Слишком молод для регистрации"
        access = False
    elif age < 18:
        status = "Регистрация с ограничениями"
        access = True
    else:
        status = "Полный доступ"
        access = True

    # Генерация логина
    login = name[0].lower() + "." + surname.lower() + str(age)

    # Дополнительная информация
    name_reversed = name[::-1]
    name_length = len(name)
    has_a = "а" in name.lower() or "a" in name.lower()

    # Формируем текст результата
    result = (
        f"Имя:          {name}\n"
        f"Фамилия:      {surname}\n"
        f"Возраст:      {age}\n"
        f"Город:        {city}\n"
        f"Статус:       {status}\n"
        f"Логин:        {login}\n"
        f"--------------------------\n"
        f"Имя наоборот: {name_reversed}\n"
        f"Букв в имени: {name_length}\n"
    )

    if has_a:
        result += "В имени есть буква «а»\n"
    else:
        result += "В имени нет буквы «а»\n"

    result += "--------------------------\n"

    if access:
        result += f"\nДобро пожаловать, {name} {surname}!"
    else:
        result += "\nК сожалению, регистрация невозможна."

    # Выводим результат в текстовое поле
    text_result.config(state="normal")
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, result)
    text_result.config(state="disabled")


# ====================== Создание окна ======================
window = tk.Tk()
window.title("Умный регистратор")
window.geometry("500x550")
window.resizable(False, False)

# Заголовок
label_title = tk.Label(window, text="УМНЫЙ РЕГИСТРАТОР", font=("Arial", 16, "bold"))
label_title.pack(pady=15)

# ----- Поля ввода -----
frame_inputs = tk.Frame(window)
frame_inputs.pack(pady=5)

tk.Label(frame_inputs, text="Имя:", font=("Arial", 11)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_name = tk.Entry(frame_inputs, width=30, font=("Arial", 11))
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Фамилия:", font=("Arial", 11)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_surname = tk.Entry(frame_inputs, width=30, font=("Arial", 11))
entry_surname.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Возраст:", font=("Arial", 11)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_age = tk.Entry(frame_inputs, width=30, font=("Arial", 11))
entry_age.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Город:", font=("Arial", 11)).grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_city = tk.Entry(frame_inputs, width=30, font=("Arial", 11))
entry_city.grid(row=3, column=1, padx=5, pady=5)

# Кнопка
btn_register = tk.Button(window, text="Зарегистрировать", font=("Arial", 12, "bold"),
                         bg="#4CAF50", fg="white", width=20, command=register)
btn_register.pack(pady=15)

# Поле для вывода результата
tk.Label(window, text="Результат:", font=("Arial", 11, "bold")).pack()
text_result = tk.Text(window, height=12, width=50, font=("Consolas", 10), state="disabled")
text_result.pack(pady=5)

# Запуск
window.mainloop()
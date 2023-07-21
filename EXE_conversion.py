import os
import tkinter as tk
from tkinter import filedialog
import subprocess


def convert_to_exe():
    file_path = entry.get()
    if not file_path:
        return

    try:
        # Убедимся, что файл существует
        if not os.path.isfile(file_path):
            status_label.config(text=f"Файл {file_path} не найден.", fg="red")
            return

        # Получим базовое имя файла без расширения
        base_name = os.path.splitext(os.path.basename(file_path))[0]

        # Создадим папку для сохранения exe-файла
        output_dir = os.path.join(os.path.dirname(file_path), "dist")
        os.makedirs(output_dir, exist_ok=True)

        # Запустим PyInstaller для создания exe-файла
        command = f"pyinstaller --onefile --noconsole {file_path}"
        subprocess.run(command, shell=True, check=True)

        # Переместим exe-файл в папку dist
        exe_file = os.path.join("dist", base_name + ".exe")
        if os.path.exists(exe_file):
            os.replace(exe_file, os.path.join(output_dir, base_name + ".exe"))
            status_label.config(text=f"Конвертер {file_path} успешно создан.", fg="green")
        else:
            status_label.config(text="Ошибка создания конвертера.", fg="red")
    except Exception as e:
        status_label.config(text=f"Произошла ошибка: {e}", fg="red")


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)


root = tk.Tk()
root.title("Python to Exe Converter")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Введите путь к файлу Python:")
label.pack()

entry = tk.Entry(frame, width=50)
entry.pack()

browse_button = tk.Button(frame, text="Обзор...", command=browse_file)
browse_button.pack()

convert_button = tk.Button(frame, text="Конвертировать в exe", command=convert_to_exe)
convert_button.pack()

status_label = tk.Label(frame, text="", fg="black")
status_label.pack()

root.mainloop()

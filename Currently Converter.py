import tkinter as tk
from tkinter import ttk

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.create_widgets()

    def create_widgets(self):
        # Валюта "из"
        ttk.Label(self.root, text="Из:").grid(row=0, column=0, padx=5, pady=5)
        self.from_currency = ttk.Combobox(self.root, values=["USD", "EUR", "RUB"], width=5)
        self.from_currency.current(0)
        self.from_currency.grid(row=0, column=1, padx=5, pady=5)

        # Валюта "в"
        ttk.Label(self.root, text="В:").grid(row=0, column=2, padx=5, pady=5)
        self.to_currency = ttk.Combobox(self.root, values=["USD", "EUR", "RUB"], width=5)
        self.to_currency.current(1)
        self.to_currency.grid(row=0, column=3, padx=5, pady=5)

        # Сумма
        ttk.Label(self.root, text="Сумма:").grid(row=1, column=0, padx=5, pady=5)
        self.amount_entry = ttk.Entry(self.root, width=15)
        self.amount_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # Кнопка конвертации
        ttk.Button(self.root, text="Конвертировать", command=self.convert).grid(row=2, columnspan=4, pady=10)

        # Таблица истории
        self.tree = ttk.Treeview(self.root, columns=("from", "to", "amount", "result"), show='headings')
        self.tree.heading("from", text="Из")
        self.tree.heading("to", text="В")
        self.tree.heading("amount", text="Сумма")
        self.tree.heading("result", text="Результат")
        self.tree.grid(row=3, columnspan=4, sticky='nsew')
import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def get_rate(self, from_curr, to_curr):
    try:
        response = requests.get(f"{BASE_URL}{from_curr}")
        data = response.json()
        rate = data['conversion_rates'][to_curr]
        return rate
    except Exception as e:
        print("Ошибка при получении курса:", e)
        return None
def convert(self):
    from_curr = self.from_currency.get()
    to_curr = self.to_currency.get()
    amount = self.amount_entry.get()

    if not amount.replace('.', '', 1).isdigit() or float(amount) <= 0:
        print("Сумма должна быть положительным числом!")
        return

    rate = self.get_rate(from_curr, to_curr)
    if rate is not None:
        result = float(amount) * rate
        self.tree.insert("", "end", values=(from_curr, to_curr, amount, f"{result:.2f}"))
        self.save_history()
import json

def save_history(self):
    data = [self.tree.item(i)['values'] for i in self.tree.get_children()]
    with open('history.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
def load_history(self):
    try:
        with open('history.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for entry in data:
                self.tree.insert("", "end", values=entry)
    except FileNotFoundError:
        pass
amount = self.amount_entry.get().strip()
if not amount.replace('.', '', 1).isdigit() or float(amount) <= 0:
    print("Сумма должна быть положительным числом!")
    return
git init
*.pyc
__pycache__/
history.json  # если не хотите хранить историю в репозитории
git add .
git commit -m "Initial commit"
git remote add origin <ссылка_на_репозиторий>
git push -u origin master

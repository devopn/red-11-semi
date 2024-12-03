from notes import NoteManager
from tasks import TaskManager
from contacts import ContactManager
from finance import FinanceManager
from calculator import Calculator
def main_menu():
    while True:
        print("\nДобро пожаловать в Персональный помощник!")
        print("Выберите действие:")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансовыми записями")
        print("5. Калькулятор")
        print("6. Выход")
        
        choice = input("Введите номер действия: ")
        
        if choice == "1":
            manage_notes()
        elif choice == "2":
            manage_tasks()
        elif choice == "3":
            manage_contacts()
        elif choice == "4":
            manage_finances()
        elif choice == "5":
            calculator()
        elif choice == "6":
            print("Спасибо за использование! До свидания.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

def manage_notes():
    manager = NoteManager()

    while True:
        print("\nУправление заметками:")
        print("1. Создать заметку")
        print("2. Просмотреть все заметки")
        print("3. Просмотреть заметку по ID")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Экспортировать заметки в CSV")
        print("7. Импортировать заметки из CSV")
        print("8. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержимое заметки: ")
            note = manager.create_note(title, content)
            print(f"Заметка создана: {note.to_dict()}")

        elif choice == "2":
            notes = manager.list_notes()
            for note in notes:
                print(note.to_dict())

        elif choice == "3":
            note_id = int(input("Введите ID заметки: "))
            note = manager.get_note_by_id(note_id)
            if note:
                print(note.to_dict())
            else:
                print("Заметка не найдена.")

        elif choice == "4":
            note_id = int(input("Введите ID заметки: "))
            title = input("Введите новый заголовок (или оставьте пустым): ")
            content = input("Введите новое содержимое (или оставьте пустым): ")
            updated_note = manager.update_note(note_id, title=title or None, content=content or None)
            if updated_note:
                print(f"Заметка обновлена: {updated_note.to_dict()}")
            else:
                print("Заметка не найдена.")

        elif choice == "5":
            note_id = int(input("Введите ID заметки для удаления: "))
            manager.delete_note(note_id)
            print("Заметка удалена.")

        elif choice == "6":
            filename = input("Введите имя файла для экспорта (например, notes.csv): ")
            manager.export_to_csv(filename)
            print(f"Заметки экспортированы в {filename}")

        elif choice == "7":
            filename = input("Введите имя файла для импорта (например, notes.csv): ")
            manager.import_from_csv(filename)
            print(f"Заметки импортированы из {filename}")

        elif choice == "8":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


def manage_tasks():
    manager = TaskManager()

    while True:
        print("\nУправление задачами:")
        print("1. Добавить новую задачу")
        print("2. Просмотреть список задач")
        print("3. Отметить задачу как выполненную")
        print("4. Редактировать задачу")
        print("5. Удалить задачу")
        print("6. Экспортировать задачи в CSV")
        print("7. Импортировать задачи из CSV")
        print("8. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок задачи: ")
            description = input("Введите описание задачи (опционально): ")
            priority = input("Введите приоритет (Высокий, Средний, Низкий): ")
            due_date = input("Введите срок выполнения (ДД-ММ-ГГГГ, опционально): ")
            task = manager.create_task(title, description, priority, due_date)
            print(f"Задача создана: {task.to_dict()}")

        elif choice == "2":
            print("\nСписок задач:")
            for task in manager.list_tasks():
                print(task.to_dict())

        elif choice == "3":
            task_id = int(input("Введите ID задачи: "))
            task = manager.update_task(task_id, done=True)
            if task:
                print(f"Задача отмечена как выполненная: {task.to_dict()}")
            else:
                print("Задача не найдена.")

        elif choice == "4":
            task_id = int(input("Введите ID задачи: "))
            title = input("Введите новый заголовок (или оставьте пустым): ")
            description = input("Введите новое описание (или оставьте пустым): ")
            priority = input("Введите новый приоритет (Высокий, Средний, Низкий): ")
            due_date = input("Введите новый срок выполнения (ДД-ММ-ГГГГ, или оставьте пустым): ")
            task = manager.update_task(
                task_id,
                title=title or None,
                description=description or None,
                priority=priority or None,
                due_date=due_date or None,
            )
            if task:
                print(f"Задача обновлена: {task.to_dict()}")
            else:
                print("Задача не найдена.")

        elif choice == "5":
            task_id = int(input("Введите ID задачи для удаления: "))
            manager.delete_task(task_id)
            print("Задача удалена.")

        elif choice == "6":
            filename = input("Введите имя файла для экспорта (например, tasks.csv): ")
            manager.export_to_csv(filename)
            print(f"Задачи экспортированы в {filename}")

        elif choice == "7":
            filename = input("Введите имя файла для импорта (например, tasks.csv): ")
            manager.import_from_csv(filename)
            print(f"Задачи импортированы из {filename}")

        elif choice == "8":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


def manage_contacts():
    manager = ContactManager()

    while True:
        print("\nУправление контактами:")
        print("1. Добавить новый контакт")
        print("2. Поиск контакта")
        print("3. Редактировать контакт")
        print("4. Удалить контакт")
        print("5. Экспортировать контакты в CSV")
        print("6. Импортировать контакты из CSV")
        print("7. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите имя контакта: ")
            phone = input("Введите номер телефона (опционально): ")
            email = input("Введите адрес электронной почты (опционально): ")
            contact = manager.create_contact(name, phone, email)
            print(f"Контакт создан: {contact.to_dict()}")

        elif choice == "2":
            query = input("Введите имя или номер телефона для поиска: ")
            results = manager.search_contacts(query)
            if results:
                print("\nНайденные контакты:")
                for contact in results:
                    print(contact.to_dict())
            else:
                print("Контакты не найдены.")

        elif choice == "3":
            contact_id = int(input("Введите ID контакта для редактирования: "))
            name = input("Введите новое имя (или оставьте пустым): ")
            phone = input("Введите новый номер телефона (или оставьте пустым): ")
            email = input("Введите новый адрес электронной почты (или оставьте пустым): ")
            contact = manager.update_contact(
                contact_id,
                name=name or None,
                phone=phone or None,
                email=email or None,
            )
            if contact:
                print(f"Контакт обновлён: {contact.to_dict()}")
            else:
                print("Контакт не найден.")

        elif choice == "4":
            contact_id = int(input("Введите ID контакта для удаления: "))
            manager.delete_contact(contact_id)
            print("Контакт удалён.")

        elif choice == "5":
            filename = input("Введите имя файла для экспорта (например, contacts.csv): ")
            manager.export_to_csv(filename)
            print(f"Контакты экспортированы в {filename}")

        elif choice == "6":
            filename = input("Введите имя файла для импорта (например, contacts.csv): ")
            manager.import_from_csv(filename)
            print(f"Контакты импортированы из {filename}")

        elif choice == "7":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")



def manage_finances():
    manager = FinanceManager()

    while True:
        print("\nУправление финансами:")
        print("1. Добавить финансовую запись")
        print("2. Просмотреть записи")
        print("3. Удалить запись")
        print("4. Рассчитать баланс")
        print("5. Сгенерировать отчёт")
        print("6. Экспортировать записи в CSV")
        print("7. Импортировать записи из CSV")
        print("8. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            amount = float(input("Введите сумму операции (отрицательная для расходов): "))
            category = input("Введите категорию (например, 'Еда', 'Транспорт'): ")
            date = input("Введите дату (ДД-ММ-ГГГГ): ")
            description = input("Введите описание (опционально): ")
            record = manager.add_record(amount, category, date, description)
            print(f"Запись добавлена: {record.to_dict()}")

        elif choice == "2":
            filter_option = input("Фильтровать по дате (1) или категории (2), или показать все (3)? ")
            if filter_option == "1":
                date = input("Введите дату (ДД-ММ-ГГГГ): ")
                records = manager.view_records(filter_by={"date": date})
            elif filter_option == "2":
                category = input("Введите категорию: ")
                records = manager.view_records(filter_by={"category": category})
            else:
                records = manager.view_records()
            for record in records:
                print(record.to_dict())

        elif choice == "3":
            record_id = int(input("Введите ID записи для удаления: "))
            manager.delete_record(record_id)
            print("Запись удалена.")

        elif choice == "4":
            balance = manager.calculate_balance()
            print(f"Общий баланс: {balance}")

        elif choice == "5":
            start_date = input("Введите начальную дату (ДД-ММ-ГГГГ): ")
            end_date = input("Введите конечную дату (ДД-ММ-ГГГГ): ")
            report = manager.generate_report(start_date, end_date)
            print(f"Доходы: {report['income']}, Расходы: {report['expenses']}, Баланс: {report['balance']}")

        elif choice == "6":
            filename = input("Введите имя файла для экспорта (например, finance.csv): ")
            manager.export_to_csv(filename)
            print(f"Записи экспортированы в {filename}")

        elif choice == "7":
            filename = input("Введите имя файла для импорта (например, finance.csv): ")
            manager.import_from_csv(filename)
            print(f"Записи импортированы из {filename}")

        elif choice == "8":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


def use_calculator():
    calc = Calculator()

    while True:
        print("\nКалькулятор:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Ввод выражения")
        print("6. Назад")

        choice = input("Выберите действие: ")

        if choice in ["1", "2", "3", "4"]:
            try:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))

                if choice == "1":
                    print(f"Результат: {calc.add(a, b)}")
                elif choice == "2":
                    print(f"Результат: {calc.subtract(a, b)}")
                elif choice == "3":
                    print(f"Результат: {calc.multiply(a, b)}")
                elif choice == "4":
                    print(f"Результат: {calc.divide(a, b)}")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "5":
            expression = input("Введите математическое выражение: ")
            try:
                result = calc.calculate(expression)
                print(f"Результат: {result}")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "6":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()

import json
from datetime import datetime


class FinanceRecord:
    def __init__(self, record_id, amount, category, date, description=""):
        self.id = record_id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            record_id=data["id"],
            amount=data["amount"],
            category=data["category"],
            date=data["date"],
            description=data.get("description", ""),
        )


class FinanceManager:
    FILE_NAME = "finance.json"

    def __init__(self):
        self.records = self.load_records()

    def load_records(self):
        try:
            with open(self.FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [FinanceRecord.from_dict(record) for record in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_records(self):
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump([record.to_dict() for record in self.records], file, ensure_ascii=False, indent=4)

    def add_record(self, amount, category, date, description=""):
        new_id = max((record.id for record in self.records), default=0) + 1
        new_record = FinanceRecord(new_id, amount, category, date, description)
        self.records.append(new_record)
        self.save_records()
        return new_record

    def view_records(self, filter_by=None):
        if filter_by:
            if "date" in filter_by:
                return [record for record in self.records if record.date == filter_by["date"]]
            if "category" in filter_by:
                return [record for record in self.records if record.category == filter_by["category"]]
        return self.records

    def delete_record(self, record_id):
        self.records = [record for record in self.records if record.id != record_id]
        self.save_records()

    def calculate_balance(self):
        return sum(record.amount for record in self.records)

    def generate_report(self, start_date, end_date):
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y")
        filtered_records = [
            record for record in self.records
            if start_date <= datetime.strptime(record.date, "%d-%m-%Y") <= end_date
        ]
        income = sum(record.amount for record in filtered_records if record.amount > 0)
        expenses = sum(record.amount for record in filtered_records if record.amount < 0)
        return {"income": income, "expenses": expenses, "balance": income + expenses}

    def export_to_csv(self, filename):
        import csv

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "amount", "category", "date", "description"])
            writer.writeheader()
            for record in self.records:
                writer.writerow(record.to_dict())

    def import_from_csv(self, filename):
        import csv

        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.add_record(
                    amount=float(row["amount"]),
                    category=row["category"],
                    date=row["date"],
                    description=row.get("description", ""),
                )

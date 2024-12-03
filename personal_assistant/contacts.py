import json


class Contact:
    def __init__(self, contact_id, name, phone="", email=""):
        self.id = contact_id
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            contact_id=data["id"],
            name=data["name"],
            phone=data.get("phone", ""),
            email=data.get("email", ""),
        )


class ContactManager:
    FILE_NAME = "contacts.json"

    def __init__(self):
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Contact.from_dict(contact) for contact in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_contacts(self):
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, ensure_ascii=False, indent=4)

    def create_contact(self, name, phone="", email=""):
        new_id = max((contact.id for contact in self.contacts), default=0) + 1
        new_contact = Contact(contact_id=new_id, name=name, phone=phone, email=email)
        self.contacts.append(new_contact)
        self.save_contacts()
        return new_contact

    def search_contacts(self, query):
        return [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]

    def update_contact(self, contact_id, name=None, phone=None, email=None):
        contact = self.get_contact_by_id(contact_id)
        if contact:
            if name:
                contact.name = name
            if phone:
                contact.phone = phone
            if email:
                contact.email = email
            self.save_contacts()
            return contact
        return None

    def delete_contact(self, contact_id):
        self.contacts = [contact for contact in self.contacts if contact.id != contact_id]
        self.save_contacts()

    def get_contact_by_id(self, contact_id):
        return next((contact for contact in self.contacts if contact.id == contact_id), None)

    def export_to_csv(self, filename):
        import csv

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name", "phone", "email"])
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.to_dict())

    def import_from_csv(self, filename):
        import csv

        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.create_contact(name=row["name"], phone=row.get("phone", ""), email=row.get("email", ""))

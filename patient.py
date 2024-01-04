class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact_name, emergency_contact_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone

    # Accessor methods
    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def get_address(self):
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"

    def get_phone_number(self):
        return self.phone_number

    def get_emergency_contact_info(self):
        return f"{self.emergency_contact_name} - {self.emergency_contact_phone}"


class Procedure:
    def __init__(self, procedure_name, procedure_date, practitioner_name, procedure_charges):
        self.procedure_name = procedure_name
        self.procedure_date = procedure_date
        self.practitioner_name = practitioner_name
        self.procedure_charges = procedure_charges

    # Accessor methods
    def get_procedure_details(self):
        return f"{self.procedure_name} on {self.procedure_date} by {self.practitioner_name}"

    def get_procedure_charges(self):
        return self.procedure_charges


# Sample data for Patient
patient_data = {
    "first_name": "John",
    "middle_name": "Doe",
    "last_name": "Smith",
    "address": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip_code": "12345",
    "phone_number": "555-1234",
    "emergency_contact_name": "Jane Doe",
    "emergency_contact_phone": "555-5678",
}

# Create instance of Patient
patient = Patient(**patient_data)

# Sample data for Procedures
procedure_data = [
    {"procedure_name": "Physical Exam", "procedure_date": "2024-01-04", "practitioner_name": "Dr. Irvin", "procedure_charges": 250.00},
    {"procedure_name": "X-ray", "procedure_date": "2024-01-04", "practitioner_name": "Dr. Jamison", "procedure_charges": 500.00},
    {"procedure_name": "Blood Test", "procedure_date": "2024-01-04", "practitioner_name": "Dr. Smith", "procedure_charges": 200.00},
]

# Create instances of Procedures
procedures = [Procedure(**data) for data in procedure_data]

# Display patient information
print("Patient Information:")
print("Name:", patient.get_full_name())
print("Address:", patient.get_address())
print("Phone Number:", patient.get_phone_number())
print("Emergency Contact:", patient.get_emergency_contact_info())
print("\nProcedure Information:")

# Display procedure details and accumulate total charges
total_charges = 0.0
for procedure in procedures:
    print(procedure.get_procedure_details())
    print("Charges:", procedure.get_procedure_charges())
    total_charges += procedure.get_procedure_charges()
    print()

# Display total charges
print("Total Charges for All Procedures:", total_charges)

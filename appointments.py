def get_valid_phone():
    phone_number = input("Enter your phone number: ")
    while len(phone_number) != 11 or not phone_number.isdigit():
        print("❌ Invalid phone number. It must be exactly 11 digits.")
        phone_number = input("Enter your phone number: ")
    return phone_number
def add_patient(name,age):
    patient = {"name": name, "age": age, "phone_number": get_valid_phone()}
    print("✔ Patient added successfully")
    return patient

def save_patient(patient):
    file = open("patients.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("patients.txt", "w")
    for line in lines:
        file.write(line)
    file.write(patient["name"] + "," + patient["age"] + "," + patient["phone_number"] + "\n")
    file.close()
    print("✔ Patient saved successfully")

def load_patients():
    patients = {}
    file = open("patients.txt", "r")
    index = 1
    for line in file:
        name, age, phone = line.strip().split(",")
        patients[index] = {"name": name,"age": age,"phone_number": phone}
        index += 1
    file.close()
    print("✔ Patients loaded.")
    return patients
def load_appointments():
    appointments = {}
    file = open("appointments.txt", "r")
    index = 1
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) != 3:
            continue
        name, date, time = parts
        appointments[index] = {"name": name, "date": date, "time": time}
        index += 1
    file.close()
    return appointments

def check_availability(date, time, appointments):
    for key in appointments:
        if appointments[key]["date"] == date and appointments[key]["time"] == time:
            return False
    return True

def book_appointment(name, date, time):
    appointments = load_appointments()
    if not check_availability(date, time, appointments):
        print("❌ This time is already booked.")
        return
    file = open("appointments.txt", "w")
    for key in appointments:
        appt = appointments[key]
        file.write(f"{appt['name']},{appt['date']},{appt['time']}\n")
    file.write(f"{name},{date},{time}\n")
    file.close()
    print("✔ Appointment booked successfully.")
    appointments = load_appointments()
    if detect_conflict(appointments):
        print("Warning: appointment conflict detected!")

def appointment_exists(name):
    appts = load_appointments()
    for a in appts.values():
        if a["name"] == name:
            return True
    return False

def update_appointment(name, key, value):
    appts = load_appointments()
    for a in appts.values():
        if a["name"] == name:
            a[key] = value
            with open("appointments.txt", "w") as file:
                for x in appts.values():
                    file.write(",".join(x.values()) + "\n")
            return True
    return False

def search_appointment(patient_name):
    results = {}
    file = open("appointments.txt", "r")
    index = 1
    for line in file:
        name, date, time = line.strip().split(",")
        if name == patient_name:
            results[index] = {"date": date, "time": time}
            index += 1
    file.close()
    if results:
        print(f"Appointments for {patient_name}:")
        for key in results:
            print(f"- {results[key]['date']} at {results[key]['time']}")
    else:
        print("No appointments found.")

def cancel_appointment(name, date_to_cancel, time_to_cancel):
    updated = {}
    file = open("appointments.txt", "r")
    index = 1
    found = False
    for line in file:
        n, d, t = line.strip().split(",")
        if n == name and d == date_to_cancel and t == time_to_cancel:
            found = True
        else:
            updated[index] = {"name": n, "date": d, "time": t}
            index += 1
    file.close()
    file = open("appointments.txt", "w")
    for key in updated:
        a = updated[key]
        file.write(f"{a['name']},{a['date']},{a['time']}\n")
    file.close()
    if found:
        print("✔ Appointment cancelled.")
    else:
        print("❌ Appointment not found.")

def detect_conflict(appointments):
    for i in appointments:
        for j in appointments:
            if i != j:
                if (appointments[i]["date"] == appointments[j]["date"] and
                    appointments[i]["time"] == appointments[j]["time"]):
                    print("❌ Conflict detected!")
                    return True
    return False

from tabulate import tabulate
def view_patient_info(name):
    patients = load_patients()
    appointments = load_appointments()
    patient_found = None
    for p in patients.values():
        if p["name"] == name:
            patient_found = p
            break
    if not patient_found:
        print(f"❌ Patient '{name}' not found.")
        return
    patient_appts = []
    for appt in appointments.values():
        if appt["name"] == name:
            patient_appts.append([patient_found["name"],patient_found["age"],patient_found["phone_number"],appt["date"],appt["time"]])
    if patient_appts:
        print("\nPatient Schedule:")
        print(tabulate(patient_appts,headers=["Name", "Age", "Phone", "Date", "Time"],tablefmt="grid"))
    else:
        print(f"\nNo appointments found for {name}.")

def display_schedule():
    appointments = load_appointments()
    if not appointments:
        print("No appointments found.")
        return
    table = []
    for key in appointments:
        appt = appointments[key]
        table.append([key, appt["name"], appt["date"], appt["time"]])
    print(tabulate(table, headers=["ID", "Name", "Date", "Time"], tablefmt="grid"))
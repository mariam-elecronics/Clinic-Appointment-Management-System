import customtkinter as ctk
from appointments import *

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x600")
app.title("Clinic Appointment System")

FONT_TITLE = ("Arial", 22, "bold")

sidebar = ctk.CTkFrame(app, width=200)
sidebar.pack(side="left", fill="y", padx=10, pady=10)

container = ctk.CTkFrame(app)
container.pack(side="right", expand=True, fill="both", padx=10, pady=10)

status = ctk.CTkLabel(app, text="Ready")
status.pack(side="bottom", fill="x")

def clear():
    for w in container.winfo_children():
        w.destroy()

def card(title):
    f = ctk.CTkFrame(container, corner_radius=20)
    f.pack(expand=True, fill="both", padx=40, pady=40)
    ctk.CTkLabel(f, text=title, font=FONT_TITLE).pack(pady=20)
    return f

def msg(text):
    status.configure(text=text)

# -------- Pages --------
def add_patient_page():
    clear()
    f = card("Add Patient")
    name = ctk.CTkEntry(f, placeholder_text="Name")
    age = ctk.CTkEntry(f, placeholder_text="Age")
    phone = ctk.CTkEntry(f, placeholder_text="Phone (11 digits)")

    for e in (name, age, phone):
        e.pack(pady=10, padx=120, fill="x")

    def save():
        if not name.get() or not age.get() or not phone.get():
            msg("❌ All fields required")
            return
        if len(phone.get()) != 11 or not phone.get().isdigit():
            msg("❌ Invalid phone")
            return
        patient = {"name": name.get(), "age": age.get(), "phone_number": phone.get()}
        save_patient(patient)
        msg("✔ Patient saved")

    ctk.CTkButton(f, text="Save Patient", command=save).pack(pady=25)

def book_page():
    clear()
    f = card("Book Appointment")
    name = ctk.CTkEntry(f, placeholder_text="Name")
    date = ctk.CTkEntry(f, placeholder_text="Date (DD-MM-YYYY)")
    time = ctk.CTkEntry(f, placeholder_text="Time (HH:MM)")

    for e in (name, date, time):
        e.pack(pady=10, padx=120, fill="x")

    def book():
        book_appointment(name.get(), date.get(), time.get())
        msg("✔ Appointment booked")

    ctk.CTkButton(f, text="Book Appointment", command=book).pack(pady=25)

def cancel_page():
    clear()
    f = card("Cancel Appointment")
    name = ctk.CTkEntry(f, placeholder_text="Patient Name")
    name.pack(pady=10, padx=120, fill="x")

    def cancel():
        appts = load_appointments()
        found = False
        for a in appts.values():
            if a["name"] == name.get():
                cancel_appointment(a["name"], a["date"], a["time"])
                found = True
        msg("✔ Appointment(s) cancelled" if found else "❌ No appointment found")

    ctk.CTkButton(f, text="Cancel Appointment", command=cancel).pack(pady=25)

def update_page():
    clear()
    f = card("Update Appointment")
    name = ctk.CTkEntry(f, placeholder_text="Patient Name")
    key = ctk.CTkEntry(f, placeholder_text="Key (date / time)")
    value = ctk.CTkEntry(f, placeholder_text="New Value")

    for e in (name, key, value):
        e.pack(pady=10, padx=120, fill="x")

    def update():
        if update_appointment(name.get(), key.get(), value.get()):
            msg("✔ Appointment updated")
        else:
            msg("❌ Appointment not found")

    ctk.CTkButton(f, text="Update Appointment", command=update).pack(pady=25)

def schedule_page():
    clear()
    f = card("Schedule")
    appts = load_appointments()
    for a in appts.values():
        ctk.CTkLabel(f, text=f"{a['name']}   {a['date']}   {a['time']}").pack(pady=5)

# -------- Sidebar Buttons --------
def side_btn(text, cmd):
    ctk.CTkButton(sidebar, text=text, height=40, command=cmd).pack(pady=10, padx=15, fill="x")

side_btn("➕ Add Patient", add_patient_page)
side_btn("📅 Book Appointment", book_page)
side_btn("❌ Cancel Appointment", cancel_page)
side_btn("✏ Update Appointment", update_page)
side_btn("🗓 Schedule", schedule_page)

add_patient_page()
app.mainloop()

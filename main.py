from appointments import (get_valid_phone,add_patient, save_patient, load_patients, book_appointment, search_appointment,
                          cancel_appointment, display_schedule,appointment_exists, update_appointment,view_patient_info)

def main():
    while True:
        print("\nClinic Appointment System")
        print("1. Add patient")
        print("2. Save patient")
        print("3. Load patients")
        print("4. Book appointment")
        print("5. Update appointment")
        print("6. Search appointment")
        print("7. Cancel appointment")
        print("8. View patient info")
        print("9. Display schedule")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Patient name: ")
            age = input("Age: ")
            add_patient(name, age)

        elif choice == "2":
            name = input("Patient name: ")
            age = input("Age: ")
            patient = {"name": name, "age": age, "phone_number":get_valid_phone()}
            save_patient(patient)

        elif choice == "3":
            load_patients()

        elif choice == "4":
            name = input("Patient name: ")
            date = input("Date (DD-MM-YYYY): ")
            time = input("Time (HH:MM): ")
            book_appointment(name, date, time)

        elif choice == "5":
            while True:
                name = input("Patient name: ")
                if appointment_exists(name):
                    break
                print("Appointment does not exist. Try again.")
            key = input("Key to update: ")
            value = input("New value: ")
            update_appointment(name, key, value)
            print("✔ Appointment updated successfully.")

        elif choice == "6":
            name = input("Patient name: ")
            search_appointment(name)

        elif choice == "7":
            name = input("Patient name: ")
            date = input("Date: ")
            time = input("Time: ")
            cancel_appointment(name, date, time)

        elif choice == "8":
            name = input("Patient name: ")
            view_patient_info(name)

        elif choice == "9":
            display_schedule()

        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")
        next_step = input("\nDo you want to return to main menu? (y/n): ")
        if next_step != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
class TravelAgency:
    def _init_(self):
        self.trips = {"available": [], "upcoming": []}
        self.customer_details = {}

    def view_trips(self):
        print("Available Trips:", self.trips["available"] or "No available trips.")
        print("Upcoming Trips:", self.trips["upcoming"] or "No upcoming trips.")

    def add_trip(self):
        trip_name = input("Enter trip name: ")
        trip_type = input("Is the trip 'available' or 'upcoming'? ").lower()

        if trip_type in self.trips:
            self.trips[trip_type].append(trip_name)
            print(f"Trip '{trip_name}' added successfully to {trip_type} trips.")
        else:
            print("Invalid trip type! Choose 'available' or 'upcoming'.")

        self.add_person_details()

    def add_person_details(self):
        name = input("Traveller name: ")
        contact_no = input("Traveller contact number: ")
        email = input("Traveller email: ")

        self.customer_details["name"] = name
        self.customer_details["contact_no"] = contact_no
        self.customer_details["email"] = email

        print("Personal details saved successfully.")
        self.payment()

    def payment(self):
        amount = input("Enter the payment amount: ")
        print(f"Payment of {amount} received. Thank you!")

    def customer_service(self):
        print("1. Trip Updation")
        print("2. Trip Cancelling")
        choice = input("Select an option (1/2): ")

        if choice == "1":
            self.trip_updation()
        elif choice == "2":
            self.trip_cancelling()
        else:
            print("Invalid choice!")

    def trip_updation(self):
        trip_name = input("Enter the name of the trip to update: ")
        new_name = input("Enter the new trip name: ")
        updated = False

        for key in self.trips:
            if trip_name in self.trips[key]:
                self.trips[key].remove(trip_name)
                self.trips[key].append(new_name)
                updated = True
                print(f"Trip '{trip_name}' updated to '{new_name}'.")

        if not updated:
            print(f"Trip '{trip_name}' not found.")

    def trip_cancelling(self):
        trip_name = input("Enter the name of the trip to cancel: ")
        cancelled = False

        for key in self.trips:
            if trip_name in self.trips[key]:
                self.trips[key].remove(trip_name)
                cancelled = True
                print(f"Trip '{trip_name}' cancelled successfully.")

        if not cancelled:
            print(f"Trip '{trip_name}' not found.")

    def main_menu(self):
        while True:
            print("1. View Trips")
            print("2. Add Trip")
            print("3. Customer Service")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.view_trips()
            elif choice == "2":
                self.add_trip()
            elif choice == "3":
                self.customer_service()
            elif choice == "4":
                print("Exiting the Travel Agency system. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")



agency = TravelAgency()
agency.main_menu()
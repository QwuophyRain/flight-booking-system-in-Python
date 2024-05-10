flights = {}

# Add initial flight data
flights["FL123"] = {
    "destination": "New York",
    "departure_time": "10:00 AM",
    "available_seats": 10,
    "reservations": []
}
flights["FL456"] = {
    "destination": "London",
    "departure_time": "08:30 PM",
    "available_seats": 5,
    "reservations": []
}

def book_seat(flight_number, passenger_name):
  if flight_number in flights:
    flight = flights[flight_number]
    if flight["available_seats"] > 0:
      flight["reservations"].append(passenger_name)
      flight["available_seats"] -= 1
      print(f"Seat booked for {passenger_name} on flight {flight_number}.")
    else:
      print(f"Flight {flight_number} is fully booked.")
  else:
    print(f"Invalid flight number: {flight_number}")

# Function to check seat availability
def check_availability(flight_number):
  if flight_number in flights:
    flight = flights[flight_number]
    print(f"Flight {flight_number} has {flight['available_seats']} seats available.")
  else:
    print(f"Invalid flight number: {flight_number}")

# Function to display passenger manifest
def display_manifest(flight_number):
  if flight_number in flights:
    flight = flights[flight_number]
    if flight["reservations"]:
      print(f"Passenger Manifest for Flight {flight_number}:")
      for passenger in flight["reservations"]:
        print(f"- {passenger}")
    else:
      print(f"No passengers booked on flight {flight_number} yet.")
  else:
    print(f"Invalid flight number: {flight_number}")

# Example usage
passenger1 = "Mr. Kwame Musah"
passenger2 = "Miss. Gloria Osei"

book_seat("FL123", passenger1)
check_availability("FL123")
display_manifest("FL123")

book_seat("FL456", passenger2)
check_availability("FL456")
display_manifest("FL456")
def display(flights):
      for index,flight_info in enumerate(flights):
            print(f"{index}:{flight_info}")
def find(flights):
      finder = input("what flight info you want to find:")
      for index,flight_info in enumerate(flights):
            if finder.upper() in flight_info:
                  print(f"{index}:{flight_info}")

def add(flights):
      departure_time = input("add departure time:")
      flight_identifier = input("add flight identifier :")
      destination = input("add destination :")
      new_flight = f"{departure_time} {flight_identifier } {destination}"
      for item in flights:
            if item == new_flight:
                  print("flight already in the list")
      flights.append(new_flight)
      print(f"new flight added: {new_flight}")

def delete(flights):
      length = len(flights)
      index_delete = int(input("enter the index of the flight want to delete:"))
      while index_delete > length:
            print("index error:input over the flight length")
            index_delete = int(input("enter the index of the flight want to delete:"))
      flights.pop(index_delete)
      print(f"flight number {index_delete} has been deleted")
      
            
# 4) Create a class that captures airline tickets. 
# 	Each ticket lists the departure and arrival cities,
#  a flight number, and a seat assignment.
#  A seat assignment has both a row and a letter for the seat within the row (such as 12F).
#  Make two examples of tickets.


class Airline_tickets:
    def __init(self, departure, arrival_city, flight_no, seat_assigned):
        self.departure = departure
        self.arrival_city = arrival_city
        self.flight_no = flight_no
        self.seat_assigned =  seat_assigned

ticket1 = Airline_tickets("Pune", "Patna", "G202112", "22F")
ticker2 = Airline_tickets("Patna", "Pune", "F453543", "42G")


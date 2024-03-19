import random


def pick_random_winner(names):
    """param: list of names
     returns: a random name
    """
    return random.choice(names)


class raffle:
    def __init__(self, max_people, max_tickets, price_per_ticket):
        self.max_people = max_people
        self.max_tickets = max_tickets
        self.number_of_sold_tickets = 0
        self.price_per_ticket = price_per_ticket
        self.total_earnings = 0
        self.people = {}

    def add_person(self, name):
        """Add a person to the raffle
          param: name of person to add.
          This method checks if the maximum number of people has been reached
          if so it returns False else it adds the person to the raffle
           returns: bool: True if the person is successfully added, False otherwise.
        """
        if len(self.people) == self.max_people:
            print("Maximum number of people reached")
            return False
        self.people[name] = 0
        print(f"Person {name} added successfully")
        return True

    def sell_ticket(self, name):
        """ Sell a ticket to a person
           param:name of person want to buy a ticket
           This method checks if the maximum number of tickets has not been reached.
           Then checks if we can add it to the raffle or he already there by using add_person method
           Then, it updates the number of tickets owned by the person, adds the ticket price to the total earnings,
           increments the number of sold tickets, prints a success message, and returns True.
           returns: bool: True if the ticket is successfully sold, False otherwise.
          """

        if self.number_of_sold_tickets == self.max_tickets:
            print("Maximum number of sold tickets reached ")
            return False
        if name not in self.people.keys():
            if not self.add_person(name):
                return False
        self.people[name] += 1
        self.total_earnings += self.price_per_ticket
        self.number_of_sold_tickets += 1
        print("Ticket sold successfully")
        return True

    def pick_winner(self):
        """This method picks the winner based on who has the max number of tickets
           if there are more than one it picks random one of them as winner and prints it
           returns:winner name
        """
        if self.number_of_sold_tickets == 0:
            print("There is no winner because no tickets have been sold.")
            return False

        max_counts_ticket = max(self.people.values())
        people_with_max_tickets = [p for p, t in self.people.items() if t == max_counts_ticket]
        if len(people_with_max_tickets) > 1:
            winner = pick_random_winner(people_with_max_tickets)
        else:
            winner = people_with_max_tickets[0]
        print(f"The winner is {winner}!")
        return winner
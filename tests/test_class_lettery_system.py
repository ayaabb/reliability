import random
import unittest
import src.class_lottery_system as ls

unittest.TestLoader.sortTestMethodsUsing = None


class Test_class_lottery_system(unittest.TestCase):
    def setUp(self):
        self.names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank"]

    def test_sell_ticket(self):
        print("sell_ticket test:")
        lottery = ls.raffle(5, 10, 20)
        for i in range(len(self.names)):
            if i < lottery.max_people:
                self.assertTrue(lottery.sell_ticket(self.names[i]))
            else:
                self.assertFalse(lottery.sell_ticket(self.names[i]))
        self.assertEqual(lottery.number_of_sold_tickets, len(lottery.people))
        self.assertEqual(lottery.total_earnings, lottery.price_per_ticket * len(lottery.people))
        # print(
        #     f"this is people {lottery.people} !!!!!!!!!!!!!!!!! {lottery.max_people} {len(lottery.people)}")
        self.assertTrue(lottery.sell_ticket(random.choice(list(lottery.people.keys()))))
        print("\n")

    def test_add_person(self):
        print("add_person test:")
        lottery = ls.raffle(1, 10, 20)
        self.assertTrue(lottery.add_person("bob"))
        self.assertFalse(lottery.add_person("Frank"))
        print("\n")

    def test_pick_random_winner(self):
        # Test picking a random winner from a list of names
        winner = ls.pick_random_winner(self.names)
        self.assertIn(winner, self.names)


    def test_pick_random_winner_empty_list(self):
        # Test picking a random winner from an empty list
        with self.assertRaises(IndexError):
            ls.pick_random_winner([])

    def test_pick_winner(self):
        print("pick_winner test:")
        lottery = ls.raffle(5, 10, 20)
        for i in range(len(self.names)):
            if i < lottery.max_people:
                lottery.sell_ticket(self.names[i])
        winner = lottery.pick_winner()
        self.assertIsNot(False, winner)
        self.assertIn(winner, lottery.people.keys())
        self.assertEqual(lottery.people[winner], max(lottery.people.values()))
        lottery.sell_ticket('Alice')
        lottery.sell_ticket('Bob')
        winner = lottery.pick_winner()
        self.assertIsNot(False, winner)
        self.assertIn(winner,['Bob','Alice'])
        lottery.sell_ticket('Alice')
        winner = lottery.pick_winner()
        self.assertIsNot(False, winner)
        self.assertEqual(winner,  'Alice')
        print("\n")

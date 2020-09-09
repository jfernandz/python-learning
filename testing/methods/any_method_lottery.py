tickets = [11, 22, 33, 44, 55]
winning_tickets = [i >= 44 for i in tickets]
print(winning_tickets)
tickets_bool = any(winning_tickets)
print(tickets_bool)

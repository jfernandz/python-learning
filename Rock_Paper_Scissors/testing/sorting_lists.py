dis_list = ["rock", "paper", "scissors", "lizard", "spock"]

ord_list = ["rock", "spock", "paper", "lizard", "scissors"]

user_choice = "lizard"

new_list = ord_list[ord_list.index(user_choice) + 1:] \
    + ord_list[:ord_list.index(user_choice)]

print(new_list[:len(new_list) // 2])
print(new_list[len(new_list) // 2:])

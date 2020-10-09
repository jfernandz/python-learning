# read animals.txt
# and write animals_new.txt

animals_file = open('animals.txt', 'r')
animals_new_file = open('animals_new.txt', 'w')

animals = [line.replace('\n', ' ') for line in animals_file]
animals_new_file.writelines(animals)

animals_file.close()
animals_new_file.close()

test_numbers_1 = [1, 2, 3, 4]

# updated_numbers = [n + 1 for n in numbers]
# print(updated_numbers)

# name = "Hamza"
# word_by_word = [word for word in name]
# print(word_by_word)

# doubled_numbers = [n * 2 for n in range(1,5)]
# print(doubled_numbers)

# test_numbers_2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num * num for num in test_numbers_2]
# print(squared_numbers)

names = ["Alan", "Beth", "Leyla", "Dominykas", "Hamza", "Sultan", "Murad", "Ieva"]

# short_names = [name for name in names if len(name) <= 4]
# print(short_names)

# capital_names = [name.upper() for name in names if len(name) > 4]
# print(capital_names)

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(num) for num in list_of_strings]
# even_numbers_without_zero = [num for num in numbers if num % 2 == 0 and num != 0]
# print(result)

# with open("file1.txt") as first_numbers:
#     file1_numbers = first_numbers.readlines()
#
# with open("file2.txt") as second_numbers:
#     file2_numbers = second_numbers.readlines()
#
# numbers = file2_numbers + file1_numbers
# result = [int(num) for num in file1_numbers if num in file2_numbers]
#
# print(result)

# import random
# student_scores = {
#     student:random.randint(20,100) for student in names
# }
#
# passed_students = {
#     student:score for (student,score) in student_scores.items() if score >= 60
# }
# print(student_scores)
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# weather_f = {
#     day:((temp_c * 9/5) + 32) for (day,temp_c) in weather_c.items()
# }
# print(weather_f)
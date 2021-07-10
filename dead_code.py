# def login(type, username, password):
#     """ Check if any line in the file contains given string """
#     # Open the file in read only mode
#     with open("login_details.txt", 'r') as read_obj:
#         # Read all lines in the file one by one
#         for line in read_obj:
#             # For each line, check if line contains the string
#             if type and username and password in line:
#                 print("Accepted Login!!!!\n")
#                 return True
#     print("GO AWAY HACKER!\n")
#     return False


# def order_retriever(order_no):
#     id_looper = 0
#     for i in order_trackers:
#         if order_no == order_trackers[id_looper]._order_no:
#             print("\nHURRAAAAY! THE ORDERING SYSTEM IS WORKING MAGNIFICENTLY!!\n")
#             print(order_trackers[id_looper])
#             break
#         id_looper = id_looper + 1

# def store_credentials(type, obj):  # Type    Username    Lastname
#     login_file = open("login_details.txt", "a")
#     login_file.write(f"{type}\t{obj._username}\t{obj._password}\n")
#     login_file.close()


# def find_duplicate_reader(username):  # True = duplicate found     False = no duplicates
#     for i in readers:
#         if i._username == username:
#             return True
#     return False


# jayavarman.add_book(Book("Monthly Subscription for 90% off on ALL orders!", 1, "Library", "2020", 0, 399.99, 9999))
# jayavarman.add_book(Book("The Art of War", 2, "Sun Tzu", "523", 1382, 199.99, 9))
# jayavarman.add_book(Book("The Odyssey", 3, "Homer", "-420", 2417, 499.98, 4))
# Pericles.add_book(Book("Liza of Lambeth", 4, "W. Somerset Maugham", "-1897", 755, 149.99, 7))
# Pericles.add_book(Book("Don Quixote", 5, "Miguel de Cervantes", "1900", 899, 249.99, 8))
# Pericles.add_book(Book("War and Peace", 6, "Leo Tolstoy", "-1800", 999, 199.99, 6))
# Pericles.add_book(Book("Hamlet", 7, "William Shakespeare", "1601", 709, 399.99, 2))
# Pericles.add_book(Book("Great Expectations", 8, "Charles Dickens", "1850", 791, 119.99, 4))
# Pericles.add_book(Book("One Thousand and One Nights", 9, "India/Iran/Iraq/Egypt", "1200", 1001, 1000.99, 1))
# Pericles.add_book(Book("The Fault in Our Stars", 10, "John Green", "2012", 313, 99.99, 8))


###OLD MAIN#####
# from classes import *
#
# Maktaba = Library("El-Horyya", "Cairo", 29, "1930")
#
# #  (firstname, lastname, dob  , shift_type, shift_duration, salary, location, username, password)
#
# # jayavarman = create_Administrator_account("jayavarman", "VII", "1130", "rotational", "8h", 7000, "cambodia", "civ6", "worstcivever")
# jayavarman = login("civ6", "worstcivever")
#
# # jayavarman = Administrator("jayavarman", "VII", "1130", "rotational", "8h", 7000, "cambodia", "civ6", "worstcivever")
# Pericles = Administrator("Pericles", "Democracy", "-210", "full", "12h", 25000, "Greece", "culture", "victory")
#
#
# load_books()
#
#
# # fawzy = Reader("Ahmed", "Fawzy", "1999", "Cairo", "ahmed", "fawzy00")
#
# ruby = Reader("Ruby", "Rabya", "1988", "Syria", "ruby", "leehbydary")
#
#
# # Saladin = Librarian("Saladin", "Saladin", "-Saladin", "Saladin", "Saladin", 25000, "Saladin", "Saladin", "Saladin")
# # Saladin.search_orders(826196)
#
#
# create_reader_account("Ahmed", "Fawzy", "1999", "Cairo", "iahmed", "fawzy00")
# fawzy = login("iahmed", "fawzy00")
#
#
#
# quit = False
# while not quit:
#
#     while True:
#
#         print("\nEnter the book ID You would like to purchase:\t")
#         system_libraries[0].show_books()
#         book_choice = int(input())
#         fawzy.add_to_cart(book_choice)
#         user_choice = int(input("Would you like to add another book?\n 1): Yes\n2): No, "
#                                 "go to checkout\n"))
#         if user_choice == 2:
#             break
#     # fawzy.add_to_cart(2)
#     fawzy.checkout()
#
#     quit_option = int(input("Would You like to quit, quitter? Enter 1 to quit or 0 to keep shopping\t"))
#     if quit_option:
#         quit = True
###NEW MAIN#####

from dataclasses import dataclass
import random
import pickle

system_libraries = []
payment_options = ["cash", "fawry", "google pay", "apple pay"]
pay_or_rent = ["purchased", "rented"]
order_trackers = []  # List of all Orders within the systems
system_books = []



def view_cart(current_user):
    None

def create_library(lib_name, lib_location, lib_staff_count, lib_found_date):
    if not find_duplicate_user(lib_name):  # make sure username is unique

        lib = Library(lib_name, lib_location, lib_staff_count, lib_found_date)

        pickle_file_name = lib_name + ".pickle"
        pickle_out = open(pickle_file_name, "wb")
        pickle.dump(lib, pickle_out)
        pickle_out.close()

        print("Reader account created and pickled successfully\n")
        return lib
        # return readers[len(readers) - 1]  # Return the index of the recently created item.
    else:
        return False

def find_duplicate_lib(libname):  # True = duplicate found     False = no duplicates
    with open("library.txt", 'r') as registered_libs:
        # Read all lines in the file one by one
        for line in registered_libs:
            # For each line, check if line contains the string
            if libname in line:
                return True
    return False

def load_library(lib_name):
    pickle_file_name = lib_name + ".pickle"
    pickle_in = open(pickle_file_name, "rb")
    lib_obj = pickle.load(pickle_in)
    system_libraries.append(lib_obj)


    pickle_in_books = open("books.pickle", "rb")
    lib_obj._list_of_books = pickle.load(pickle_in_books)


    #print(f"Library: {lib_obj._name} loaded!\n\n")
    #print(f"Library_book[1]: {lib_obj._list_of_books[1]} confirmed\n\n")

    return lib_obj


def order_no_generator(a=100000, b=999999):
    return random.randint(a, b)


def find_duplicate_user(username):  # True = duplicate found     False = no duplicates
    with open("usernames.txt", 'r') as registered_users:
        # Read all lines in the file one by one
        for line in registered_users:
            # For each line, check if line contains the string
            if username in line:
                return True
    return False


def create_reader_account(firstname, lastname, date_of_birth, location, username, password):


    librarian = Reader(firstname, lastname, date_of_birth, location, username, password)

    pickle_file_name = username + ".pickle"
    pickle_out = open(pickle_file_name, "wb")
    pickle.dump(librarian, pickle_out)
    pickle_out.close()

        #print("Reader account created and pickled successfully\n")
    return librarian
        # return readers[len(readers) - 1]  # Return the index of the recently created item.

def create_librarian_account(firstname, lastname, date_of_birth, shift_type, shift_duration, salary, location, username, password):
#    if not find_duplicate_user(username): # make sure username is unique

    reader = Librarian(firstname, lastname, date_of_birth, shift_type, shift_duration, salary, location, username, password)

    pickle_file_name = username + ".pickle"
    pickle_out = open(pickle_file_name, "wb")
    pickle.dump(reader, pickle_out)
    pickle_out.close()

    #print("Reader account created and pickled successfully\n")
    #print(reader)
    return reader
    # else:
    #     print("incorrect registration parameters\n")

def create_Administrator_account(firstname, lastname, date_of_birth, shift_type, shift_duration, salary, location, username, password):
    # if not find_duplicate_user(username): # make sure username is unique

    admin = Administrator(firstname, lastname, date_of_birth, shift_type, shift_duration, salary, location, username, password)

    pickle_file_name = username + ".pickle"
    pickle_out = open(pickle_file_name, "wb")
    pickle.dump(admin, pickle_out)
    pickle_out.close()

    #print("Reader account created and pickled successfully\n")
    return admin
    # else:
    #     print("incorrect registration parameters\n")

def store_credentials(type, obj):  # Type    Username    Lastname
    login_file = open("usernames.txt", "a")
    login_file.write(f"{type}\t{obj._username}\n")
    login_file.close()

def store_lib(obj):
    lib = open("library.txt", "a")
    lib.write(f"{obj._name}\n")
    lib.close()

def login(username, password):
    try:
        pickle_file_name = username + ".pickle"
        pickle_in = open(pickle_file_name, "rb")
        user_obj = pickle.load(pickle_in)
    except IOError as e:
        return False



    if (username == user_obj._username) and (password == user_obj._password):
        #print("Accepted Login!!!!\n")
        return user_obj
    else:
        return False


def load_books():
    global system_books
    system_books = pickle.load(open("books.pickle", "rb"))
    return system_books

@dataclass()
class Order:
    _order_creator_ID: int
    _total: str
    _order_cart_list: []
    _order_no: int = order_no_generator()


@dataclass()
#Book("Liza of Lambeth", 4, "W. Somerset Maugham", "-1897", 755, 149.99, 7)
class Book:
    _title: str
    _ID: int
    _author: str
    _release_year: str
    _page_count: int
    _price: float
    book_count: int = 1



@dataclass()
class Librarian:
    _firstname: str
    _lastname: str
    _date_of_birth: str
    _shift_type: str
    _shift_duration: float
    _salary: float
    _username: str
    _password: str

    def __init__(self, firstname, lastname, date_of_birth, shift_type, shift_duration, salary, location, username, password):
        self._firstname = firstname
        self._lastname = lastname
        self._date_of_birth = date_of_birth
        self._shift_type = shift_type
        self._shift_duration = shift_duration
        self._salary = salary
        self._location = location
        self._username = username
        self._password = password
        store_credentials("librarian", self)




@dataclass()
class Administrator:
    _firstname: str
    _lastname: str
    _date_of_birth: str
    _shift_type: str
    _shift_duration: float
    _salary: float
    _location: str
    _username: str
    _password: str

    def __init__(self, firstname, lastname, date_of_birth, shift_type, shift_duration, salary, location, username, password):
        self._firstname = firstname
        self._lastname = lastname
        self._date_of_birth = date_of_birth
        self._shift_type = shift_type
        self._shift_duration = shift_duration
        self._salary = salary
        self._location = location
        self._username = username
        self._password = password
        store_credentials("admin", self)

    def add_book(self, Book, libId=0):
        system_libraries[0]._list_of_books.append(Book)
        system_libraries[0]._lib_book_count += 1
        Book.book_count += 1

        system_books.append(Book)
        pickle_out = open("books.pickle", "wb")
        pickle.dump(system_books, pickle_out)
        pickle_out.close()
        load_books()

    def remove_book(self, bk_name):

        books_file = open("books.pickle", "rb")
        list_of_books = pickle.load(books_file)

        bk_index = -2
        looper = -1
        # 1. get the book index
        for book in list_of_books:
            looper += 1
            if bk_name == book._title:
                bk_index = looper
                break

        # 2. Remove the index
        if bk_index != -2:
            del list_of_books[bk_index]

            pickle_out = open("books.pickle", "wb")
            pickle.dump(list_of_books, pickle_out)
            pickle_out.close()

            load_books()
            print(load_books())
            return True
        else:
            return False
        # 3. Update books




@dataclass()
class Reader:
    _firstname: str
    _lastname: str
    _date_of_birth: str
    _location: str
    _reader_cart = []  # tuple like this: [("id", "title", "rent", "19.99")]
    _username: str
    _password: str
    _reader_orders = []
    _has_monthly_sub: bool = False
    _registration_date: str = "2021"
    _reader_id: int = order_no_generator(1000, 9999)

    def __init__(self, firstname, lastname, date_of_birth, location, username, password):
        self._firstname = firstname
        self._lastname = lastname
        self._date_of_birth = date_of_birth
        self._location = location
        self._username = username
        self._password = password
        store_credentials("reader", self)

    def get_reader_cart(self):
        return self._reader_cart

    def empty_reader_cart(self):
        self._reader_cart.clear()

    def checkout(self, pmnt_choice, libId=0):
        payment_option = 0
        pay_rent = 0

        total = self.cart_receipt()

        # print(f"your total is {total}")
        # while True:
        #     payment_option = input("please enter the number your preferred payment method:\n"
        #                            "1): cash\n2): Fawry\n3): Google Pay\n4): Apple Pay\n")
        #     payment_option = int(payment_option)
        #
        #     if payment_option != 1 and payment_option != 2 and payment_option != 3 and payment_option != 4:
        #         print("please enter a valid number")
        #     else:
        #         break

        payment_option = pmnt_choice

        # payment_option = payment_option - 1  # index starts at 0 w keda
        #
        # if payment_option > 0:  # online payment
        #     print(f"connecting to {payment_options[payment_option]}'s servers for payment...\n")
        #     print(f"successfully paid {total} via {payment_options[payment_option]}")
        # else:
        #     print(f"An amount of {total} will be paid in cash\n")

        cur_order = Order(self._reader_id, total, self._reader_cart)

        for i in self._reader_cart:
            if i[0] == 1:  # Monthly Subscription ID
                self._has_monthly_sub = True

        order_trackers.append(cur_order)  # Register the order to the system
        self._reader_orders.append(cur_order)  # Add the order to history log of user's purchases

        orders_file = open("orders.txt", "a")
        orders_file.write(
            f"{cur_order._order_creator_ID}\t{cur_order._total}\t{cur_order._order_cart_list}\t{cur_order._order_no}\n")
        orders_file.close()

        return cur_order._order_no



    def add_to_cart(self, Bk, pay_rent, libId=0): # Bk._ID

        if Bk._ID == 1:  # Monthly subscription, not applicable for rent/purchase.
            print(Bk._ID)
            pay_rent = 1

        for book in enumerate(system_libraries[0]._list_of_books):  # idx is equivalent to i in C loops
            if (Bk._ID == book[1]._ID):  # checks if the book exists or not

                if (book[1].book_count > 0):  # checks if the book has enough quantity or not
                    print(f"BOOK TO BE ADDED TO CART: {book[1]}")
                    self._reader_cart.append(tuple((book[1]._ID,
                                                    book[1]._title,
                                                    pay_rent,
                                                    book[1]._price)))
        # Confirmation message:
        if Bk._ID == 1:
            self.subscribe()

        print("Book added to cart!")

    def cart_receipt(self, libId=0):  # embedded function
        total = 0
        idlooper = 0
        print(self._reader_cart)
        for i in self._reader_cart:
            total = total + self._reader_cart[idlooper][3]
            idlooper = idlooper + 1

        if self._has_monthly_sub:
            return 0.1 * total
        else:
            return total

    def subscribe(self, libId=0):
        if not self._has_monthly_sub:
            #self.add_to_cart(0)
            self._has_monthly_sub = True
            print("successfully subscribed to our awesome monthly subscription!\n")


class Library:
    _name: str
    _location: str
    _staff_count: int
    _year_of_building: str
    _list_of_books = []
    _lib_book_count: int

    def __init__(self, name, location, staff_count, year_of_building):
        self._name = name
        self._location = location
        self._staff_count = staff_count
        self._year_of_building = year_of_building
        self._lib_book_count = 0
        self._list_of_books = []
        store_lib(self)

    def show_books(self): # CONSOLE FUNCTION
        idlooper = 1
        for book in self._list_of_books:
            print(f"Book#{idlooper} =>\tTitle: {book._title}, ID: {book._ID}, Author: {book._author}, Released in {book._release_year}, "f"Page count: {book._page_count}, Available in Stock: {book.book_count}")
            idlooper += 1

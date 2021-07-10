# KEDA ANA 5ALAST KOL 7AGA 3ND EL READER.. FADEL EL LIBRARIAN WL ADMIN.. MAYBE ADJUST THE ENTRY OF THE BOOKS. AND TEST

from classes import *
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

current_mode = None
current_user = None
selected_book = None
cart_total = 0
accepted_login = True
add_bk = Book("", -1, "", "", -1, -1, -1)

# create_library("El-Horyya", "Cairo", 29, "1930")
load_library("El-Horyya")

#     def __init__(firstname, lastname, date_of_birth, shift_type, shift_duration, salary, location, username, password):
#   create_librarian_account("Samy", "Yasser", "Nope", "rotational", "8h", 23999, "cairo", "libr", "libr")
#   create_Administrator_account("Admin", "Tester", "2021", "full", "8h", 49999, "Cairo", "admin", "admin")



def rm_book(rm_entry):
    book_name = rm_entry.get()
    removal_result = current_user.remove_book(book_name)

    if removal_result:
        ui_books = load_books()  # UPDATE THE VIEW
        tree.delete(*tree.get_children())
        for Book in ui_books:
            tree.insert('', tk.END, values=(
                Book._title, Book._ID, Book._author, Book._release_year, Book._release_year, Book._price,
                Book._page_count,
                Book.book_count))

        tree.update()
        tree.update_idletasks()
        main_library_screen.update()
        main_library_screen.update_idletasks()

        tk.messagebox.showinfo(title="SUCCESS!", message="BOOK WAS REMOVED SUCCESSFULLY!\n")
    else:
        tk.messagebox.showerror(title="FAILURE!", message="BOOK WAS NOT FOUND!\n")


def add_book_btn_clicked(a, b, c, d, e, f, g):
    global add_bk

    a = a.get()
    b = int(b.get())
    c = c.get()
    d = d.get()
    e = int(e.get())
    f = float(f.get())
    g = int(g.get())

    #   Couldn't add the book here using constructor (ERROR: BOOK IS NOT CALLABLE). THIS IS A WORKAROUND:
    add_bk._title = a
    add_bk._ID = b
    add_bk._author = c
    add_bk._release_year = d
    add_bk._page_count = e
    add_bk._price = f
    add_bk.book_count = g
    current_user.add_book(add_bk)

    ui_books = load_books()  # Array of Book objects as: Book(_title='The Odyssey', _ID=3, _author='Homer', _release_year='-420', _page_count=2417, _price=499.98, book_count=5)
    tree.delete(*tree.get_children())
    for Book in ui_books:
        tree.insert('', tk.END, values=(
            Book._title, Book._ID, Book._author, Book._release_year, Book._release_year, Book._price, Book._page_count,
            Book.book_count))

    raise_frame_no_dest(add_book_screen, main_library_screen)


def search_orders(order_no):
    #   267290
    #   4832319.98[(6, 'War and Peace', 1, 199.99), (8, 'Great Expectations', 1, 119.99)]267290

    """ Check if any line in the file contains given string """
    order_no = str(order_no)
    # Open the file in read only mode
    with open("orders.txt", 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if order_no in line:
                ordern = "ORDER #" + str(order_no) + ":\n\n"
                lst = line.split('\t')
                line = lst[2]
                line = line[:0] + line[0 + 1:]
                line = line[:-1]
                lst = line.split('), (')
                msg = ""
                for x in lst:
                    msg += x + "\n"
                msg = msg[1:]
                msg = msg.replace(')', '')

                tk.messagebox.showinfo(title="Order Details", message=ordern + msg)
                return line
    tk.messagebox.showwarning(title="Order Details", message="ORDER NOT FOUND")


def raise_frame_no_dest(frame_to_destroy, new_frame):
    frame_to_destroy.pack_forget()
    new_frame.tkraise()
    new_frame.pack()


def raise_frame(frame_to_destroy, new_frame, type=None):
    if not accepted_login:
        return
    frame_to_destroy.destroy()
    new_frame.tkraise()
    new_frame.pack()

    global current_mode
    if type != None:
        current_mode = type


#
# admin_label
# admin_add_book_btn
# admin_rm_book_btn
#

def login_btn_clicked(login_username, login_password, isRegister=False):
    global current_mode

    if current_mode == "librarian" or current_mode == "admin":
        view_cart_btn.grid_forget()
        checkout_btn.grid_forget()
        if current_mode == "librarian":
            # admin_label.grid_forget()
            admin_add_book_btn.grid_forget()
            admin_rm_book_btn.grid_forget()
            remove_book_entry.grid_forget()
            bk_rm_entry.grid_forget()
        else:
            lib_label.grid_forget()
            search_order_entry.grid_forget()
            search_ord_id_bk.pack_forget()
            search_ord_id_btn.grid_forget()

    else:
        # lib_label.grid_forget()
        search_ord_id_bk.grid_forget()
        search_ord_id_btn.grid_forget()
        admin_add_book_btn.grid_forget()
        admin_rm_book_btn.grid_forget()
        lib_label.grid_forget()
        search_order_entry.grid_forget()
        search_ord_id_bk.pack_forget()
        search_ord_id_btn.grid_forget()
        remove_book_entry.grid_forget()
        bk_rm_entry.grid_forget()

    # ^END OF GUI BLAH BLAH

    login_username = login_username.get()
    login_password = login_password.get()

    global current_user
    current_user = login(login_username, login_password)

    if isRegister:
        raise_frame(registers_screen, main_library_screen)
        return

    if current_user == False:
        accepted_login = False
        tk.messagebox.showerror(title="ERROR!", message="INCORRECT LOGIN DETAILS!!")
        # raise_frame(reader_login_reg_option, reader_login)
    else:
        accepted_login = True
        raise_frame(reader_login, main_library_screen)

    if current_mode == "reader" or current_mode == "admin":
        tk.messagebox.showinfo(title="WELCOME!", message="WELCOME, " + current_user._firstname)
    else:
        tk.messagebox.showinfo(title="WELCOME!", message="WELCOME, " + current_user._name)

    return current_user


def register_btn_clicked(register_fname, register_lname, register_dob, register_location, register_username,
                         register_pwd):
    register_fname_user = register_fname.get()
    register_lname_user = register_lname.get()
    register_dob_user = register_dob.get()
    register_location_user = register_location.get()
    register_username_user = register_username.get()
    register_pwd_user = register_pwd.get()
    create_reader_account(register_fname_user, register_lname_user, register_dob_user, register_location_user,
                          register_username_user,
                          register_pwd_user)
    login_btn_clicked(register_username, register_pwd, True)
    # raise_frame(registers_screen, main_library_screen, "reader")
    tk.messagebox.showinfo(title="Accepted!", message="Registration Accepted!\nThank You!")


def refresh_frames(keep):
    first_screen.grid_forget()
    reader_login_reg_option.grid_forget()
    reader_register.grid_forget()
    reader_login.grid_forget()
    registers_screen.grid_forget()
    main_library_screen.grid_forget()
    add_book_screen.grid_forget()
    keep.pack()


def search_for_book(str):
    ui_books = load_books()
    for book in ui_books:
        if str == book._title:
            return book
        elif str == book._author:
            return book
    return False


def search_result(entry_box):
    userinput = entry_box.get()
    book = search_for_book(userinput)
    if book != 0:
        res = "Book is found!\n" + book._title + " By " + book._author + " is available for E£" + str(
            book._price) + ".\n" + str(book.book_count) + " copies remaining."
        tk.messagebox.showinfo(title="Book Found!", message=res)
    else:
        tk.messagebox.showwarning(title="Not Found", message="Sorry, We did not find this Book/Author")


def search_for_book_by_ID(id):
    ui_books = load_books()
    for book in ui_books:
        if id == book._ID:
            return book
    return False


def get_book_id_ev(record):
    record = record[1:-1]
    record_list = record.split(",")
    return record_list[1]


def processed_book_info(record):
    # ['The Odyssey', 3, 'Homer', -420, -420, '499.98', 2417, 5]
    record = record[1:-1]
    record_list = record.split(",")
    record = "Book " + record_list[0] + " BY " + record_list[2] + "\nWrittien in: " + \
             record_list[3] + ", Page count: " + record_list[4] + ".\nPrice: E£ " + record_list[5] + "," + record_list[
                 6] + " copies remaining."
    return record


def view_cart(cur_user):
    cart = cur_user.get_reader_cart()  # tuple like this: [("id", "title", "rent", "19.99")]
    # print (cart[1])
    view = ""

    counter = 0
    global cart_total
    cart_total = 0
    for book in cart:

        rent_or_purchase = ""
        if book[2] == 1:
            rent_or_purchase = "purchase"
        elif book[2] == 2:
            rent_or_purchase = "rent"

        counter = counter + 1
        view = view + "ORDER #" + str(counter) + ":\nBook Title: " + book[1] + ". ID " + str(
            book[0]) + ".\nOption: " + rent_or_purchase + ".\nPrice: E£" + str(book[3]) + ".\n\n"
        cart_total += book[3]

    if cart_total == 0:
        tk.messagebox.showinfo(title=cur_user._username + "'s Cart:", message="Your Cart is Empty")
        return

    if current_user._has_monthly_sub:
        cart_total = cart_total*0.1

    view += "Total = E£" + str(cart_total) + ".\n\n" + "Would You like to checkout now?\n"
    user_input = tk.messagebox.askyesno(title=cur_user._username + "'s Cart:", message=view)
    if user_input:
        NewWindow(root)


#
# def checkout(cur_user):
#     global total
#     total_msg = "Your Total is: " + total + ".\n\nChoose your prefered payment method"

class NewWindow(Toplevel):  # Checkout Window

    def __init__(self, master=None):
        cart = current_user.get_reader_cart()
        global cart_total
        cart_total = 0
        counter = 0

        for book in cart:
            counter = counter + 1
            cart_total += book[3]

        if(current_user._has_monthly_sub):
            cart_total = cart_total*0.1

        ch_total = cart_total
        total_msg = "\nYour Total is: " + str(ch_total) + ".\n\nChoose your prefered payment method"

        super().__init__(master=master)
        self.title("Checkout Page")
        self.geometry("240x240")
        label = Label(self, text=total_msg)
        label.grid(row=0, column=0, padx=10, pady=0)

        v = tk.IntVar()
        v.set(0)  # initializing the choice, i.e. Python

        user_payment_choice = 0

        def ShowChoice():
            global user_payment_choice
            user_payment_choice = v.get()
            return user_payment_choice

        languages = [("Cash", 0), ("Fawry", 1), ("Google Pay", 2), ("Apple Pay", 3)]

        counter = 0
        for language, val in languages:
            counter += 10
            tk.Radiobutton(self, text=language, padx=20, variable=v, command=ShowChoice, value=val).grid(row=counter,
                                                                                                         column=0,
                                                                                                         padx=10,
                                                                                                         pady=0)

        def show_checkout_success():
            payment_choice_arr = payment_options[user_payment_choice]

            order_Number = current_user.checkout(ShowChoice())
            order_Number = str(order_Number)

            if ShowChoice() == 0:
                #print("CASH")
                success_msg = "A total of E£" + str(ch_total) + " will be paid in cash.\n\nYour Order Number Is: " + order_Number + "\.n\nThanks for choosing us! "
            else:
                #print("NOT CASH")
                success_msg = "Connecting to " + payment_options[
                    ShowChoice()] + "'s servers...\n\nPayment Accepted!\n" + "A total of E£" + str(
                    ch_total) + " was deducted from your " + payment_options[ShowChoice()] + " Account.\n\nYour Order Number Is: " + order_Number + "\n\nThanks for choosing us! "

            pmt_suc = tk.messagebox.showinfo(title="Payment Status", message=success_msg)

            current_user.empty_reader_cart()
            cart_total = 0
            if pmt_suc:
                self.destroy()

        proceed_checkout_btn = Button(self, width=10, text='Proceed', font=f, relief=SOLID, cursor='hand2',
                                      command=lambda: show_checkout_success())
        cart_total = 0
        proceed_checkout_btn.grid(row=50, column=0, padx=10, pady=10)


root = Tk()
root.title('Library System Prototype')
root.config(bg='#ccc')
root.geometry("1440x540")
f = ('Times', 14)
var = StringVar()
var.set('male')

# FRAMES DEFINITIONS

first_screen = Frame(root, width=720, height=480, bg='#CCCCCC', relief=SOLID, padx=637, pady=168)
first_screen.grid(row=0, column=0, sticky=W, pady=10)
first_screen.place(relx=0.5, rely=0.5, anchor=CENTER)



reader_login_reg_option = Frame(root, width=720, height=480, bg='#CCCCCC', relief=SOLID, padx=637, pady=200)
reader_login_reg_option.grid(row=0, column=0, sticky=W, pady=10)

reader_register = Frame(root, width=720, height=480, bg='#CCCCCC', relief=SOLID, padx=10, pady=10)
reader_register.grid(row=0, column=0, sticky=W, pady=10)

reader_login = Frame(root, width=720, height=480, bg='#CCCCCC', relief=SOLID, padx=637, pady=190)
reader_login.grid(row=0, column=0, sticky=W, pady=10)

registers_screen = Frame(root, width=720, height=480, bg='#CCCCCC', relief=SOLID, padx=530, pady=100)
registers_screen.grid(row=0, column=0, sticky=W, pady=10)

main_library_screen = Frame(root, width=720, height=480, bg='#CCCCCC', relief=SOLID, padx=10, pady=10)
main_library_screen.grid(row=0, column=0, sticky=W, pady=10)

add_book_screen = Frame(root, width=720, height=480, bg='#CCCCCC', relief=SOLID, padx=10, pady=10)
add_book_screen.grid(row=0, column=0, sticky=W, pady=10)

refresh_frames(first_screen)
Label(first_screen, text="I am:", bg='#CCCCCC', font=f).pack()
Button(first_screen, width=15, text='Reader', font=f, relief=SOLID, cursor='hand2',
       command=lambda: raise_frame(first_screen, reader_login_reg_option, "reader")).pack(pady=10)
Button(first_screen, width=15, text='Librarian', font=f, relief=SOLID, cursor='hand2',
       command=lambda: raise_frame(first_screen, reader_login, "librarian")).pack(pady=10)
Button(first_screen, width=15, text='Admin', font=f, relief=SOLID, cursor='hand2',
       command=lambda: raise_frame(first_screen, reader_login, "admin")).pack(pady=10)

Label(reader_login_reg_option, text="Choose an option", bg='#CCCCCC', font=f).pack()
Button(reader_login_reg_option, width=15, text='Register', font=f, relief=SOLID, cursor='hand2',
       command=lambda: raise_frame(reader_login_reg_option, registers_screen)).pack(pady=10)
Button(reader_login_reg_option, width=15, text='Login', font=f, relief=SOLID, cursor='hand2',
       command=lambda: raise_frame(reader_login_reg_option, reader_login)).pack(pady=10)

# Login
# refresh_frames(reader_login)
Label(reader_login, text="Enter Username", bg='#CCCCCC', font=f).pack()
login_username = Entry(reader_login, font=f)
login_username.pack()

Label(reader_login, text="Enter Password", bg='#CCCCCC', font=f).pack()
login_pass = Entry(reader_login, font=f, show='*')
login_pass.pack()
Login_btn = Button(reader_login, width=15, text='Login', font=f, relief=SOLID, cursor='hand2',
                   command=lambda: login_btn_clicked(login_username, login_pass)).pack(pady=10)

# Register


variable = StringVar()

Label(registers_screen, text="First Name:", bg='#CCCCCC', font=f).grid(row=0, column=0, sticky=W, pady=10)
Label(registers_screen, text="Last Name:", bg='#CCCCCC', font=f).grid(row=1, column=0, sticky=W, pady=10)
Label(registers_screen, text="Date of Birth:", bg='#CCCCCC', font=f).grid(row=2, column=0, sticky=W, pady=10)
Label(registers_screen, text="Location:", bg='#CCCCCC', font=f).grid(row=3, column=0, sticky=W, pady=10)
Label(registers_screen, text="Username:", bg='#CCCCCC', font=f).grid(row=4, column=0, sticky=W, pady=10)
Label(registers_screen, text="Password:", bg='#CCCCCC', font=f).grid(row=5, column=0, sticky=W, pady=10)

register_fname = Entry(registers_screen, font=f)
register_fname.grid(row=0, column=1, pady=10, padx=20)
register_lname = Entry(registers_screen, font=f)
register_lname.grid(row=1, column=1, pady=10, padx=20)
register_dob = Entry(registers_screen, font=f)
register_dob.grid(row=2, column=1, pady=10, padx=20)
register_location = Entry(registers_screen, font=f)
register_location.grid(row=3, column=1, pady=10, padx=20)
register_username = Entry(registers_screen, font=f)
register_username.grid(row=4, column=1, pady=10, padx=20)
register_pwd = Entry(registers_screen, font=f)
register_pwd.grid(row=5, column=1, pady=10, padx=20)

register_btn = Button(registers_screen, width=25, text='Register', font=f, relief=SOLID, cursor='hand2',
                      command=lambda: register_btn_clicked(register_fname, register_lname, register_dob,
                                                           register_location, register_username, register_pwd))
register_btn.grid(row=10, column=0,  pady=20)

# App Main UI

# Search:
Label(main_library_screen, text="Search for Book/Author:", bg='#CCCCCC', font=f).grid(row=0, column=0, padx=10, pady=0)
search_bk = Entry(main_library_screen, font=f)
search_bk.grid(row=1, column=0, padx=10, pady=5)
search_btn = Button(main_library_screen, width=10, text='Search', font=f, relief=SOLID, cursor='hand2',
                    command=lambda: search_result(search_bk))

search_btn.grid(row=5, column=0, padx=10, pady=10)

# LIST OF BOOKS:
columns = ('Title', 'ID', 'Author', 'Written In', 'Page Count', 'Price', 'Available Copies')
tree = ttk.Treeview(main_library_screen, columns=columns, show='headings')

tree.heading('Title', text='Title')
tree.heading('ID', text='ID', anchor="center")
tree.heading('Author', text='Author', anchor="center")
tree.heading('Written In', text='Written In', anchor="center")
tree.heading('Page Count', text='Page Count', anchor="center")
tree.heading('Price', text='Price', anchor="center")
tree.heading('Available Copies', text='Available Copies', anchor="center")

ui_books = load_books()  # Array of Book objects as: Book(_title='The Odyssey', _ID=3, _author='Homer', _release_year='-420', _page_count=2417, _price=499.98, book_count=5)

for Book in ui_books:
    tree.insert('', tk.END, values=(
    Book._title, Book._ID, Book._author, Book._release_year, Book._release_year, Book._price, Book._page_count,
    Book.book_count))


# bind the select event
def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    # reverse sort next time
    tv.heading(col, command=lambda _col=col: treeview_sort_column(tv, _col, not reverse))

for col in columns:
    tree.heading(col, text=col,command=lambda _col=col: treeview_sort_column(tree, _col, False))
def item_selected(event):
    if current_mode == "reader":
        global selected_book
        for selected_item in tree.selection():
            # dictionary

            item = tree.item(selected_item)

            # list
            record = item['values']
            book_name = record[0]
            record = str(record)
            record = processed_book_info(record)
            option = "\n\nWould you like to get this book?"
            box_result1 = tk.messagebox.askyesno(title="Book Information!", message=record + option)

            if box_result1:
                selected_book = search_for_book(book_name)
                #print("SELECTED BOOK " + str(selected_book))
                strin = "Press YES to purchase\nPress NO to rent\nPress CANCEL to return to the main screen"
                box_result2 = tk.messagebox.askyesnocancel(title="Get The Book!", message=strin)

            if box_result2 != None:
                if box_result2:  # Purchase [0]
                    # add_book(self, Book, libId=0):
                    current_user.add_to_cart(selected_book, 1)
                    # print("Purchase")
                    # print(selected_book)
                    tk.messagebox.showinfo(title="Get The Book Now!",
                                           message="Thank You!\nYour Purchase Book is added to the cart.")

                else:
                    # print("Rental")
                    # print(selected_book)
                    current_user.add_to_cart(selected_book, 2)
                    tk.messagebox.showinfo(title="Get The Book Now!",
                                           message="Thank You!\nYour Rental Book is added to the cart.")


tree.bind('<Double-1>', item_selected)  # message box view

tree.grid(row=10, column=0, sticky='nsew')
# scrollbar = ttk.Scrollbar(master=main_library_screen, orient=tk.HORIZONTAL, command=tree.xview)
# tree.configure(xscroll=scrollbar.set)
# scrollbar.grid(row=10, column=0, sticky='s')

view_cart_btn = Button(main_library_screen, width=10, text='View Cart', font=f, relief=SOLID, cursor='hand2',
                       command=lambda: view_cart(current_user))
view_cart_btn.grid(row=20, column=0, padx=10, pady=10)
checkout_btn = Button(main_library_screen, width=10, text='Checkout', font=f, relief=SOLID, cursor='hand2',
                      command=lambda: None)
checkout_btn.grid(row=25, column=0, padx=10, pady=10)
checkout_btn.bind("<Button>", lambda e: NewWindow(root))

lib_label = Label(main_library_screen, text="Search with Order Code:", bg='#CCCCCC', font=f)
lib_label.grid(row=30, column=0, padx=10, pady=0)

search_ord_id_bk = Entry(main_library_screen, font=f)

search_order_entry = Entry(main_library_screen, font=f)
search_order_entry.grid(row=31, column=0, padx=10, pady=5)
search_ord_id_btn = Button(main_library_screen, width=20, text='View Order', font=f, relief=SOLID, cursor='hand2',
                           command=lambda: search_orders(search_order_entry.get()))

search_ord_id_btn.grid(row=35, column=0, padx=10, pady=10)

admin_add_book_btn = Button(main_library_screen, width=15, text='Add Book', font=f, relief=SOLID, cursor='hand2',
                            command=lambda: raise_frame_no_dest(main_library_screen, add_book_screen))

admin_add_book_btn.grid(row=35, column=0, padx=10, pady=10)

remove_book_entry = Label(main_library_screen, text="Book Name to Remove:", bg='#CCCCCC', font=f)
remove_book_entry.grid(row=36, column=0, padx=10, pady=0)
bk_rm_entry = Entry(main_library_screen, font=f)
bk_rm_entry.grid(row=37, column=0, padx=0, pady=5)
admin_rm_book_btn = Button(main_library_screen, width=15, text='Remove Book', font=f, relief=SOLID, cursor='hand2',
                           command=lambda: rm_book(bk_rm_entry))

admin_rm_book_btn.grid(row=38, column=0, padx=0, pady=0)

Label(add_book_screen, text="Book Name:", bg='#CCCCCC', font=f).grid(row=0, column=0, sticky=W, pady=10)
Label(add_book_screen, text="Book ID:", bg='#CCCCCC', font=f).grid(row=1, column=0, sticky=W, pady=10)
Label(add_book_screen, text="Author Name:", bg='#CCCCCC', font=f).grid(row=2, column=0, sticky=W, pady=10)
Label(add_book_screen, text="Date Written in:", bg='#CCCCCC', font=f).grid(row=3, column=0, sticky=W, pady=10)
Label(add_book_screen, text="Page Count:", bg='#CCCCCC', font=f).grid(row=4, column=0, sticky=W, pady=10)
Label(add_book_screen, text="Price:", bg='#CCCCCC', font=f).grid(row=5, column=0, sticky=W, pady=10)
Label(add_book_screen, text="Available Copies:", bg='#CCCCCC', font=f).grid(row=6, column=0, sticky=W, pady=10)

addb_bname = Entry(add_book_screen, font=f)
addb_bname.grid(row=0, column=1, pady=10, padx=20)

addb_bid = Entry(add_book_screen, font=f)
addb_bid.grid(row=1, column=1, pady=10, padx=20)

addb_bauthor = Entry(add_book_screen, font=f)
addb_bauthor.grid(row=2, column=1, pady=10, padx=20)

addb_bwdate = Entry(add_book_screen, font=f)
addb_bwdate.grid(row=3, column=1, pady=10, padx=20)

addb_bpcount = Entry(add_book_screen, font=f)
addb_bpcount.grid(row=4, column=1, pady=10, padx=20)

addb_bprice = Entry(add_book_screen, font=f)
addb_bprice.grid(row=5, column=1, pady=10, padx=20)

addb_bcopies = Entry(add_book_screen, font=f)
addb_bcopies.grid(row=6, column=1, pady=10, padx=20)

admin_add_book_final_btn = Button(add_book_screen, width=15, text='Add Book', font=f, relief=SOLID, cursor='hand2',
                                  command=lambda: add_book_btn_clicked(addb_bname, addb_bid, addb_bauthor, addb_bwdate,
                                                                       addb_bpcount, addb_bprice, addb_bcopies))

admin_add_book_final_btn.grid(row=36, column=0, padx=10, pady=0)

first_screen.tkraise()
root.mainloop()

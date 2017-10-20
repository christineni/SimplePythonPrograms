import tkinter
import sqlite3
import os
import tkinter.ttk

__author__ = 'cni12345'

# Global variable for the database object so that it can be referenced by all functions
db = None    # Initialized to None, and set in the main function


class DBBrowser:
    def __init__(self, rows):
        # Define the main window that contains the widgets
        self.main_window = tkinter.Tk()
        self.main_window.title("Book Browser")
        self.main_window.configure(background='lavender')

        selectfont = ('times', 9, 'italic bold')

        # Define the 'Select Column' Label and the ComboBox with values for each column in the BOOK table
        self.selectColumn_label = tkinter.Label(self.main_window, text='Select Column', bg='lavender', font=selectfont)\
            .grid(row=0, column=0)
        self.box_value = tkinter.StringVar()
        self.box = tkinter.ttk.Combobox(self.main_window, textvariable=self.box_value)
        # When a new value is selected in the ComboBox, call the newselection function
        self.box.bind("<<ComboboxSelected>>", self.newselection)
        self.box['values'] = ('ISBN', 'Title', 'Author', 'Publisher', 'Format', 'Subject')
        self.box.grid(row=0, column=1)
        self.box.current(0)
        self.value_of_combo = 'ISBN'

        # Define the 'Search column' Button and Entry field that contains the value to search the database
        self.searchvalue = tkinter.StringVar()
        tkinter.Button(self.main_window, text='Search column', bg='pink', command=self.search_db).grid(row=0, column=2)
        self.searchterm_entry = tkinter.Entry(self.main_window, textvariable=self.searchvalue).grid(row=0, column=3)

        # Define the 'Sort column' Button
        tkinter.Button(self.main_window, text='Sort column', bg='pink', command=self.sort_db).grid(row=0, column=4)

        labelfont = ('times', 12, 'bold underline')
        # Define the column labels (headings)
        try:
            r = 1
            cols = ['ISBN', 'Title', 'Author', 'Publisher', 'Format', 'Subject']
            tkinter.Label(self.main_window, text=cols[0], fg='dark blue', bg='lavender', font=labelfont).grid(row=r, column=0)
            tkinter.Label(self.main_window, text=cols[1], fg='dark blue', bg='lavender', font=labelfont).grid(row=r, column=1)
            tkinter.Label(self.main_window, text=cols[2], fg='dark blue', bg='lavender', font=labelfont).grid(row=r, column=2)
            tkinter.Label(self.main_window, text=cols[3], fg='dark blue', bg='lavender', font=labelfont).grid(row=r, column=3)
            tkinter.Label(self.main_window, text=cols[4], fg='dark blue', bg='lavender', font=labelfont).grid(row=r, column=4)
            tkinter.Label(self.main_window, text=cols[5], fg='dark blue', bg='lavender', font=labelfont).grid(row=r, column=5)

            # Call display_rows function to display the contents of the BOOK table when the GUI is initially created
            self.display_rows(rows)

            tkinter.mainloop()

        except Exception as err:
            print('An error occurred: ', err)

    # When a new value is selected in the ComboBox, this function is called to get the value
    def newselection(self, event):
        self.value_of_combo = self.box.get()
        print(self.value_of_combo)

    def display_rows(self, rows):
        # Clear the previous rows of data before displaying results of the current search
        r = 2
        for label in self.main_window.grid_slaves():
            if int(label.grid_info()["row"]) >= 2:
                label.grid_forget()

        # Loop through the rows and display the data in Label widgets in the grid layout
        for a_row in rows:
            for i in a_row:
                tkinter.Label(self.main_window, text=a_row[0], bg='lavender').grid(row=r, column=0)
                tkinter.Label(self.main_window, text=a_row[1], bg='lavender').grid(row=r, column=1)
                tkinter.Label(self.main_window, text=a_row[2], bg='lavender').grid(row=r, column=2)
                tkinter.Label(self.main_window, text=a_row[3], bg='lavender').grid(row=r, column=3)
                tkinter.Label(self.main_window, text=a_row[4], bg='lavender').grid(row=r, column=4)
                tkinter.Label(self.main_window, text=a_row[5], bg='lavender').grid(row=r, column=5)
            r += 1
        # If there are no rows, this means the search did not return any results
        # Display a message indicating "No results were found"
        if len(rows) < 1:
            tkinter.Label(self.main_window, text='No results were found', bg='lavender').grid(row=r, column=0)

        # For debugging purposes, display results to the console
        # for a_row in rows:
        # print(a_row)

    # This function uses 2 values to formulate the query to search the database:
    #   1) Value entered in the 'Search column' entry field
    #   2) The table column name that corresponds to the selection from the ComboBox
    # Example query: Find all books with a subject of biography
    # SQL for this query is SELECT * FROM BOOK WHERE Subject LIKE "%biography%"
    def search_db(self):
        global db
        try:
            cursor = db.cursor()
            # Get the value entered in the 'Search column' entry field
            search = self.searchvalue.get()
            # Get the ComboBox selection
            combo = self.box.get()
            # Formulate the query with these values. If no 'Search' entry specified, retrieve all rows
            if search == '':
                sql = 'SELECT * FROM BOOK'
            elif combo == 'ISBN':
                sql = 'SELECT * FROM BOOK WHERE ISBN LIKE "%' + search + '%"'
            elif combo == 'Title':
                sql = 'SELECT * FROM BOOK WHERE Title LIKE "%' + search + '%"'
            elif combo == 'Author':
                sql = 'SELECT * FROM BOOK WHERE Author LIKE "%' + search + '%"'
            elif combo == 'Publisher':
                sql = 'SELECT * FROM BOOK WHERE Publisher LIKE "%' + search + '%"'
            elif combo == 'Format':
                sql = 'SELECT * FROM BOOK WHERE Format LIKE "%' + search + '%"'
            elif combo == 'Subject':
                sql = 'SELECT * FROM BOOK WHERE Subject LIKE "%' + search + '%"'

        # Execute the query and use the fetchall function to obtain the rows in the result, rows = cursor.fetchall()
            cursor.execute(sql)
        # Call display_rows function to display the results of the query
            rows = cursor.fetchall()
            self.display_rows(rows)

        except sqlite3.IntegrityError as err:
            print('Integrity Error on select:', err)
        except sqlite3.OperationalError as err:
            print('Operational Error on select:', err)
        except sqlite3.Error as err:
            print('Error on select:', err)

    # This function uses the table column name that was selected from the ComboBox to sort the database on that column
    # Example query: Sort books based on Title
    # SQL for this query is SELECT * FROM BOOK ORDER BY Title
    def sort_db(self):
        global db
        try:
            cursor = db.cursor()
            # Get the value of the ComboBox selection
            combo = self.box.get()
            # Formulate the query with this value
            if combo == 'ISBN':
                sql = 'SELECT * FROM BOOK ORDER BY ISBN'
            elif combo == 'Title':
                sql = 'SELECT * FROM BOOK ORDER BY Title'
            elif combo == 'Author':
                sql = 'SELECT * FROM BOOK ORDER BY Author'
            elif combo == 'Publisher':
                sql = 'SELECT * FROM BOOK ORDER BY Publisher'
            elif combo == 'Format':
                sql = 'SELECT * FROM BOOK ORDER BY Format'
            elif combo == 'Subject':
                sql = 'SELECT * FROM BOOK ORDER BY Subject'

            # Execute the query with the fetchall function
            cursor.execute(sql)
            # Call display_rows function to display the results of the query
            rows = cursor.fetchall()
            self.display_rows(rows)

        except sqlite3.IntegrityError as err:
            print('Integrity Error on select:', err)
        except sqlite3.OperationalError as err:
            print('Operational Error on select:', err)
        except sqlite3.Error as err:
            print('Error on select:', err)


# The main function connects to the database and executes a query to retrieve all of the rows in the BOOK table.
# An instance of the DB_Browser GUI is created and the rows are passed to the GUI for initial display of the BOOK table contents
def main():
    global db
    try:
        dbname = 'books.db'
        if os.path.exists(dbname):
            db = sqlite3.connect(dbname)
            cursor = db.cursor()
            sql = 'SELECT * FROM BOOK'
            cursor.execute(sql)
            rows = cursor.fetchall()
            DBBrowser(rows)
            db.close()
        else:
            print('Error:', dbname, 'does not exist')
    except sqlite3.IntegrityError as err:
        print('Integrity Error on connect:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error on connect:', err)
    except sqlite3.Error as err:
        print('Error on connect:', err)

main()

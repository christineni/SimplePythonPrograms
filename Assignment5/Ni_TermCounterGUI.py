import string
import tkinter
import tkinter.filedialog

__author__ = 'cni12345'
file_open = ''


class FileEditor:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window. title('Term Counter')
        self.main_window.geometry('600x150')
        self.main_window.configure(background='lavender')

        # Create four frames to group widgets.
        self.open_frame = tkinter.Frame()
        self.search_frame = tkinter.Frame()
        self.count_frame = tkinter.Frame()
        self.quit_frame = tkinter.Frame()

        # Create the widgets for the open frame.
        self.select = tkinter.Button(self.open_frame, text='Select a File', bg='green', command=self.open_file)
        self.name_value = tkinter.StringVar()
        self.type_label = tkinter.Label(self.open_frame, textvariable=self.name_value)

        # Pack the open frame's widgets.
        self.select.pack(side='left')
        self.type_label.pack(side='left')

        # Create the widgets for the search frame.
        self.search_label = tkinter.Label(self.search_frame, text='Enter a search term:   ', bg='lavender')
        self.entry = tkinter.Entry(self.search_frame, width=10)

        # Pack the search frame's widgets.
        self.search_label.pack(side='left')
        self.entry.pack(side='left')

        # Create the widgets for the count frame.
        self.count = tkinter.Button(self.count_frame, text='Count Terms', bg='green', command=self.count_terms)
        self.count_value = tkinter.StringVar()
        self.count_label = tkinter.Label(self.count_frame, textvariable=self.count_value)

        # Pack the count frame's widgets.
        self.count.pack(side='left')
        self.count_label.pack(side='left')

        # Create the widgets for the quit frame.
        self.quit = tkinter.Button(self.quit_frame, text='Quit', bg='green', command=self.main_window.destroy)

        # Pack the quit button.
        self.quit.pack(side='left')

        # Pack the frames.
        self.open_frame.pack()
        self.search_frame.pack()
        self.count_frame.pack()
        self.quit_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # Function to open text file.
    def open_file(self):
        global file_open
        file_open = tkinter.filedialog.askopenfilename()
        self.name_value.set(file_open)

    # Function to search a term and count the number of occurrences.
    def count_terms(self):
        count = 0
        try:
            # Get the name of the open file.
            infile = self.name_value.get()
            f = open(infile, "r")
            content = f.readlines()

            # Search for term.
            search = self.entry.get()

            if search == '':
                self.count_value.set("Enter a search term")
            else:
                for words in content:
                    txt = remove_punctuation(words)
                    for j in txt:
                        if j == search:
                            count += 1
                return self.count_value.set("'" + search + "'" + " occurs " + str(count) + " times.")

        except OSError:
            self.name_value.set("Select a file to search")
        except Exception as error:
            print(error)


def remove_punctuation(text):
    clean_words = []  # create an empty list
    text = text.rstrip()  # remove trailing whitespace characters
    words = text.split()  # create a list of words from the text
    for word in words:  # normalize and add to list
        clean_words.append(word.strip(string.punctuation).lower())
    return clean_words

FileEditor()  # Create GUI

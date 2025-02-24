
from tkinter import Menu, StringVar, Tk
from tkinter.ttk import Button, Entry, Frame, Label, Style


def grid(widget, row, column, row_span=1, column_span=1, **kwargs):
    widget.grid(
        row=row,
        column=column,
        rowspan=row_span,
        columnspan=column_span,
        **kwargs,
    )


class SqliteBrowser(Tk):

    def __init__(self):
        super().__init__()

        self.style = Style(self)
        self.style.theme_use('clam')
        self.title('SQLite Browser')
        self.build_menus()

        # top_level = self.winfo_toplevel()
        # top_level.geometry('600x400')

        root_frame = Frame(self, padding=10)
        root_frame.grid()

        self.database_var = StringVar()
        self.database_var.set("Some database file")

        grid(Label(root_frame, text="Database"), 0, 0)
        grid(Entry(root_frame, textvariable=self.database_var), 0, 1)
        grid(Button(root_frame, text="browse"), 0, 2)

        self.root_frame = root_frame

    def build_menus(self):
        self.option_add('*tearOff', False)

        menubar = Menu(self)
        self['menu'] = menubar

        file_menu = Menu(menubar)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        edit_menu = Menu(menubar)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label='Cut', command=self.cut)
        edit_menu.add_command(label='')

    def open_file(self):
        print("open_file")

    def save_file(self):
        print('save_file')

    def cut(self):
        print('cut')

    def copy(self):
        print('copy')

    def paste(self):
        print('paste')

    @staticmethod
    def grid(widget, row, column, row_span=1, column_span=1, **kwargs):
        widget.grid(
            row=row,
            column=column,
            rowspan=row_span,
            columnspan=column_span,
            **kwargs,
        )


def main():
    browser = SqliteBrowser()
    browser.mainloop()


if __name__ == '__main__':
    main()

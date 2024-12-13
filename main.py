import tkinter as tk

from bd import mydb
from gui import mygui

if __name__ == "__main__":
    index_files = {
        "SN": "index_sn.csv",
        "Name": "index_name.csv",
        "Date": "index_date.csv",
        "Compliance Index": "index_compliance_index.csv",
        "Sold": "index_sold.csv",
        "Removed": "removed.txt"
    }
    # объект бд
    db = mydb.create_empty()

    root = tk.Tk()
    gui = mygui(root, db)

    root.mainloop()
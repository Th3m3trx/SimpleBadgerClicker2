import tkinter as tk

class BadgerClickerGame:
    def __init__(self):
        self.badger_count = 0
        self.total_clicks = 0
        self.item1_count = 0
        self.item2_count = 0

        # Create the main window
        self.main_window = tk.Tk()
        self.main_window.title("Badger Clicker")

        # Create labels for main window
        self.badger_count_label = tk.Label(self.main_window, text="Badger count: 0")
        self.badger_count_label.pack()

        self.total_clicks_label = tk.Label(self.main_window, text="Total clicks: 0")
        self.total_clicks_label.pack()

        # Create buttons for main window
        self.badger_button = tk.Button(self.main_window, text="Click the Badger!", command=self.click_badger)
        self.badger_button.pack()

        self.reset_button = tk.Button(self.main_window, text="Reset", command=self.reset_game)
        self.reset_button.pack()

        # Create buttons to open seperate windpws
        self.stats_button = tk.Button(self.main_window, text="View Statistics", command=self.open_stats_window)
        self.stats_button.pack()

        self.shop_button = tk.Button(self.main_window, text="Visit Shop", command=self.open_shop_window)
        self.shop_button.pack()

        # Create seperate windows
        self.stats_window = None
        self.shop_window = None

        # Create the main loop
        self.main_window.mainloop()

        # Create counter for stats window
    def click_badger(self):
        self.badger_count += 1
        self.total_clicks += 1
        self.badger_count_label["text"] = "Badger count: " + str(self.badger_count)
        self.total_clicks_label["text"] = "Total clicks: " + str(self.total_clicks)

        # Create a reset feature 
    def reset_game(self):
        self.badger_count = 0
        self.total_clicks = 0
        self.badger_count_label["text"] = "Badger count: 0"
        self.total_clicks_label["text"] = "Total clicks: 0"

        # Ceate the stats window and create labels for it
    def open_stats_window(self):
        if self.stats_window is None or not self.stats_window.winfo_exists():
            self.stats_window = tk.Toplevel(self.main_window)
            self.stats_window.title("Statistics")

            stats_label = tk.Label(self.stats_window, text="Badger count: " + str(self.badger_count) + "\nTotal clicks: " + str(self.total_clicks) +
                                             "\nTough Badger count: " + str(self.item1_count) + "\nGolden Badger count: " + str(self.item2_count))
            stats_label.pack()

            # reate the shop window and create labels and buttons for it
    def open_shop_window(self):
        if self.shop_window is None or not self.shop_window.winfo_exists():
            self.shop_window = tk.Toplevel(self.main_window)
            self.shop_window.title("Shop")

            item_label = tk.Label(self.shop_window, text="Items:")
            item_label.pack()

            item1_button = tk.Button(self.shop_window, text="Tough Badger (10 Badgers)", command=self.buy_item1)
            item1_button.pack()

            item2_button = tk.Button(self.shop_window, text="Golden Badger (20 Badgers)", command=self.buy_item2)
            item2_button.pack()

            # Create the name and data for the first item
    def buy_item1(self):
        if self.badger_count >= 10:
            self.badger_count -= 10
            self.item1_count += 1
            self.badger_count_label["text"] = "Badger count: " + str(self.badger_count)
            self.update_stats_window()
            print("Tough Badger purchased!")
        else:
            print("Not enough badgers to buy Tough Badger!")

            # Create the name and data for the second item
    def buy_item2(self):
        if self.badger_count >= 20:
            self.badger_count -= 20
            self.item2_count += 1
            self.badger_count_label["text"] = "Badger count: " + str(self.badger_count)
            self.update_stats_window()
            print("Item 2 purchased!")
        else:
            print("Not enough badgers to buy Item 2!")

           # Create and updater to change the stats window according to the data
    def update_stats_window(self):
        if self.stats_window is not None and self.stats_window.winfo_exists():
            stats_label = tk.Label(self.stats_window, text="Badger count: " + str(self.badger_count) + "\nTotal clicks: " + str(self.total_clicks))
            stats_label.pack()

            item1_label = tk.Label(self.stats_window, text="Tough Badger count: " + str(self.item1_count))
            item1_label.pack()

            item2_label = tk.Label(self.stats_window, text="Golden Badger2 count: " + str(self.item2_count))
            item2_label.pack()

# Create an instance of the game
game = BadgerClickerGame()

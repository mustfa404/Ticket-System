import tkinter as tk

from ticket_queue_gui import TicketQueueGUI


if __name__ == "__main__":
    root = tk.Tk()
    app = TicketQueueGUI(root)
    root.mainloop()

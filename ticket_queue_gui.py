import tkinter as tk
from tkinter import messagebox

from ticket_queue import TicketQueue


class TicketQueueGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket Queue System")
        self.root.minsize(600, 400)
        self.root.resizable(True, True)
        self.root.configure(bg="#f5f5f5")
        self.queue_system = TicketQueue()

        self._build_ui()

    def _build_ui(self):
        self._build_title()
        self._build_input_frame()
        self._build_buttons_frame()
        self._build_display_frame()

    def _build_title(self):
        tk.Label(
            self.root,
            text="Ticket Reservation Management",
            font=("Helvetica", 24, "bold"),
            bg="#f5f5f5",
            fg="#333333",
        ).pack(pady=20)

    def _build_input_frame(self):
        input_frame = tk.Frame(self.root, bg="#f5f5f5")
        input_frame.pack(pady=10)

        tk.Label(
            input_frame,
            text="Customer Name(s):",
            font=("Helvetica", 14),
            bg="#f5f5f5",
            fg="#555555",
        ).grid(row=0, column=0, padx=10, pady=10)

        self.name_entry = tk.Entry(input_frame, width=30, font=("Helvetica", 14))
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(
            input_frame,
            text="Add Customer(s)",
            command=self.add_customers,
            font=("Helvetica", 12),
            bg="#4caf50",
            fg="white",
            relief="raised",
            bd=2,
        ).grid(row=0, column=2, padx=10, pady=10)

    def _build_buttons_frame(self):
        buttons_frame = tk.Frame(self.root, bg="#f5f5f5")
        buttons_frame.pack(pady=20)

        tk.Button(
            buttons_frame,
            text="Issue All Tickets",
            command=self.issue_all_tickets,
            font=("Helvetica", 12),
            bg="#2196f3",
            fg="white",
            relief="raised",
            bd=2,
        ).grid(row=0, column=0, padx=10, pady=10)

        tk.Button(
            buttons_frame,
            text="Cancel Ticket",
            command=self.cancel_ticket,
            font=("Helvetica", 12),
            bg="#f44336",
            fg="white",
            relief="raised",
            bd=2,
        ).grid(row=0, column=1, padx=10, pady=10)

    def _build_display_frame(self):
        display_frame = tk.Frame(self.root, bg="#f5f5f5")
        display_frame.pack(pady=20)

        self.queue_label = tk.Label(
            display_frame,
            text="Queue: []",
            font=("Helvetica", 14),
            bg="#f5f5f5",
            fg="#333333",
        )
        self.queue_label.pack()

        self.tickets_label = tk.Label(
            display_frame,
            text="Issued Tickets: {}",
            font=("Helvetica", 14),
            bg="#f5f5f5",
            fg="#333333",
        )
        self.tickets_label.pack()

    def update_display(self):
        self.queue_label.config(text=f"Queue: {self.queue_system.display_queue()}")
        self.tickets_label.config(text=f"Issued Tickets: {self.queue_system.display_tickets()}")

    def add_customers(self):
        names = self.name_entry.get().split(",")
        names = [name.strip() for name in names if name.strip()]
        if not names:
            messagebox.showerror("Input Error", "Please enter at least one name.")
            return
        self.queue_system.add_customer(*names)
        self.update_display()
        self.name_entry.delete(0, tk.END)

    def issue_all_tickets(self):
        if not self.queue_system.queue:
            messagebox.showinfo("No Customers", "No customers in the queue to issue tickets.")
            return
        self.queue_system.issue_all_tickets()
        self.update_display()

    def cancel_ticket(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Input Error", "Please enter a name to cancel.")
            return
        try:
            self.queue_system.cancel_ticket(name)
            self.update_display()
        except ValueError as e:
            messagebox.showerror("Cancel Error", str(e))
        finally:
            self.name_entry.delete(0, tk.END)  # Always clear input

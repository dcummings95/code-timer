import tkinter as tk
from datetime import datetime, timedelta

class CodingTimerApp:
    def __init__(self, root):
        # Main app window setup
        self.root = root
        self.root.title("Coding Timer")
        
        # Variables to keep track of start time and elapsed time
        self.start_time = None
        self.elapsed_time = timedelta(0)
        
        # Setting up the timer display
        self.timer_var = tk.StringVar()
        self.update_display()
        self.timer_label = tk.Label(root, textvariable=self.timer_var, font=("Arial", 24))
        self.timer_label.pack(pady=20)
        
        # Start and Stop buttons
        self.start_button = tk.Button(root, text="Start", command=self.start_timer, bg="green", fg="white")
        self.start_button.pack(side="left", padx=20)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, bg="red", fg="white")
        self.stop_button.pack(side="right", padx=20)
        
        # To periodically update the timer display when it's running
        self.update_timer()

    def update_display(self):
        # Convert timedelta to hours:minutes:seconds format
        hours, remainder = divmod(self.elapsed_time.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        self.timer_var.set(f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}")
        
    def start_timer(self):
        self.start_time = datetime.now()
        self.update_timer()
        
    def stop_timer(self):
        if self.start_time:
            self.elapsed_time += datetime.now() - self.start_time
            self.start_time = None
            self.update_display()
            
    def update_timer(self):
        # If the timer is running, update the display every second
        if self.start_time:
            self.elapsed_time += datetime.now() - self.start_time
            self.start_time = datetime.now()
            self.update_display()
            self.root.after(1000, self.update_timer)
            
root = tk.Tk()
app = CodingTimerApp(root)
root.mainloop()
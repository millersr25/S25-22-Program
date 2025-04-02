import tkinter as tk
from tkinter import ttk
import random
import time

# Matplotlib imports for embedding the voltage plot in the GUI
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create main window
root = tk.Tk()
root.title("Satellite Solar Energy Harvester Monitor")
root.geometry("700x500")

# Create a top frame for sensor values
top_frame = tk.Frame(root, padx=10, pady=10)
top_frame.pack(side=tk.TOP, fill="x")

# Battery Charge Level (Label + Progress Bar)
tk.Label(top_frame, text="Battery Charge Level:").grid(row=0, column=0, sticky="w")
charge_percentage = tk.StringVar(value="0%")
tk.Label(top_frame, textvariable=charge_percentage, width=8).grid(row=0, column=1, sticky="w")
charge_progress = ttk.Progressbar(top_frame, orient="horizontal", length=200, mode="determinate", maximum=100)
charge_progress.grid(row=0, column=2, padx=10)

# Battery Voltage
tk.Label(top_frame, text="Battery Voltage:").grid(row=1, column=0, sticky="w")
voltage_val = tk.StringVar(value="0.00 V")
tk.Label(top_frame, textvariable=voltage_val, width=10).grid(row=1, column=1, sticky="w")

# Battery Current
tk.Label(top_frame, text="Battery Current:").grid(row=2, column=0, sticky="w")
current_val = tk.StringVar(value="0.0 mA")
label_current_val = tk.Label(top_frame, textvariable=current_val, width=10)
label_current_val.grid(row=2, column=1, sticky="w")

# System Temperature
tk.Label(top_frame, text="System Temperature:").grid(row=3, column=0, sticky="w")
temp_val = tk.StringVar(value="0.0 °C")
tk.Label(top_frame, textvariable=temp_val, width=10).grid(row=3, column=1, sticky="w")

# Solar Panel Voltage Input
tk.Label(top_frame, text="Solar Panel Voltage:").grid(row=4, column=0, sticky="w")
panel_val = tk.StringVar(value="0.00 V")
tk.Label(top_frame, textvariable=panel_val, width=10).grid(row=4, column=1, sticky="w")

# System Status (Text + Visual Indicator)
tk.Label(top_frame, text="System Status:").grid(row=5, column=0, sticky="w")
status_val = tk.StringVar(value="Normal")
tk.Label(top_frame, textvariable=status_val, width=12).grid(row=5, column=1, sticky="w")
status_canvas = tk.Canvas(top_frame, width=25, height=25, highlightthickness=0)
status_canvas.grid(row=5, column=2, padx=10)
status_circle = status_canvas.create_oval(2, 2, 23, 23, fill="green")

# Define status code mappings (dummy mapping)
STATUS_CODES = {
    0: ("Normal", "green"),
    1: ("Charging", "blue"),
    2: ("Over-voltage", "red"),
    3: ("Under-voltage", "orange"),
    4: ("Over-current", "red"),
    5: ("Over-temperature", "red")
}

def update_status_indicator(color):
    """Update the color of the status circle."""
    status_canvas.itemconfig(status_circle, fill=color)

# ---------------------------
# Voltage tracking over time setup
# ---------------------------
start_time = time.time()
time_data = []
voltage_data = []

# Create a frame for the plot
plot_frame = tk.Frame(root)
plot_frame.pack(side=tk.BOTTOM, fill="both", expand=True)

# Create a matplotlib Figure and a subplot for voltage tracking
fig = Figure(figsize=(6, 3), dpi=100)
ax = fig.add_subplot(111)
ax.set_title("Battery Voltage Over Time")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Voltage (V)")
line, = ax.plot([], [], marker='o', linestyle='-')

# Create a canvas widget for the figure
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.get_tk_widget().pack(fill="both", expand=True)
canvas.draw()

# ---------------------------
# Dummy data update function (simulating sensor readings)
# ---------------------------
def update_dummy_data():
    # Simulate dummy sensor values
    charge = random.uniform(20, 90)
    voltage = random.uniform(4.0, 4.4)
    current = random.uniform(-600, 600)
    temperature = random.uniform(10, 35)
    panel_voltage = random.uniform(1.0, 2.0)
    status_code = random.choice(list(STATUS_CODES.keys()))
    
    # Update display values
    charge_percentage.set(f"{charge:.1f}%")
    charge_progress['value'] = charge
    voltage_val.set(f"{voltage:.2f} V")
    current_val.set(f"{current:.1f} mA")
    temp_val.set(f"{temperature:.1f} °C")
    panel_val.set(f"{panel_voltage:.2f} V")
    
    status_text, color = STATUS_CODES.get(status_code, ("Unknown", "gray"))
    status_val.set(status_text)
    update_status_indicator(color)
    label_current_val.config(fg="red" if current < 0 else "green")
    
    # Track voltage over time
    elapsed_time = time.time() - start_time
    time_data.append(elapsed_time)
    voltage_data.append(voltage)
    
    # Update the plot with the new data
    line.set_data(time_data, voltage_data)
    ax.relim()
    ax.autoscale_view()
    canvas.draw()
    
    # Schedule next update (every 10 second)
    root.after(10000, update_dummy_data)


# Start the dummy update loop
root.after(1000, update_dummy_data)

# Run the GUI main loop
root.mainloop()

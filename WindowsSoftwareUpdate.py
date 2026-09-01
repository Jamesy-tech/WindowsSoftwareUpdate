import tkinter as tk
import random
import winsound

class WindowsSoftwareUpdate:

    def __init__(self, root):

        winsound.MessageBeep(winsound.MB_OK)

        self.root = root
        self.root.title("Windows Software Update")
        self.root.geometry("720x460")
        self.root.resizable(False, False)
        self.root.configure(bg="#f7f7f7")

        self.blue = "#0067c0"
        self.text = "#202020"
        self.gray = "#666666"

        self.step = 0
        self.progress_value = 0
        self.progress_points = []

        self.steps = [
            {
                "title": "Checking for updates",
                "description": "Checking for available software updates"
            },
            {
                "title": "Downloading updates",
                "description": "Downloading required software components"
            },
            {
                "title": "Preparing installation",
                "description": "Preparing downloaded files for installation"
            },
            {
                "title": "Installing updates",
                "description": "Installing software update components"
            },
            {
                "title": "Checking system security",
                "description": "Performing final security and integrity checks"
            }
        ]

        self.build_welcome()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def header(self):
        frame = tk.Frame(self.root, bg="white", height=70)
        frame.pack(fill="x")

        tk.Label(
            frame,
            text="Windows Software Update",
            font=("Segoe UI", 15),
            fg=self.text,
            bg="white"
        ).pack(side="left", padx=30, pady=20)

    def build_welcome(self):
        self.clear()
        self.header()

        tk.Label(
            self.root,
            text="Welcome to Windows Software Update",
            font=("Segoe UI", 22),
            fg=self.text,
            bg="#f7f7f7"
        ).pack(pady=(55, 15))

        tk.Label(
            self.root,
            text="Windows Software Update will check your device for "
                 "available updates and prepare them for installation.",
            font=("Segoe UI", 11),
            fg=self.gray,
            bg="#f7f7f7",
            wraplength=560,
            justify="center"
        ).pack()

        tk.Label(
            self.root,
            text="Make sure your device remains powered on",
            font=("Segoe UI", 10),
            fg="#777777",
            bg="#f7f7f7"
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="Continue",
            command=self.start_update,
            bg=self.blue,
            fg="white",
            activebackground="#005a9e",
            activeforeground="white",
            relief="flat",
            font=("Segoe UI", 10),
            padx=25,
            pady=8,
            cursor="hand2"
        ).pack(pady=25)

    def start_update(self):
        self.step = 0
        self.show_step()

    def show_step(self):
        self.clear()
        self.header()

        current = self.steps[self.step]

        tk.Label(
            self.root,
            text=current["title"],
            font=("Segoe UI", 21),
            fg=self.text,
            bg="#f7f7f7"
        ).pack(pady=(55, 10))

        tk.Label(
            self.root,
            text=current["description"],
            font=("Segoe UI", 10),
            fg=self.gray,
            bg="#f7f7f7"
        ).pack()

        self.progress_canvas = tk.Canvas(
            self.root,
            width=560,
            height=8,
            bg="#dddddd",
            highlightthickness=0
        )
        self.progress_canvas.pack(pady=(40, 10))

        self.progress_bar = self.progress_canvas.create_rectangle(
            0, 0, 0, 8,
            fill=self.blue,
            outline=""
        )

        self.percent_label = tk.Label(
            self.root,
            text="0%",
            font=("Segoe UI", 10),
            fg=self.gray,
            bg="#f7f7f7"
        )
        self.percent_label.pack()

        self.status_label = tk.Label(
            self.root,
            text="Starting...",
            font=("Segoe UI", 9),
            fg="#777777",
            bg="#f7f7f7"
        )
        self.status_label.pack(pady=15)

        tk.Label(
            self.root,
            text=f"Step {self.step + 1} of {len(self.steps)}",
            font=("Segoe UI", 9),
            fg="#999999",
            bg="#f7f7f7"
        ).pack(side="bottom", pady=20)

        self.progress_value = 0
        self.progress_points = self.generate_progress_points()

        self.update_progress()

    def generate_progress_points(self):
        point_count = random.randint(3, 7)

        points = sorted(
            random.sample(
                range(1, 100),
                point_count - 1
            )
        )

        points.append(100)

        return points

    def update_progress(self):
        if not self.progress_points:
            self.next_step()
            return

        self.progress_value = self.progress_points.pop(0)

        width = 560 * (self.progress_value / 100)

        self.progress_canvas.coords(
            self.progress_bar,
            0, 0,
            width, 8
        )

        self.percent_label.config(
            text=f"{self.progress_value}%"
        )

        messages = [
            "Working...",
            "Processing files...",
            "Verifying components...",
            "Checking integrity...",
            "Applying update...",
            "Please wait..."
        ]

        self.status_label.config(
            text=random.choice(messages)
        )

        if self.progress_value >= 100:
            self.root.after(
                random.randint(150, 500),
                self.next_step
            )
        else:
            self.root.after(
                random.randint(150, 900),
                self.update_progress
            )

    def next_step(self):
        self.step += 1

        if self.step >= len(self.steps):
            self.finished()
        else:
            self.show_step()

    def finished(self):
        self.clear()
        self.header()

        tk.Label(
            self.root,
            text="Update complete",
            font=("Segoe UI", 22),
            fg=self.text,
            bg="#f7f7f7"
        ).pack(pady=(65, 15))

        tk.Label(
            self.root,
            text="Windows Software Update has finished successfully",
            font=("Segoe UI", 11),
            fg=self.gray,
            bg="#f7f7f7"
        ).pack()

        tk.Button(
            self.root,
            text="Finish",
            command=self.show_fake_security_alerts,
            bg=self.blue,
            fg="white",
            activebackground="#005a9e",
            activeforeground="white",
            relief="flat",
            font=("Segoe UI", 10),
            padx=30,
            pady=8,
            cursor="hand2"
        ).pack(pady=45)

    def show_fake_security_alerts(self):
        self.clear()

        tk.Label(
            self.root,
            text="Update completed",
            font=("Segoe UI", 22),
            fg=self.text,
            bg="#f7f7f7"
        ).pack(pady=(70, 10))

        tk.Label(
            self.root,
            text="Thank you for keeping your computer safe.",
            font=("Segoe UI", 10),
            fg=self.gray,
            bg="#f7f7f7"
        ).pack()

        delay = 0

        for i in range(random.randint(10, 100)):
            delay += random.randint(10, 100)
            self.root.after(
                delay,
                lambda n=i + 1: self.warning_popup(n)
            )

    def warning_popup(self, number):

        winsound.MessageBeep(winsound.MB_ICONHAND)

        popup = tk.Toplevel(self.root)
        popup.title("Windows Security")
        popup.geometry("460x250")
        popup.resizable(False, False)
        popup.configure(bg="white")
        popup.attributes("-topmost", True)

        tk.Label(
            popup,
            text="⚠",
            font=("Segoe UI", 34),
            fg="#d83b01",
            bg="white"
        ).pack(pady=(15, 0))

        tk.Label(
            popup,
            text="Windows Security Alert",
            font=("Segoe UI", 11, "bold"),
            fg="#d83b01",
            bg="white"
        ).pack()

        tk.Label(
            popup,
            text="Malicious software has been detected on this device",
            font=("Segoe UI", 13, "bold"),
            fg=self.text,
            bg="white"
        ).pack(pady=6)

        tk.Label(
            popup,
            text="We suggest you either:\n"
                 "- Remove the malicious software\n"
                 "- Boot Windows in Safe Mode",
            font=("Segoe UI", 9),
            fg=self.gray,
            bg="white",
            justify="center"
        ).pack()

        tk.Button(
            popup,
            text="OK",
            width=12,
            command=popup.destroy
        ).pack(pady=15)


root = tk.Tk()
app = WindowsSoftwareUpdate(root)
root.mainloop()
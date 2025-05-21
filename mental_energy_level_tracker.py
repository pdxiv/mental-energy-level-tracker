import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
import os
import platform
import base64
import tempfile

# Brain icon as a base64 encoded GIF (64x64)
BRAIN_ICON_B64 = '''
R0lGODlhQABAAOf/AJCBjcbBxP/GAP/HAK2kp//IALCnqv/JAP/KAP/LAP/MAP/NAP/OAP/PAP/QAP/R
AAEABLmws//SAP/TAP/UAP/VAP/WAP/XAP/YAP/ZAP/aAP/bAP/cAP/dAP/eAP/fAP/gAP/hAP/iAP/j
AP/kANDLzv/lAP/mAP/nAP/oAP/pAP/qAP/rAP/sAP/tAP/uAP/vAP/wAP/xAP/yAP/zAP/0AP/1AP/2
AP/3AP/4AP/5AP/6AP/7AP/8AP/9AP/+AP//AJWMkZGIjZKJjpOKj5WMkJaMkZeNkpiOk5mPlJqQlZuR
lpySmJ2TmZ6UmqCVm6GWnKKXnaOYnqSZn6WaoaWbop6Wn5+XoKCYoaKapKObpaScpqecplm9mKecplm9
mVm+mqmep1m+m1m/nFm/nVnAnlnAn6mgqKqhqVnBoFnBoa2jq1nColnCo66krFnDpFnDpa+lrVnEplnE
p7CmrlnFqFnFqbGnr1nGqlnGq7KosVnHrFnHrbOpsrSpslnIrVnIrrSqs7WrtLartFnJr1nJsLattrGu
tLOvtbevtlnKsVnKsrivt1nLslnLs7mwuFnMtFnMtbqxuVnNtlnNt7uyu1nOuFnOubyzvFnPulnPu72z
vVnQvFnQvb60vlnRvlnRv7+1v1nSwFnSw8C2wFnTwVnTw8G3wcG4wlnUxFnUxcK5w1nVxlnVx8O6xFnW
yFnWyU3XykjXy0PYzD7ZzTnazjTb0C/c0Srd0ibf0yHf1Bzg1Rjh1hPi1w/j2Ark2Qbl2gLm2wDn3ADo
3QDp3gDq3wDr4ADs4QDt4gDu4wDv5ADw5QDx5gDy5wDz6AD06QD16gD27QD37gD47wD58AD68QD78gD8
8wD99QD+9gD/9wD/+AD/+QD/+gD/+wD//AD//QD//gD//wD//wD//wD//wD//wD//wD//wD//wD//wD/
/wD//wD//wD//wD//wD//wD//wD//wD//wD//wD//wD//wD//wD//wD//wD//wD//wD//wD//yH+EUNy
ZWF0ZWQgd2l0aCBHSU1QACH5BAEKAP8ALAAAAABAAEAAAAj+AP8JHEiwoMGDCBMqXMiwocOHECNKnEix
osWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2bOHPq3Mmzp8+fQIMKHUq0qNGjSJMq
XRrRwIIACBAwXcq06QGnUJ9OjfoA6tSqTaVezQqVa9euX7uG/Uq2bNivaNOqHZu2rduwb+Omndm2bt23
eff2/Ss3r9/BgQkPPlw4MOLGjRU/jpxY8WTKkC1fzqw58+bOnEF/Fh16NGnRqE2jVq2aderXsF/Lni0b
Nu3btXHn1s27t23fwXsHHz5cuHHkxZUjZ96c+XPoy6VLtz7d+nXp2LVnl86du3fq4MMz/y9fHn16iurV
s3e//n189e/l169Pnz7//Pv139///wAGKKCBAx6YoIELFvhggg0uGGGEE0Z4YYUbZthhh9StZ+GIrXW4
XWvYhVieiSime6KKK7L4ImgxzihjjDOKaGONN+K4I4888uijkDsWaeSRRyap5JFMJunkk08COeWUVVJZ
5WBXYpnlll2KqCWCX7LWpZhmlunmmmimuWabb8IZpHKKVWmnY3jeGWeeeu7JZ59+/glooIIOSmihiyGq
aKKMMurooyCOwVeehkKq6aacdjpVR6KKitSSpp6Kaqpbrcqqq1u6CmuUqqqq6qy01mqrrbjqeiqvvfr6
K7AICiyswAMjULA2wsQWa+yxyFrMrMDKJovtrJg9K+201Fab7bbcnnettt0O9+245GLLrbjibjWuuu6+
C2+79NZ7b7rO5ltvv9leJW/AAOtLb2AAF2wwwQcnrPDCDTdM8cMRT6ywWxMrfHHGFGfM8ccghyxyyB6T
PG9XJqOc8sosm/xyyzCXLHPMNNu8lc0c45zzrTr37PPPQAc9dM5EH220UkcrvfTSRzf9tNNRUy311FRX
LXXVWGe9dNdce71V2GKPTXbZYZ+Ndtpqxx023U3BHRXcdued9958a9X334AHLvjghN9puOGIJ6744ow3
LnTajkc+ueKVW365XZhfrvnmnG/++dyhhy760aSXvtQeAQA7
'''

class MentalEnergyLevelTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Mental Energy Level Tracker")
        self.root.geometry("600x800")
        self.root.minsize(500, 300)
        
        # Set the window icon
        self.set_window_icon()
        
        # Store the icon as an attribute to prevent garbage collection
        self.icon = None
        
        # Set up database
        self.setup_database()
        
        # Create UI
        self.create_ui()
        
        # Auto-resize after UI creation
        self.root.update_idletasks()
        self.resize_window_to_content()
    
    def set_window_icon(self):
        """Set the window icon using the base64 encoded GIF icon"""
        try:
            # Decode the base64 image
            icon_data = base64.b64decode(BRAIN_ICON_B64)
            
            # Create a temporary file to store the icon
            with tempfile.NamedTemporaryFile(delete=False, suffix='.gif') as f:
                f.write(icon_data)
                icon_path = f.name
            
            # Load the icon as a PhotoImage
            self.icon = tk.PhotoImage(file=icon_path)
            
            # Set the icon for the window
            self.root.iconphoto(True, self.icon)
            
            # Remove the temporary file
            try:
                os.remove(icon_path)
            except:
                pass
        except Exception as e:
            print(f"Could not set icon: {e}")
    
    def setup_database(self):
        """Create SQLite database and table if they don't exist"""
        if not os.path.exists("data"):
            os.makedirs("data")
            
        self.conn = sqlite3.connect("data/mental_energy_levels.db")
        self.cursor = self.conn.cursor()
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS energy_levels_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            focus TEXT,
            decision_making TEXT,
            memory TEXT,
            processing_speed TEXT,
            sharpness TEXT,
            communication TEXT,
            notes TEXT
        )
        ''')
        self.conn.commit()
    
    def resize_window_to_content(self):
        """Resize the window to fit content or 90% of screen height"""
        self.canvas.update_idletasks()
        
        # Get the content height and screen height
        content_height = self.canvas.bbox("all")[3] + 20
        screen_height = self.root.winfo_screenheight() * 0.9
        
        # Set height to the smaller of content height or 90% screen height
        new_height = min(content_height, screen_height)
        
        # Set window size
        self.root.geometry(f"{self.root.winfo_width()}x{int(new_height)}")
    
    def create_ui(self):
        """Create the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Canvas and scrollbar setup
        self.canvas = tk.Canvas(main_frame, highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        # Configure scrolling behavior
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Make canvas resize with window
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.canvas_window, width=e.width))
        
        # Pack canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Add mouse wheel scrolling
        self.bind_mousewheel()
        
        # Title
        ttk.Label(self.scrollable_frame, text="Mental Energy Level Tracker", 
                 font=("Arial", 16, "bold")).pack(pady=(0, 20))
        
        # Create category sections
        self.create_category_sections()
        
        # Notes section
        notes_frame = ttk.LabelFrame(self.scrollable_frame, text="Additional Notes")
        notes_frame.pack(fill=tk.X, pady=10, padx=5)
        
        self.notes_text = tk.Text(notes_frame, height=4)
        self.notes_text.pack(fill=tk.X, padx=10, pady=10, expand=True)
        
        # Buttons
        self.create_buttons()
        
        # Window resize handler for text wrapping
        self.root.bind("<Configure>", self.update_text_wrapping)
    
    def create_category_sections(self):
        """Create the assessment category sections"""
        # Style configuration for radio buttons
        self.root.option_add('*TRadiobutton*Foreground', 'black')
        ttk.Style().configure('Green.TRadiobutton', background='#e8f5e9')
        ttk.Style().configure('Yellow.TRadiobutton', background='#fff9c4')
        ttk.Style().configure('Red.TRadiobutton', background='#ffebee')
        
        # Define assessment categories
        self.categories = {
            "Focus & Attention": [
                "Can I easily concentrate on what I'm doing?",
                "Am I having trouble following conversations or written text?",
                "Do I have to reread or relisten frequently?"
            ],
            "Decision-making & Problem-solving": [
                "Is it hard to make simple decisions right now (e.g., deciding what to eat)?",
                "Does solving simple tasks seem difficult or overwhelming?"
            ],
            "Memory & Recall": [
                "Am I forgetting simple things (like why I entered a room, or what I was about to do)?",
                "Am I struggling to recall words, names, or common facts?"
            ],
            "Processing Speed": [
                "Does my thinking feel unusually slow or sluggish?",
                "Am I slower to respond to questions than usual?"
            ],
            "Sharpness & Alertness": [
                "Does my thinking feel fuzzy, unclear, or foggy?",
                "Am I misreading or misunderstanding things I normally wouldn't?"
            ],
            "Ease of Communication": [
                "Am I having trouble clearly expressing my thoughts?",
                "Am I unusually hesitant or stumbling when speaking?"
            ]
        }
        
        # Variables to store ratings
        self.ratings = {}
        
        # Create a frame to hold all categories
        categories_frame = ttk.Frame(self.scrollable_frame)
        categories_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create each category section
        for category, points in self.categories.items():
            # Create frame for this category
            category_frame = ttk.LabelFrame(categories_frame, text=category)
            category_frame.pack(fill=tk.X, pady=10, padx=5, expand=True)
            
            # Add description points
            for point in points:
                bullet_frame = ttk.Frame(category_frame)
                bullet_frame.pack(fill=tk.X, anchor=tk.W, pady=2, padx=10)
                
                ttk.Label(bullet_frame, text="•").pack(side=tk.LEFT, padx=(0, 5))
                ttk.Label(bullet_frame, text=point, wraplength=500).pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            # Add rating options
            rating_var = tk.StringVar(value="")
            self.ratings[category] = rating_var
            
            rating_frame = ttk.Frame(category_frame)
            rating_frame.pack(fill=tk.X, padx=10, pady=5)
            
            # Add radio buttons
            ttk.Radiobutton(rating_frame, text="Good", value="Good", 
                           variable=rating_var, style='Green.TRadiobutton').pack(side=tk.LEFT, padx=(0, 10))
            ttk.Radiobutton(rating_frame, text="Moderate", value="Moderate", 
                           variable=rating_var, style='Yellow.TRadiobutton').pack(side=tk.LEFT, padx=(0, 10))
            ttk.Radiobutton(rating_frame, text="Poor", value="Poor", 
                           variable=rating_var, style='Red.TRadiobutton').pack(side=tk.LEFT)
    
    def create_buttons(self):
        """Create action buttons"""
        # Set button style
        ttk.Style().configure('TButton', font=('Arial', 11))
        
        # Create button frame
        buttons_frame = ttk.Frame(self.scrollable_frame)
        buttons_frame.pack(fill=tk.X, pady=20)
        
        # Add buttons
        ttk.Button(buttons_frame, text="Submit Entry", command=self.save_entry).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="View History", command=self.view_history).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Clear Form", command=self.clear_form).pack(side=tk.LEFT, padx=5)
    
    def bind_mousewheel(self):
        """Bind mousewheel events based on platform"""
        system = platform.system()
        
        if system == "Windows":
            self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1 * e.delta / 120), "units"))
        elif system == "Darwin":  # macOS
            self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1 * e.delta), "units"))
        else:  # Linux
            self.canvas.bind_all("<Button-4>", lambda e: self.canvas.yview_scroll(-1, "units"))
            self.canvas.bind_all("<Button-5>", lambda e: self.canvas.yview_scroll(1, "units"))
    
    def update_text_wrapping(self, event):
        """Update text wrapping for labels when window is resized"""
        if event.widget != self.root:
            return
            
        # Calculate new wraplength
        new_wraplength = max(400, event.width - 150)
        
        # Update all labels in scrollable frame
        for widget in self.scrollable_frame.winfo_children():
            self.update_wraplength(widget, new_wraplength)
    
    def update_wraplength(self, widget, wraplength):
        """Recursively update wraplength for all labels"""
        for child in widget.winfo_children():
            if isinstance(child, ttk.Label) and child.cget("text") != "•":
                child.configure(wraplength=wraplength)
            elif hasattr(child, "winfo_children") and child.winfo_children():
                self.update_wraplength(child, wraplength)
    
    def save_entry(self):
        """Save the current entry to the database"""
        # Check for empty fields
        empty_fields = [category for category, var in self.ratings.items() if not var.get()]
        
        if empty_fields:
            messagebox.showwarning(
                "Incomplete Form", 
                f"Please fill in all categories before saving.\n\nMissing: {', '.join(empty_fields)}"
            )
            return
        
        # Get data
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notes = self.notes_text.get("1.0", tk.END).strip()
        
        # Insert into database
        self.cursor.execute('''
        INSERT INTO energy_levels_entries (
            timestamp, focus, decision_making, memory, 
            processing_speed, sharpness, communication, notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            timestamp,
            self.ratings["Focus & Attention"].get(),
            self.ratings["Decision-making & Problem-solving"].get(),
            self.ratings["Memory & Recall"].get(),
            self.ratings["Processing Speed"].get(),
            self.ratings["Sharpness & Alertness"].get(),
            self.ratings["Ease of Communication"].get(),
            notes
        ))
        
        self.conn.commit()
        messagebox.showinfo("Success", "Mental Energy Level entry saved successfully!")
        self.clear_form()
    
    def clear_form(self):
        """Clear all form fields"""
        for var in self.ratings.values():
            var.set("")
        self.notes_text.delete("1.0", tk.END)
    
    def view_history(self):
        """Open a new window to view entry history"""
        # Create history window
        history_window = tk.Toplevel(self.root)
        history_window.title("Mental Energy Level History")
        history_window.geometry("800x500")
        
        # Apply the icon to this window too
        if hasattr(self, 'icon') and self.icon:
            history_window.iconphoto(True, self.icon)
        
        # Create treeview columns
        columns = ("timestamp", "focus", "decision_making", "memory", 
                  "processing_speed", "sharpness", "communication")
        
        tree = ttk.Treeview(history_window, columns=columns, show="headings")
        
        # Set column headings
        tree.heading("timestamp", text="Date & Time")
        tree.heading("focus", text="Focus")
        tree.heading("decision_making", text="Decision")
        tree.heading("memory", text="Memory")
        tree.heading("processing_speed", text="Speed")
        tree.heading("sharpness", text="Sharpness")
        tree.heading("communication", text="Communication")
        
        # Set column widths
        tree.column("timestamp", width=150)
        for col in columns[1:]:
            tree.column(col, width=80, anchor=tk.CENTER)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(history_window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack tree and scrollbar
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Fetch and display data
        self.cursor.execute('''
        SELECT timestamp, focus, decision_making, memory, 
               processing_speed, sharpness, communication
        FROM energy_levels_entries
        ORDER BY timestamp DESC
        ''')
        
        for row in self.cursor.fetchall():
            tree.insert("", tk.END, values=row)
        
        # Function to show notes when row is double-clicked
        def show_notes(event):
            try:
                item = tree.selection()[0]
                timestamp = tree.item(item, "values")[0]
                
                # Fetch notes
                self.cursor.execute("SELECT notes FROM energy_levels_entries WHERE timestamp = ?", (timestamp,))
                notes = self.cursor.fetchone()[0]
                
                # Create note window
                note_window = tk.Toplevel(history_window)
                note_window.title(f"Notes - {timestamp}")
                note_window.geometry("400x300")
                
                # Apply the icon to the notes window too
                if hasattr(self, 'icon') and self.icon:
                    note_window.iconphoto(True, self.icon)
                
                note_text = tk.Text(note_window, wrap=tk.WORD)
                note_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
                note_text.insert(tk.END, notes if notes else "No notes for this entry.")
                note_text.config(state=tk.DISABLED)
            except IndexError:
                pass
        
        # Bind double-click event
        tree.bind("<Double-1>", show_notes)
        
        # Add instruction label
        ttk.Label(
            history_window, 
            text="Double-click any row to view notes for that entry",
            font=("Arial", 10, "italic")
        ).pack(side=tk.BOTTOM, pady=5)

def main():
    root = tk.Tk()
    app = MentalEnergyLevelTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
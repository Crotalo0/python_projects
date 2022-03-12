import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class emailSlicer:
    
    def __init__(self):
        
        # Creating the window
        self.window = tk.Tk()
        self.window.title("tk Email slicer")
        
        # Calling create_widgets to give structure to window
        self.create_widgets()

    def quitting(self):
        answer = messagebox.askyesno("Question", "Do you really wanna quit?")
        if answer is True:
            
            # I need the () at the end if i am not giving the command to a button.
            self.window.quit()

    def create_widgets(self):
        
        def reset():
            """Reset all entries"""
            answer = messagebox.askyesno("Question", "Are you sure to reset?")
            if answer is True:
                entry2.delete(0, 'end')
                entry3.delete(0, 'end')
                entry4.delete(0, 'end')
                messagebox.showinfo("Information", "Reset successful.")
        
        def slice():
            """E-mail slicer"""
            email_to_slice = str(entry2.get())
            user, domain = email_to_slice.split('@')
            entry3.insert(0, user)
            entry4.insert(0, domain)
            messagebox.showinfo("Information", "E-mail successfully sliced.")
                
                       
        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5

        # - - - - - - - - - - - - - - - - - - - - -
        # Entry Frame
        
        # Defining the program greeting title.
        labeled_frame_label = ttk.Label(self.window, text = "Welcome to email slicer!")
        labeled_frame_label.grid(row = 1, column = 1, pady = 3)

        # Frame 2 is the entry frame 
        # Here i defined  a labeled frame
        frame2 = ttk.LabelFrame(self.window, text = " Insert E-mail to slice: ", relief = tk.RIDGE)
        frame2.grid(row = 2, column = 1, sticky = tk.E + tk.W + tk.N + tk.S, padx = 30, pady = 4)
        
        # Creating a simple label and used grid to pin it in frame2
        label2 = ttk.Label(frame2, text = "E-mail: ")
        label2.grid(row = 1, column = 1, sticky = tk.W, pady = 3)
        
        # Creating an entry and pinned in frame2 next to label2
        entry2 = ttk.Entry(frame2, width = 40)
        entry2.grid(row = 1, column = 2, sticky = tk.E , pady = 3)
        
        # - - - - - - - - - - - - - - - - - - - - -
        # Frame with result.
        
        # Creating the Frame3 for results.        
        frame3 = ttk.LabelFrame(self.window, text = " Results ", relief = tk.RIDGE)
        frame3.grid(row = 4, column = 1, sticky = tk.E + tk.W + tk.N + tk.S, padx = 30, pady = 4)
        
        # Creating the label and the result box like before.  
        
        # Entry and label relative to Username      
        label3 = ttk.Label(frame3, text = "Username: ")
        label3.grid(row = 1, column = 1, sticky = tk.W, pady = 3)
        
        entry3 = ttk.Entry(frame3, width = 40)
        entry3.grid(row = 1, column = 2, sticky = tk.E , pady = 3)
        
        # Entry and label relative to Domain
        label4 = ttk.Label(frame3, text = "Domain name: ")
        label4.grid(row = 2, column = 1, sticky = tk.W, pady = 3)
        
        entry4 = ttk.Entry(frame3, width = 40)
        entry4.grid(row = 2, column = 2, sticky = tk.E , pady = 3)
        
        # - - - - - - - - - - - - - - - - - - - - -
        # Button Frame
        frame4 = ttk.Frame(self.window)
        frame4.grid(row = 3, column = 1, sticky = tk.E , padx = 30, pady = 4)
        button1 = ttk.Button(frame4, text = "Reset", command = reset)
        button1.grid(row = 1, column = 1, sticky = tk.E , pady = 3, padx = 10)
        button2 = ttk.Button(frame4, text = "Slice", command = slice)
        button2.grid(row = 1, column = 2, sticky = tk.E, padx = 10, pady = 3)
        
        
        # - - - - - - - - - - - - - - - - - - - - -
        # Menus
        menubar = tk.Menu(self.window)

        filemenu = tk.Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "Reset", command = reset)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = self.quitting)
        menubar.add_cascade(label = "File", menu = filemenu)

        self.window.config(menu = menubar)
        
def main():
    es = emailSlicer()
    es.window.mainloop()

if __name__ == "__main__":
    main()


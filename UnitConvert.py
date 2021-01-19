import tkinter as tk
from Distance import *

# Options list for the dropdown menus to select units
OPTIONS = Distance(0, None).getOptions()

class MainWindow(tk.Frame):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)

        self.inp_unit = ''      # stores current input unit dropdown menu choice
        self.outp_unit = ''     # stores current output unit dropdown menu choice

        # Create a frame to organize all the widgets associated with input values
        frm_input = tk.Frame(self, height=100)
        master = frm_input

        # Create text entry box
        self.ent_input = tk.Entry(master, width=10)
        self.ent_input.pack()

        # Create unit selection drop down menu for input unit
        input_variable = tk.StringVar(master)
        input_variable.set(' ')  # Default option shown in menu
        self.unit_input = tk.OptionMenu(master, input_variable, *OPTIONS, command=self.updateInpUnit)
        self.unit_input.pack()

        # Create the button that performs the conversion
        btn_convert = tk.Button(master, command=self.buttonClick, text="Convert To")
        btn_convert.pack()

        # Create another frame to organize all the widgets associated with output values
        frm_output = tk.Frame(self, height=100)
        master = frm_output

        # Create unit selection drop down menu for output unit
        output_variable = tk.StringVar(master)
        output_variable.set(' ')
        self.unit_output = tk.OptionMenu(master, output_variable,  *OPTIONS, command=self.updateOutpUnit)
        self.unit_output.pack()

        # Create results text box
        self.lbl_results = tk.Label(master, width=10, text=" ")
        self.lbl_results.pack(padx=50, pady=20)

        frm_input.pack()
        frm_output.pack()

    # This method updates inp_unit whenever the text menu box dropdown menu is updated.
    def updateInpUnit(self, value):
        self.inp_unit = value

    # This method updates outp_unit whenever the text menu box dropdown menu is updated.
    def updateOutpUnit(self, value):
        self.outp_unit = value


    def buttonClick(self):
        # grab the input
        value = float(self.ent_input.get())
        lbl = self.inp_unit

        # create a distance object
        distance = Distance(value, lbl)

        # convert it
        lbl = self.outp_unit
        converted = distance.convert(lbl)

        # display to output
        self.lbl_results.config(text=str(converted))



if __name__ == "__main__":
    root = tk.Tk()

    main = MainWindow(root)
    main.pack(fill="both", expand=True)

    root.mainloop()
import PySimpleGUI as sg 

class GUI:
    def __init__(self, title):
        self.title = title
    def create_window(self, layout = None):
        # Add some color 
        # to the window 
        sg.theme('Black')      
        
        # Very basic window. 
        # Return values using 
        # automatic-numbered keys 
        if layout is None:
            layout = [ 
                [sg.Text('Enter Your Order Number Below')], 
                [sg.Text('Order_Number', size =(15, 1)), sg.InputText(key='-ORDER-')], 
                [sg.Text('Additional Comment', size =(15, 1)), sg.InputText(key='-COMMENT-')],
                [sg.Text('',key='-ERROR-',visible=False)],
                [sg.Button('Submit'), sg.Cancel()] 
            ] 
        
        window = sg.Window(self.title, layout, grab_anywhere=True, finalize=True)    
        input_field = window['-ORDER-'].set_focus()

        self.window = window

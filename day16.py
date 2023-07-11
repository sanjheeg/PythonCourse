import PySimpleGUI as gui

def gui_stuff():
    feet_l = gui.Text("enter feet:")
    feet_i = gui.InputText()
    inch_l = gui.Text("enter inches:")
    inch_i = gui.InputText()
    conv_b = gui.Button("convert")
    window = gui.Window("converter", layout=[[feet_l, feet_i], [inch_l, inch_i],[conv_b]])
    window.read()
    window.close()



gui_stuff()
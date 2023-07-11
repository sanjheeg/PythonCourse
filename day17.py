import PySimpleGUI as gui

gui.theme("Black")

# day 18 involved adding the exit button and adding a theme for the window


def exercise2(ounces):
    return ounces * 29.57353


def exercise1():
    feet_l = gui.Text("enter feet:")
    feet_i = gui.InputText(key="feet")
    inch_l = gui.Text("enter inches:")
    inch_i = gui.InputText(key="inch")
    conv_b = gui.Button("convert")
    output_label = gui.Text("", key="output")
    exit_b = gui.Button("exit")
    window = gui.Window("converter", layout=[[feet_l, feet_i], [inch_l, inch_i],[conv_b,exit_b, output_label]])

    while True:
        event, values = window.read()
        match event:
            case "convert":
                feet_input = int(values["feet"])
                inch_input = int(values["inch"])
                print("feet ", feet_input)
                print("inch ", inch_input)
                total = (feet_input*12) + inch_input
                meters = total * 0.0254
                window["output"].update(value=str(meters)+"m")
            case "exit":
                break
            case gui.WIN_CLOSED:
                break

    window.close()

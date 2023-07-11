import PySimpleGUI as gui
from zip_extractor import extract

gui.theme("Black")


# zip elements
zip_l = gui.Text("select zip:")
zip_input = gui.InputText(tooltip="choose a zip file")
zip_b = gui.FileBrowse("select", key="zip")


# destination elements
dest_l = gui.Text("choose a destination")
dest_input = gui.InputText(tooltip="choose a destination")
dest_b = gui.FolderBrowse("select", key="destination")


# converting elements
convert_b = gui.Button("convert")
output_l = gui.Text(key="output", text_color="green")

window = gui.Window("zip extractor", layout=[[zip_l, zip_input, zip_b], [dest_l, dest_input, dest_b], [convert_b, output_l]])



while True:
    event, values = window.read()
    match event:
        case "convert":
            input_zip = values['zip']
            dest_folder = values["destination"]
            extract(input_zip, dest_folder)
            window["output"].update(value="extraction completed!")
        case gui.WIN_CLOSED:
            break


window.close()
import os
import PySimpleGUI as sg

def change_extensions(path_folder, old_extension, new_extension):
    files_counter = 0

    with os.scandir(path_folder) as files_and_folders:
        for element in files_and_folders:
            if element.is_file():
                tuple_root_ext = os.path.splitext(element.path)
                root = tuple_root_ext[0]
                ext = tuple_root_ext[1]

                if ext == old_extension:
                    new_path = root + new_extension
                    os.rename(element.path, new_path)
                    files_counter += 1

    return files_counter

def create_gui():
    layout = [
        [sg.Text("Directory Path"), sg.InputText(key="-FOLDER-"), sg.FolderBrowse()],
        [sg.Text("Old Extension"), sg.InputText(key="-OLD_EXT-")],
        [sg.Text("New Extension"), sg.InputText(key="-NEW_EXT-")],
        [sg.Button("Change Extensions"), sg.Button("Exit")]
    ]

    window = sg.Window("File Extension Changer", layout)

    while True:
        event, values = window.read()

        if event == "Change Extensions":
            folder_path = values["-FOLDER-"]
            old_extension = values["-OLD_EXT-"]
            new_extension = values["-NEW_EXT-"]

            if folder_path and old_extension and new_extension:
                files_changed = change_extensions(folder_path, old_extension, new_extension)
                sg.popup(f"Number of files processed: {files_changed}")

        if event in (sg.WINDOW_CLOSED, "Exit"):
            break

    window.close()

if __name__ == "__main__":
    create_gui()

import os, shutil, re, datetime
from tkinter import filedialog
from . import config

class Functions:
    def __init__(self):
        pass

    def getDirectoryContents(self, directory):
        try:
            absFilePaths = []
            for root, _, files in os.walk(directory):
                for file in files:
                    filePath = os.path.join(root, file)
                    absFilePaths.append(filePath)
            return absFilePaths
        except Exception as e:
            print(f"An error has occurred: {e}")

    
    def parseDirectoryString(self, directory):
        match = re.search(r"[/\\]([^/\\]*)[/\\]?$", directory)
        if match:
            return match.group(1)
        else:
            return None

    def zipDirectoryContents(self, zipButton, newDirectoryButton):
        zipButton.configure(state="disabled")
        newDirectoryButton.configure(state="disabled")
        directory = config.ZIPDIRECTORY
        newDirectory = config.SAVELOCATION
        directoryName = self.parseDirectoryString(directory)
        currentDate = datetime.date.today().strftime("%m.%d.%Y")
        if not os.path.exists(f"{directory}"):
            raise FileNotFoundError(f"Source directory '{directory}' was not found.")
        if os.path.exists(f"{newDirectory}/{directoryName}_archived_{currentDate}"):
            raise FileExistsError(f"The new location '{newDirectory}/{directoryName}_archived_{currentDate}' already exists.")
        
        try:
            newZipName = f"{directoryName}_archived_{currentDate}"
            zipWithDirectory = f"{os.getcwd()}/{directoryName}_archived_{currentDate}.zip"
            shutil.make_archive(newZipName, 'zip', directory)
            shutil.move(zipWithDirectory, newDirectory)
            print(f"Successfully packed '{directoryName}' to '{newDirectory}'")
        except Exception as e:
            print(f"An error has occurred: {e}")
        
        zipButton.configure(state="normal")
        newDirectoryButton.configure(state="normal")
    
    def chooseDirectory(self, action, label, packFilesButton):
        if action == "zip":
            print("Choosing ZIP folder")
            directory = filedialog.askdirectory()
            if directory:
                config.ZIPDIRECTORY = directory
                if len(directory) <= 50:
                    label.config(text=directory)
                else:
                    label.config(text="".join([".", ".", "."] + list(directory)[-47:]))

        elif action == "location":
            print("Choosing save location")
            directory = filedialog.askdirectory()
            if directory:
                config.SAVELOCATION = directory
                if len(directory) <= 50:
                    label.config(text=directory)
                else:
                    label.config(text="".join([".", ".", "."] + list(directory)[-47:]))
        
        if len(list(config.SAVELOCATION)) > 0 and len(list(config.ZIPDIRECTORY)) > 0:
            packFilesButton.configure(state="normal", background="#6cf542")
        else:
            packFilesButton.configure(state="disabled", background="#daffd6")
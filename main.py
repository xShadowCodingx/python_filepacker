# Main entry point for zipper file archiver
# Author: Chase Quinn
# Date: 3/20/2025

import os
from bin import ui, functions, config

uic = ui.Components()
func = functions.Functions()

root = uic.root()

fpLogo = os.getcwd() + "/bin/assets/FilePacker.png"
scLogo = os.getcwd() + "/bin/assets/ShadowCodingLogo.png"

# Initialize components
filePackerLabelImage = uic.image(root, fpLogo)
zipDescriptionLabel = uic.label(root, "Choose the directory to pack")
packFilesButton = uic.button(root, "Pack Files")
zipLabel = uic.label(root, "")
zipButton = uic.button(root, "Browse")
newDirectoryDescriptionLabel = uic.label(root, "Choose the save location")
newDirectoryLabel = uic.label(root, "")
newDirectoryButton = uic.button(root, "Browse")
shadowCodingLogo = uic.image(root, scLogo)

# Set image and update it to get correct measurements, then place it in correct position
filePackerLabelImage.pack()
filePackerLabelImage.update()
filePackerLabelImage.place(x=(root.winfo_width() / 2) - (filePackerLabelImage.winfo_width() / 2), y=35)

# zipDescriptionLabel
zipDescriptionLabel.configure(background="#aaaaaa")
zipDescriptionLabel.place(x=49, y=180)

# packFilesButton
packFilesButton.configure(background="#daffd6", height=5, width=12, state="disabled", command=lambda : func.zipDirectoryContents(zipButton, newDirectoryButton))
packFilesButton.place(x=368, y=375)

# zipLabel
zipLabel.configure(text=config.ZIPDIRECTORY, background="#ffffff", width=42, height=1)
zipLabel.place(x=49, y=202)

# zipButton
zipButton.configure(width=15,command=lambda : func.chooseDirectory("zip", zipLabel, packFilesButton))
zipButton.place(x=350, y=200)

# newDirectoryDescriptionLabel
newDirectoryDescriptionLabel.configure(background="#aaaaaa")
newDirectoryDescriptionLabel.place(x=49, y=250)

# newDirectoryLabel
newDirectoryLabel.configure(text=config.SAVELOCATION, background="#ffffff", width=42, height=1)
newDirectoryLabel.place(x=49, y=272)

# newDirectoryButton
newDirectoryButton.configure(width=15,command=lambda : func.chooseDirectory("location", newDirectoryLabel, packFilesButton))
newDirectoryButton.place(x=350, y=270)

# ShadowCodingLogo
shadowCodingLogo.configure(background="#aaaaaa")
shadowCodingLogo.place(x=-30, y=350)

root.mainloop()
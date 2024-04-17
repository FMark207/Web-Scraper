from bs4 import BeautifulSoup
import requests
import json

from tkinter import *

data = {
    "tempPage":"",
    "tempElement":"",
    "tempAttr":"",
    "tempName":"",
}

info = []

exportData = {
    "info":info,
    "tempId":""
}

#Test Site: https://tatibudapest.com/hu/menu

def scrapeTemplate(page, element, attrib, attribName):
    pageToScrape = requests.get(page)
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    thingToScrape = soup.findAll(element, attrs= {attrib:attribName})
    for i in thingToScrape:
        info.append(i.text)
    jsonObj = json.dumps(exportData, indent=4)
    with open("read.json", "a") as outFile:
        outFile.write(jsonObj)
        outFile.write("\n")

def testFunction():
    data["tempPage"] = str(pageInput.get())
    data["tempElement"] = str(elementInput.get())
    data["tempAttr"] = str(attrInput.get())
    data["tempName"] = str(nameInput.get())
    exportData["tempId"] = str(idInput.get())
    scrapeTemplate(data["tempPage"], data["tempElement"], data["tempAttr"], data["tempName"])

root = Tk()
root.title("WebScraper")

root.geometry("600x600")
root.tk.call("tk", "scaling", 1.5)

root.configure(background="#D9D9D9")

myLabel = Label(root, text="Web-Scraper Tool 2.0", font=("Arial", 20), pady="10", background=("#D9D9D9"))
myLabel.pack()

pageLabel = Label(root, text="Type In Page URL: ", font=("Arial", 10), pady="10", background=("#D9D9D9"))
pageLabel.pack()
pageInput = Entry(root, border=3, width=80)
pageInput.pack()

elementLabel = Label(root, text="Type In Element: ", font=("Arial", 10), pady="10", background=("#D9D9D9"))
elementLabel.pack()
elementInput = Entry(root, border=3, width=40)
elementInput.pack()

attrLabel = Label(root, text="Type In Attribute Type: ", font=("Arial", 10), pady="10", background=("#D9D9D9"))
attrLabel.pack()
attrInput = Entry(root, border=3, width=40)
attrInput.pack()

nameLabel = Label(root, text="Type In Attribute Name/Names: ", font=("Arial", 10), pady="10", background=("#D9D9D9"))
nameLabel.pack()
nameInput = Entry(root, border=3, width=80)
nameInput.pack()

idLabel = Label(root, text="ID name for list: ", font=("Arial", 10), pady="10", background=("#D9D9D9"))
idLabel.pack()
idInput = Entry(root, border=3, width=40)
idInput.pack()

hollowLabel = Label(root, text=" ", font=("Arial", 10), pady="40", background=("#D9D9D9"))
hollowLabel.pack()

saveButton = Button(root, width=30, height=2, text="Save To JSON", command=testFunction)
saveButton.pack()

exitButton = Button(root, width=30, height=2, text="Exit", command=root.destroy)
exitButton.pack()

root.mainloop()
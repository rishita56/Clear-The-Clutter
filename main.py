import os

def createifnotexists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername,files):
    for file in files:
        os.replace(file,f"{foldername}/{file}")

files=os.listdir()
files.remove("main.py")
print(files)
createifnotexists('Images')
createifnotexists('Docs')
createifnotexists('Media')
createifnotexists('Others')

imgExts=[".png",".jpg","jpeg"]
images=[file for file in files if os.path.splitext(file)[1].lower() in imgExts]


docsExts = [".txt",".docx",".doc",".pdf"]
docs=[file for file in files if os.path.splitext(file)[1].lower() in docsExts]


mediaExts=[".mp4",".mp3",".flv"]
medias=[file for file in files if os.path.splitext(file)[1].lower() in mediaExts]


others=[]
for file in files:
    ext=  os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docsExts) and (ext not in imgExts) and os.path.isfile(file):
        others.append(file)


move("Images",images)
move("Docs",docs)
move("Media",medias)
move("Images",images)
move("Others",others)
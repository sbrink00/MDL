import os
import shutil

def hasBadEnding(string):
  if string == "copyFiles.py": return True
  for ending in badEndings:
    if ending in string: return True
  return False

oldDir = input("What directory do you want to copy files from? ") + "/"
if os.path.exists("/Users/god/graphics/" + oldDir + "__pycache__"):
  shutil.rmtree("/Users/god/graphics/" + oldDir + "__pycache__")
files = os.listdir("/Users/god/graphics/" + oldDir)
badEndings = [".md", ".pyc", ".png", ".ppm", ".git", ".gif"]

files = [x for x in files if not hasBadEnding(x)]
print(files)
for i in files:
  with open("/Users/god/graphics/" + oldDir + i, "r") as f:
    s = f.readlines()
    with open(i, "w") as f1:
      f1.writelines(s)

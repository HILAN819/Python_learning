from pathlib import Path 
from zipfile import ZipFile

zip1 = ZipFile("files.zip", "w")
for p in Path("Demo").rglob("*.*"):
    zip1.write(p)
zip1.close()

# with ZipFile("files.zip") as zip1:
#     # print(zip1.namelist())
#     zip1.extractall("extract")
      
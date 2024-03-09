from pathlib import Path 
from zipfile import ZipFile

zip1 = ZipFile("files.zip", "w")
for p in Path("Demo").rglob("*.*"):
    zip1.write(p)
zip1.close()
from pathlib import Path
from time import ctime
import shutil

path = Path("Demo/")
# print(path.exists())
# print(path.is_file())
# print(path.is_dir())
paths = [p for p in path.iterdir()]  # if p is dir()]
# print(paths)
py_files = [p for p in path.rglob("*.py")]
# print("py files: ", py_files)


path2 = Path("Demo/exercise.py")
print(path2.exists())
# path2.rename("sample1.py")
# path2.unlink()
print(ctime(path2.stat().st_ctime))
print(path2.read_text(str))

# Copying a file
shutil.copy(path2, path)

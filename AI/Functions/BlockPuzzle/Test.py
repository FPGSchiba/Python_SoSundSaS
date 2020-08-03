import _tkinter as tk
import os
import sys

scriptpath = "./DragAndDrop.py"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))

# Do the import
from ./DragAndDrop


dnd = .DragManager()
dnd.add_dragable(label)
root.mainloop()
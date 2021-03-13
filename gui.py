from dearpygui.core import *
from dearpygui.simple import *

set_main_window_size(800,800)
#show_about()
#show_documentation()
with window("Simple GUI", width= 520, height= 677):
    print("GUI is running---")
    set_window_pos("Simple GUI",0,0)
    add_separator()
    add_spacing(count=12)
    add_text("This is a simple text for this simple gui", color = [232,163,33])
    add_separator()
    add_text("Next command", color = [232,163,33])

#
start_dearpygui()
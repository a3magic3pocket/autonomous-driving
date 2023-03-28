from ..utils.utils import Utils
from ..utils.windows import Windows
import os

if __name__ == "__main__":
    win = Windows()
    auto_title = "Ultimate Car Driving Game"
    img_dir_path = "img"
    os.makedirs(img_dir_path, exist_ok=True)
    
    dlg = win.get_dialog(auto_title)
    
    dlg[auto_title].wait('visible')
    dlg[auto_title].set_focus()
    print(f"{dlg.exists()=}")
    
    win.resize_window(auto_title, 1280, 720)
    
    w = dlg.wrapper_object().rectangle().width()
    radius = int(w/2)
    dlg.move_mouse_input(coords=(radius, 0), absolute=False)
    
    while True:
        screenshot_path = Utils.get_screenshot_path(img_dir_path)
        dlg.capture_as_image().save(screenshot_path)

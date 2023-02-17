from pywinauto import findwindows, application, keyboard
import datetime
import time
import sys
import os
from PIL import ImageGrab

def get_proc(name: str): 
    procs = findwindows.find_elements()
    
    for proc in procs:
        if name in proc.name:
            return proc
        
    return None

def get_dialog(auto_title):
    proc = get_proc(auto_title)
    if proc is None:
        print(f"{auto_title} is not opened. please open it and try again")
        sys.exit(1)
        
    auto_pid = proc.process_id
    
    app = application.Application(backend="uia")
    app.connect(process=auto_pid)
    dialogs = app.windows()
    # print(f"{dialogs=}")
    
    return app.window(class_name=proc.class_name, title_re=auto_title)

def type_key(keyword, typing_time_sec = 0.5):
    allowed_keys = ['{UP}', '{DOWN}', '{LEFT}', '{RIGHT}', 'idle']
    if keyword not in allowed_keys:
        print(f'{keyword} is not allowed, {allowed_keys=}')
        sys.exit(1)
    
    start = time.time()
    
    while True:
        now = time.time()
        diff = now - start
        
        if diff > typing_time_sec:
            break

        if keyword == 'idle':
            continue
        
        keyboard.send_keys(keyword)
        
def get_current_time_string():
    KST = datetime.timezone(datetime.timedelta(hours=+9))
    now = datetime.datetime.utcnow().replace(tzinfo=KST)
    
    return now.strftime("%Y-%m-%d_%H+%M+%S+%f")

def get_screenshot_path(parent_dir_path: str = ""):
    return f"{parent_dir_path}/screenshot_{get_current_time_string()}.png"
        
def hello():
    auto_title = "Ultimate Car Driving Game"
    up, down, left, right, idle = '{UP}', '{DOWN}', '{LEFT}', '{RIGHT}', 'idle'
    
    img_dir_path = "img"
    os.makedirs(img_dir_path, exist_ok=True)
    
    dlg = get_dialog(auto_title)
    
    dlg[auto_title].set_focus()
    print(f"{dlg.exists()=}")
    while True:
        # for key in [up, down, left, right]:
        for key in [up, idle]:
            screenshot_path = get_screenshot_path(img_dir_path)
            if key == up:
                type_key(key)
            elif key == idle:
                type_key(key, 3)
                
            dlg.capture_as_image().save(screenshot_path)
            print(f"{key=}")
    

if __name__ == "__main__":
    hello()
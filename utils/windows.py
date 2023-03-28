from pywinauto import findwindows, application, keyboard, mouse
import sys

class Windows:
    def get_proc(self, name: str): 
        procs = findwindows.find_elements()
        
        for proc in procs:
            if name in proc.name:
                return proc
            
        return None

    def get_dialog(self, auto_title, backend="uia"):
        assert backend in ['uia', 'win32']
        
        proc = self.get_proc(auto_title)
        if proc is None:
            print(f"{auto_title} is not opened. please open it and try again")
            sys.exit(1)
            
        auto_pid = proc.process_id
        
        app = application.Application(backend=backend)
        app.connect(process=auto_pid)
        
        return app.window(class_name=proc.class_name, title_re=auto_title)

    def resize_window(self, auto_title: str, width: int, height: int):
        app = self.get_dialog(auto_title, 'win32')
        app.move_window(0, 0, width, height, False)
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ExcelFileHandler(FileSystemEventHandler):
    def __init__(self, python_script_path):
        self.python_script_path = python_script_path

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('.xlsx'):
            print(f"Detected change in file: {event.src_path}")
            print("Running update script...")
            subprocess.run(["python", self.python_script_path])


if __name__ == "__main__":
    path_to_watch = "C:/Users/15267/Desktop/paper/rizhao/newdocument/"  # 替换为你想要监视的目录路径
    python_script_to_run = "graph.py"  # 替换为要运行的Python脚本路径

    event_handler = ExcelFileHandler(python_script_to_run)
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
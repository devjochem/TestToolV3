# This Python file uses the following encoding: utf-8
import logging
import os
import shutil
import subprocess
import sys
import tempfile
import time
from subprocess import Popen

import requests
from packaging import version
from PySide6.QtWidgets import QMainWindow, QAbstractItemView, QTableWidgetItem, QApplication

from lib.systemspecs import Specs
from windows.audiotest.audiotestwindow import AudioTest

from windows.lcdtest.lcdtestwindow import LCDWindow
from windows.kbtest.kbtestwindow import KBWindow
from windows.camtest.camtestwindow import CamWindow
from windows.battest.battestwintest import BatWindow

from windows.mainwindow.form import Ui_MainWindow



__version__ = "1.0.0"
GITHUB_REPO = "devjochem/TestToolV3"
ASSET_MATCH = "TestTool"


def get_latest_release(repo):
    r = requests.get(f"https://api.github.com/repos/{repo}/releases/latest")
    r.raise_for_status()
    return r.json()

def download_asset(asset_url):
    headers = {'Accept': 'application/octet-stream'}
    r = requests.get(asset_url, headers=headers, stream=True)
    r.raise_for_status()

    fd, tmp_path = tempfile.mkstemp()
    with os.fdopen(fd, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
    os.chmod(tmp_path, 0o755)
    return tmp_path

def launch_delayed_replacement(old_path, new_path):
    """
    Launch a stub process that waits for the current process to exit,
    replaces the old binary, and restarts it.
    """
    stub_code = f"""
import os, sys, time, shutil
time.sleep(2)
try:
    shutil.copy2(r"{new_path}", r"{old_path}")
    os.execv(r"{old_path}", [r"{old_path}"])
except Exception as e:
    print("Self-update failed:", e)
    sys.exit(1)
"""
    stub_file = tempfile.NamedTemporaryFile("w", delete=False, suffix=".py")
    stub_file.write(stub_code)
    stub_file.close()

    # Launch stub with the system Python executable
    subprocess.Popen([sys.executable, stub_file.name])
    print("Launched update stub. Exiting to complete update.")
    sys.exit(0)

def self_update():
    print(f"Current version: {__version__}")
    release = get_latest_release(GITHUB_REPO)
    latest_version = release["tag_name"].lstrip("v")

    if version.parse(latest_version) <= version.parse(__version__):
        print("Already up to date.")
        return

    print(f"New version available: {latest_version}")
    for asset in release["assets"]:
        if ASSET_MATCH in asset["name"]:
            print(f"Downloading asset: {asset['name']}")
            new_binary = download_asset(asset["url"])
            current_binary = sys.executable
            print(f"Preparing to update: {current_binary}")
            launch_delayed_replacement(current_binary, new_binary)


def info(key, data):
    info = "<span style=\" font-size:12pt; font-weight:600;\" >"
    info += f"{key}:    "
    info += "<span style=\" font-size:12pt; font-weight:600; color:#28a745;\" >" + f" {data}" + "</span>"
    info += "</span>"
    return info

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        logging.basicConfig(filename="./AppLog.log",
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            filemode='w')
        log = logging.getLogger()
        log.setLevel(logging.INFO)


        self.ui.pushButton_lcd.clicked.connect(lambda p: self.lcdwindow())
        self.ui.pushButton_kb.clicked.connect(lambda p: self.kbwindow())
        self.ui.pushButton_cm.clicked.connect(lambda p: self.camwindow())
        self.ui.pushButton_2.clicked.connect(lambda p: AudioTest().show())
        self.ui.batButton.clicked.connect(lambda p: BatWindow().show())
        self.ui.actionUpdate.triggered.connect(lambda p: self_update())
        log.info("TestTool started")
        specs = Specs()
        self.specs = specs.getSpecs()
        self.useroutput()

    def infolist(self,output,key,l):
        self.text = output
        info = "<span style=\" font-size:12pt; font-weight:600;\" >"
        info += f"{key}:"
        info += "</span>"
        self.text.append(info)
        for i,s in enumerate(l):
            self.text.append("<span style=\" font-size:12pt; font-weight:600; color:#28a745;\" >" + s.replace('gpu: ', '') + "</span><br>")

    def populate_disks(self):
        disks = self.specs["disks"]
        table = self.ui.diskTable
        table.verticalHeader().setVisible(False)
        table.setRowCount(len(disks))
        table.setColumnCount(3)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # w.verticalHeader().setVisible(False)
        table.horizontalHeader().setStretchLastSection(True)
        table.setHorizontalHeaderLabels(('Model', 'Size', 'Type'))

        for i,d in enumerate(disks):
            if d.get_type_str() == 'LOOP':
                continue
            s, u = d.get_size_in_hrf()
            table.setItem(i, 0, QTableWidgetItem(d.get_model()))
            table.setItem(i, 1, QTableWidgetItem(f"{s:.1f}  {u} "))
            table.setItem(i, 2, QTableWidgetItem(d.get_type_str()))
        table.resizeColumnsToContents()

    def useroutput(self):
        self.text = self.ui.userOutput
        title = "<span style=\" font-size:32pt; font-weight:600;\" > System Info </span>"
        self.text.append(title)

        self.text.append(info("VENDOR", self.specs['vendor']))
        self.text.append(info("MODEL", self.specs['model']))
        self.text.append(info("CPU", self.specs['cpu']))
        self.text.append(info("RAM", self.specs['ram']))

        gpus = self.specs["gpu"]
        self.infolist(self.text,"GPU(S)",gpus)
        self.populate_disks()
        #self.text.append(f'   {self.specs["cpu"]}')
        return self.text


    def lcdwindow(self):
        self.lcdWindow = LCDWindow()
        self.lcdWindow.show()
        self.lcdWindow.showFullScreen()

    def kbwindow(self):
        self.kbWindow = KBWindow()
        self.kbWindow.show()

    def camwindow(self):
        self.camWindow = CamWindow()
        self.camWindow.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
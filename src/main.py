from Computer import Computer
import console_colors as cc

import time
import curses
from curses import wrapper
from math import floor
import pandas as pd

_17X15 = (17, 15)  #minimum cell size

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

_max_x = curses.COLS - 1
_max_y = curses.LINES - 1

def get_bar_v(height):
    bar = ""
    for i in range(height):
        bar += '|\n'
    return bar

"""
Class Name:     Cell

Description:    Used to display the computer information 
                onto the screen in an organized fashion
"""

class Cell:
    def __init__(self, current: Computer) -> None:
        self.com = current
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

    def get_bar_text(self, max_val, current_val, max_size) -> str:
        bar = "|"
        if current_val > max_val:
            bar += self.center_text_w("OVER!", max_size)
        else:
            bar += "▇" * floor((float(current_val) / float(max_val)) * max_size)
            bar += " " * (max_size - len(bar))
        bar += "|"
        return bar

    def print_cell_text(self, y, x, stdscr) -> str:
        """
        return dict({
            "Hostname": self.host,
            "IP": self.addr,
            "MaxRAM": self.max_ram,
            "CurrentCPU": self.current_cpu,
            "CurrentRAM": self.current_ram
        })
        """
        dict = self.com.dictionary()
        dict_t = self.com.task_dct()

        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)

        lp = 0  #lines printed for positioning

        stdscr.addstr(
            y, x,
            self.center_text(dict["Hostname"][0:self.width].upper()) + ' ',
            curses.color_pair(1) if dict["Alive"] else curses.color_pair(2))

        lp += 1

        stdscr.addstr(
            y + lp, x,
            f"""CPU: {self.get_bar_text(100, float(dict["CurrentCPU"]), 5)} {int(float(dict["CurrentCPU"]))}%  |"""
        )

        lp += 1

        stdscr.addstr(
            y + lp, x,
            f"""RAM: {self.get_bar_text(int(dict["MaxRAM"]), int(dict["CurrentRAM"]), 5)}{dict["CurrentRAM"]}/{dict["MaxRAM"]} |"""
        )

        lp += 1
        stdscr.addstr(y + lp, x, f"{self.get_dividing_bar()}|"); lp += 1
        stdscr.addstr(y + lp, x, f"""{self.center_text("TOP TASKS")}|"""); lp += 1
        stdscr.addstr(y + lp, x, f"""1. {dict_t["Task1"][0][0:13]} |"""); lp += 1
        stdscr.addstr(y + lp, x, f"""CPU: {self.get_bar_text(100, float(dict_t["Task1"][1]), 5)} {int(float(dict_t["Task1"][1]))}%  |"""); lp += 1
        stdscr.addstr(y + lp, x, f"""{self.center_text(self.get_dividing_bar()[:self.width])}|"""); lp += 1
        stdscr.addstr(y + lp, x, f"""2. {dict_t["Task2"][0][0:13]} |"""); lp += 1
        stdscr.addstr(y + lp, x, f"""CPU: {self.get_bar_text(100, float(dict_t["Task2"][1]), 5)} {int(float(dict_t["Task2"][1]))}%  |"""); lp += 1
        stdscr.addstr(y + lp, x, f"""{self.center_text(self.get_dividing_bar()[:self.width])}|"""); lp += 1
        stdscr.addstr(y + lp, x, f"""3. {dict_t["Task3"][0][0:13]}\t |"""); lp += 1
        stdscr.addstr(y + lp, x, f"""CPU: {self.get_bar_text(100, float(dict_t["Task3"][1]), 5)} {int(float(dict_t["Task3"][1]))}%  |"""); lp += 1
        stdscr.addstr(y + lp, x, f"""{self.get_dividing_bar()}+""")

    def get_dividing_bar(self) -> str:
        return "-" * self.width

    def center_text(self, some_str) -> str:
        centered_str = " " * int(
            (self.width - len(some_str)) / 2) + some_str + " " * int(
                (self.width - len(some_str)) / 2)
        return centered_str

    def center_text_w(self, some_str, width) -> str:
        centered_str = " " * int((width - len(some_str)) / 2) + some_str
        return centered_str

    def trunc_text(self, some_str, width) -> str:
        if len(some_str) > width:
            return some_str[0:width]
        return some_str

    def snap_to_grid(self, pos) -> (int, int):
        return 0

    def get_pos(self):
        return (self.x, self.y)

    def set_xy(self, x, y) -> None:
        self.x = int(x)
        self.y = int(y)

    def set_wh(self, pos) -> None:
        self.width = int(pos[0])
        self.height = int(pos[1])

    def get_top_tasks(self) -> list:
        dict_t = self.com.task_dct()
        return [[dict_t["Task1"][0][0:13], dict_t["Task1"][1]],
                [dict_t["Task2"][0][0:13], dict_t["Task2"][1]],
                [dict_t["Task3"][0][0:13], dict_t["Task3"][1]]]

def csv_to_com(path) -> Computer:
    df = pd.read_csv(path, header=None, index_col=0).squeeze("columns")
    info = df.to_dict()
    com = Computer(info["alive"], 
                    info["hostname"], 
                    info["address"],
                    info["max_ram"], 
                    info["cpu"], 
                    info["cur_ram"],
                    info["task1_name"], 
                    info["task2_name"],
                    info["task3_name"], 
                    info["task1_cpu"], 
                    info["task2_cpu"],
                    info["task3_cpu"])
    com.path = path
    return com

def new_cell(computer, x, y, wh) -> Cell:
    cell = Cell(computer)
    cell.set_xy(int(x), int(y))
    cell.set_wh(wh)
    return cell

def main(stdscr):
    germain_path = "/home/lab-monitor/lab-monitor/data/data.csv"
    katherine_path = "/home/lab-monitor/lab-monitor/data/data3.csv"
    rockhopper_path = "/home/lab-monitor/lab-monitor/data/data4.csv"
    germain = csv_to_com(germain_path)[0]
    katherine = csv_to_com(katherine_path)[0]
    rockhopper = csv_to_com(rockhopper_path)[0]

    # curses.init_pair(1, (curses.COLOR_BLACK if katherine.dictionary()["Alive"]
    #                      else curses.COLOR_WHITE),
    #                  (curses.COLOR_WHITE
    #                   if katherine.dictionary()["Alive"] else curses.COLOR_RED))
    # curses.init_pair(1, (curses.COLOR_BLACK if rockhopper.dictionary()["Alive"]
    #                      else curses.COLOR_WHITE),
    #                  (curses.COLOR_WHITE
    #                   if rockhopper.dictionary()["Alive"] else curses.COLOR_RED))

    stdscr.clear()

    while True:  #change later to while button hit is not escape or control + c or something like that
        germain = csv_to_com(germain)[0]
        katherine = csv_to_com(katherine)[0]
        rockhopper = csv_to_com(rockhopper)[0]
        germain_cell = new_cell(germain, 0, 18*0, _17X15)
        katherine_cell = new_cell(katherine, 0, 18*1, _17X15)
        rockhopper_cell = new_cell(rockhopper, 0, 18*2, _17X15)
        germain_cell.print_cell_text(0, 18*0, stdscr)
        katherine_cell.print_cell_text(0, 18*1, stdscr)
        rockhopper_cell.print_cell_text(0, 18*2, stdscr)
        #title, info = cell_text[0], cell_text[1]
        #stdscr.addstr(0, 0, title, curses.color_pair(1))
        stdscr.refresh()
        time.sleep(1)
    curses.endwin()


wrapper(main)

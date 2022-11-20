from math import floor
from Computer import Computer
import curses
from curses import wrapper
import pandas as pd
import console_colors as cc
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
Cell class

Used to display the computer information 
onto the screen in an 
"""

class Cell:
    over = "|OVER!|"

    def __init__(self, current: Computer) -> None:
        self.com = current
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

    def get_bar_text(self, max_val, current_val, max_size) -> str:
        if current_val > max_val:
            return Cell.over
        bar = '|'
        bar += ("▩" if
                (int(current_val) >= round(float(max_val))) else "▩") * floor(
                    (float(current_val) / float(max_val)) * max_size)
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
        # Returns a cell that has a fancy looking UI
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
        stdscr.addstr(y + lp, x, f"""{self.center_text(self.get_dividing_bar()[:self.width//2])} |"""); lp += 1
        stdscr.addstr(y + lp, x, f"""2. {dict_t["Task2"][0][0:13]} |"""); lp += 1
        
        stdscr.addstr(y + lp, x, f"""CPU: {self.get_bar_text(100, float(dict_t["Task2"][1]), 5)} {int(float(dict_t["Task2"][1]))}%  |"""); lp += 1
        stdscr.addstr(y + lp, x, f"""{self.center_text(self.get_dividing_bar()[:self.width//2])} |"""); lp += 1
        stdscr.addstr(y + lp, x, f"""3. {dict_t["Task3"][0][0:13]}\t |"""); lp += 1
        stdscr.addstr(y + lp, x, f"""CPU: {self.get_bar_text(100, float(dict_t["Task3"][1]), 5)} {int(float(dict_t["Task3"][1]))}%  |"""); lp += 1
        stdscr.addstr(y + lp, x, f"""{self.get_dividing_bar()}+""")

   

#         return [
#             self.center_text(dict["Hostname"][0:self.width].upper()) + ' ',
#             f"""CPU: {self.get_bar_text(100, float(dict["CurrentCPU"]), 5)} {int(float(dict["CurrentCPU"]))}%  |
# RAM: {self.get_bar_text(int(dict["MaxRAM"]), int(dict["CurrentRAM"]), 5)}{dict["CurrentRAM"]}/{dict["MaxRAM"]} |
# {self.get_dividing_bar()}|
# {self.center_text("TOP TASKS")}|
# 1. {dict_t["Task1"][0][0:13]} |
# CPU: {self.get_bar_text(100, float(dict_t["Task1"][1]), 5)} {int(float(dict_t["Task1"][1]))}%  |
# {self.center_text(self.get_dividing_bar()[:self.width//2])} |
# 2. {dict_t["Task2"][0][0:13]} |
# CPU: {self.get_bar_text(100, float(dict_t["Task2"][1]), 5)} {int(float(dict_t["Task2"][1]))}%  |
# {self.center_text(self.get_dividing_bar()[:self.width//2])} |
# 3. {dict_t["Task3"][0][0:13]}\t |
# CPU: {self.get_bar_text(100, float(dict_t["Task3"][1]), 5)} {int(float(dict_t["Task3"][1]))}%  |
# {self.get_dividing_bar()}+
# """
#         ]

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


def get_bash_cinfo_as_com(files) -> Computer:
    compu = []
    for i in range(len(files)):
        df = pd.read_csv(files[i], header=None, index_col=0, squeeze=True)
        info = df.to_dict()
        compu.append(
            Computer(info["alive"], info["hostname"], info["address"],
                     info["max_ram"], info["cpu"], info["cur_ram"],
                     info["task1_name"], info["task2_name"],
                     info["task3_name"], info["task1_cpu"], info["task2_cpu"],
                     info["task3_cpu"]))
    return compu


def new_cell(computer, x, y, wh) -> Cell:
    cell = Cell(computer)
    cell.set_xy(int(x), int(y))
    cell.set_wh(wh)
    return cell


def main(stdscr):
    germain = get_bash_cinfo_as_com(("data.csv", ))[0]
    germain_cell = new_cell(germain, 0, 0, _17X15)


    # curses.init_pair(1, (curses.COLOR_BLACK if germain.dictionary()["Alive"]
    #                      else curses.COLOR_WHITE),
    #                  (curses.COLOR_WHITE
    #                   if germain.dictionary()["Alive"] else curses.COLOR_RED))
    # curses.init_pair(1, (curses.COLOR_BLACK if germain2.dictionary()["Alive"]
    #                      else curses.COLOR_WHITE),
    #                  (curses.COLOR_WHITE
    #                   if germain2.dictionary()["Alive"] else curses.COLOR_RED))

    stdscr.clear()
    while True:  #change later to while button hit is not escape or control + c or something like that
        germain = get_bash_cinfo_as_com(("data.csv", ))[0]
        germain_cell.print_cell_text(0, 0, stdscr)
        #title, info = cell_text[0], cell_text[1]


       # stdscr.addstr(0, 0, title, curses.color_pair(1))


        stdscr.refresh()
    curses.endwin()

wrapper(main)

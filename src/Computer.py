class Computer:
    def __init__(self):
      self.host = None
      self.addr = None
      self.listed = None
      self.top_tasks = None
      self.top_tasks_cpu = None
      self.max_ram = None
      self.current_cpu = None
      self.current_ram = None
      self.alive = None
      self.path = None
    def __init__(self, alive, hn, _addr, mr, cpu, ram, 
                 tt1, tt2, tt3, tt1cpu, tt2cpu, tt3cpu) -> None:     
      self.host = hn
      self.addr = _addr
      self.listed = [self.host, self.addr]
      self.top_tasks = [tt1, tt2, tt3]
      self.top_tasks_cpu = [tt1cpu, tt2cpu, tt3cpu]
      self.max_ram = mr
      self.current_cpu = cpu
      self.current_ram = ram
      self.alive = (alive == 'true') 
      self.path = ""
    def task_dct(self) -> dict:
      return dict({
        "Task1": [self.top_tasks[0], self.top_tasks_cpu[0]],
        "Task2": [self.top_tasks[1], self.top_tasks_cpu[1]],
        "Task3": [self.top_tasks[2], self.top_tasks_cpu[2]]   
      })    
    def dictionary(self) -> dict:
      return dict({
          "Hostname": self.host,
          "IP": self.addr,
          "MaxRAM": self.max_ram,
          "CurrentCPU": self.current_cpu,
          "CurrentRAM": self.current_ram,
          "Tasks": self.task_dct(),
          "Alive": self.alive
      })

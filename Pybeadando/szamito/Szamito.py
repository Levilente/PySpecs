import psutil

#print(psutil.cpu_percent(1))
#print(psutil.disk_usage("C:"))
#print(psutil.sensors_battery())
#print(psutil.cpu_count(logical=True))
class data:
    def __init__(self):
        self.cpu=""
        self.disk=""
        self.battery=""
        self.corecount=""
import tkinter as tk
import psutil
from szamito.Szamito import data

root = tk.Tk()
root.title("Rendszerinfó")
root.geometry("800x400")
def ui():
    button1 = tk.Button(root, command=Refresh, text="Frissítés", anchor="c")
    button2 = tk.Button(root, command=Tulterheltteszt, text="Processzor Tulterheltseg teszt", anchor="c")
    button3 = tk.Button(root, command=WriteOut, text="Mentes fajlba", anchor="c")
    button1.grid(row=0, column=0)
    button2.grid(row=1, column=0)
    button3.grid(row=2, column=0)
    root.mainloop()

d=data()
def Refresh():
    d.cpu=psutil.cpu_percent(1)
    d.disk=psutil.disk_usage("C:")
    d.battery=psutil.sensors_battery()
    d.corecount=psutil.cpu_count(logical=True)
    global substring2
    global substring3
    diskuse=str(d.disk)
    substring1=diskuse[11:]
    substring3=substring1[:-1]
    batuse=str(d.battery)
    substring2=batuse[17:20]
    cpulb=tk.Label(root, text="CPU-Felhasznalas: " + str(d.cpu)+"%")
    disklb=tk.Label(root, text="Lemezfelhasznalas: " + substring3 +"%")
    batterylb=tk.Label(root, text="Akkumulator: " + substring2 + "%")
    corecountlb=tk.Label(root, text="Logikai magok szama: " + str(d.corecount))
    cpulb.grid(row=3, column=0)
    disklb.grid(row=6, column=0)
    batterylb.grid(row=5, column=0)
    corecountlb.grid(row=4, column=0)

def Tulterheltteszt():
    if d.cpu>85:
        cpustresslb=tk.Label(root, text="CPU-Tulterhelt!")
        cpustresslb.grid(row=3, column=2)
    else:
        cpustresslb=tk.Label(root, text="CPU-Megfelelo allapotban!")
        cpustresslb.grid(row=3, column=2)

def WriteOut():
    with open('eredmenyek.txt', 'w') as f:
        f.write("CPU-Felhasznalas: " + str(d.cpu)+"%" +"\n" +"Lemezfelhasznalas: " + substring3 +"%"+ "\n" +"Akkumulator: " + substring2 + "%"+ "\n" +"Logikai magok szama: " + str(d.corecount))





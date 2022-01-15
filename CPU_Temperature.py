# Takes CPU tempture 5 times calc avg. value 
# with crontab runs the script each min and saves values to text_exporter folder
# node_exporter adds metrics which are picked up by Prometheus and pushed to grafana
# if using crontab, have to use python3 as it admin mode it will take default version 2, even if aliase is created

from gpiozero import CPUTemperature
import statistics
import time

cpu = CPUTemperature()
cpu = str(cpu).replace("<gpiozero.CPUTemperature object temperature=", "")
cpu = str(cpu).replace(">", "")
# print (cpu)

temp1 = float(cpu)
# print (temp1)

time.sleep(1)
cpu = CPUTemperature()
cpu = str(cpu).replace("<gpiozero.CPUTemperature object temperature=", "")
cpu = str(cpu).replace(">", "")
temp2 = float(cpu)
# print (temp2)

time.sleep(1)
cpu = CPUTemperature()
cpu = str(cpu).replace("<gpiozero.CPUTemperature object temperature=", "")
cpu = str(cpu).replace(">", "")
temp3 = float(cpu)
# print (temp3)

time.sleep(1)
cpu = CPUTemperature()
cpu = str(cpu).replace("<gpiozero.CPUTemperature object temperature=", "")
cpu = str(cpu).replace(">", "")
temp4 = float(cpu)
# print (temp4)

time.sleep(1)
cpu = CPUTemperature()
cpu = str(cpu).replace("<gpiozero.CPUTemperature object temperature=", "")
cpu = str(cpu).replace(">", "")
temp5 = float(cpu)
# print (temp5)

orders = [temp1, temp2, temp3, temp4, temp5]
average = statistics.mean(orders)
print('CPU_Temperature', str(round(average, 2)))

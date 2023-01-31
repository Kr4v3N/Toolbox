import platform

import psutil

#https://docs.python.org/3/library/platform.html

my_system = platform.uname()

print(f"Node Name: {my_system.node}")
print(f"Sytem: {my_system.system}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: machine:{my_system.machine}")
print(f"Processor: {my_system.processor}")

print(f"Platform: {platform.platform()}")
print(f"Architecture: {platform.architecture()}")

#####################################################
#####################################################
# import psutil,pprint,tabulate
#
# for proc in psutil.process_iter(['pid', 'ppid', 'name', 'username', ]):
#     print(proc.info)

#####################################################
#####################################################
# import psutil,sys
#
# # Overall CPU utilization, based on interval
# try:
#     while True:
#         print(psutil.cpu_percent(interval=3, percpu=True))
# except KeyboardInterrupt:
#     print("Stopping")
#     sys.exit(0)
# except Exception as e:
#     print(e)

#####################################################
#####################################################

# #CPU PERCENT PER PROCESS, BASED ON INTERVAL
#
# p = psutil.Process(2894) # Number represents PID
#
# try:
#     while True:
#         print("The process {} has a rolling utilization of {}%".format(p.name(),p.cpu_percent(interval=3)))
# except KeyboardInterrupt:
#     print("Stopping")
#     sys.exit(0)
# except Exception as e:
#     print(e)

#####################################################
#####################################################

# #SYSTEM WIDE MEMORY USAGE
# Virtual_memory = psutil.virtual_memory()
# print("Total memory: {} bytes".format(("{:,}".format(Virtual_memory.total))))
# print("Used memory: {} bytes".format(("{:,}".format(Virtual_memory.used))))
# print("Total memory percentage: {} bytes".format(("{:,}".format(Virtual_memory.percent))))
# print("Available memory: {} bytes".format(("{:,}".format(Virtual_memory.free))))

#####################################################
#####################################################
# # CHECKING MEMORY USE OF SPECIFIC PROCESS
# p = psutil.Process(2959)
# Process_Memory = p.memory_info().rss
# print("The {} process is using {} bytes of physical memory".format(p.name(),("{:,}".format(Process_Memory))))

#####################################################
#####################################################
# import winapps
#
# #The library currently lookups only for software installed for all users
# index = 0
# thisdict = {}
#
# for item in winapps.list_installed():
#     thisdict [item.name] = item.version
#
# print(thisdict)
#
# for key, value in thisdict.items():
#     print(key, ' : ', value)

import psutil
#Vaiables
memory = psutil.virtual_memory()

#Functions
def ConvertGiB(bytes):
    return round(bytes / (1024 ** 3))

#CPU
print("CPUS STATS:")
print("-----------------")

print("Physical CPUS:", psutil.cpu_count(logical=False))
print("Logical CPUS:", psutil.cpu_count(logical = True))
print("")

#MEMORY
print("MEMORY STATS:")
print("-----------------")

print("Total Memory:", ConvertGiB(memory.total), "GiB")
print("Available Memory:", ConvertGiB(memory.available), "GiB")
print("Used Memory:", ConvertGiB(memory.used), "GiB")
print("Memory Percentage:", memory.percent, "%")
print("")

#DISK
print("DISK STATS:")
print("-----------------")
print("Total Disk Space:", ConvertGiB(psutil.disk_usage('/').total), "GiB")
print("Used Disk Space:", ConvertGiB(psutil.disk_usage('/').used), "GiB")
print("Free Disk Space:", ConvertGiB(psutil.disk_usage('/').free), "GiB")
print("Disk Usage Percentage:", psutil.disk_usage('/').percent, "%")
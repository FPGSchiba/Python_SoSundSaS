# Version 1.0
# Author: Jann Erhardt
# Build: 1.0

import psutil
import GPUtil


def get_size(bytes):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}"
        bytes /= factor


def CPU_Precent():
    return psutil.cpu_percent()


def MEM_Precent():
    swap = psutil.swap_memory()
    return swap.percent


def DISK_Usage():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        return partition_usage.percent


def DISK_Free():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        return int(float(get_size(partition_usage.free)))


def DISK_Max():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        return int(float(get_size(partition_usage.total)))


def GPU_Usage():
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        print("SoS")
        gpu_load = f"{gpu.load * 100}%"
        gpu_temperature = f"{gpu.temperature} °C"
        list_gpus.append((
            f"GPU-Load: {gpu_load}", f"GPU-Temp: {gpu_temperature}"
        ))
    return list_gpus

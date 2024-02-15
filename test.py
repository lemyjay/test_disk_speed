#!/usr/bin/python3

import psutil

def get_disk_speed():
    disk_usage = psutil.disk_io_counters()
    read_speed = disk_usage.read_bytes
    write_speed = disk_usage.write_bytes
    return read_speed, write_speed

read_speed, write_speed = get_disk_speed()
print(f"Read speed: {read_speed} bytes/sec")
print(f"Write speed: {write_speed} bytes/sec")


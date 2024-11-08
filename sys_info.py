import os
import psutil
import platform
import socket
import argparse

def get_distro_info():
    try:
        with open("/etc/os-release") as f:
            distro_info = f.readlines()
        distro = {}
        for line in distro_info:
            if line.startswith("NAME="):
                distro["name"] = line.split("=")[1].strip().strip('"')
            elif line.startswith("VERSION="):
                distro["version"] = line.split("=")[1].strip().strip('"')
        return f"{distro.get('name', 'Unknown')} {distro.get('version', 'Unknown')}"
    except Exception as e:
        return f"Error fetching distro info: {e}"

def get_memory_info():
    memory = psutil.virtual_memory()
    return {
        "total": memory.total,
        "used": memory.used,
        "free": memory.free
    }

def get_cpu_info():
    cpu_info = {}
    cpu_info["model"] = platform.processor() or "Unknown"
    cpu_info["cores"] = psutil.cpu_count(logical=False)  
    cpu_info["logical_cores"] = psutil.cpu_count(logical=True)  
    cpu_info["speed"] = psutil.cpu_freq().current if psutil.cpu_freq().current else "Unknown"
    return cpu_info

def get_current_user():
    return os.getlogin()

def get_load_avg():
    load_avg = os.getloadavg()
    return {"1min": load_avg[0], "5min": load_avg[1], "15min": load_avg[2]}

def get_ip_address():
    ip_address = socket.gethostbyname(socket.gethostname())
    return ip_address

def main():
    parser = argparse.ArgumentParser(description="Get system information.")
    
    parser.add_argument("-d", "--distro", action="store_true", help="Display distribution information")
    parser.add_argument("-m", "--memory", action="store_true", help="Display memory usage (total, used, free)")
    parser.add_argument("-c", "--cpu", action="store_true", help="Display CPU information (model, cores, speed)")
    parser.add_argument("-u", "--user", action="store_true", help="Display current user")
    parser.add_argument("-l", "--load", action="store_true", help="Display system load average")
    parser.add_argument("-i", "--ip", action="store_true", help="Display IP address")

    args = parser.parse_args()

    if args.distro:
        print("Distribution Info:", get_distro_info())

    if args.memory:
        memory_info = get_memory_info()
        print(f"Memory Info: Total = {memory_info['total'] / (1024**3):.2f} GB, Used = {memory_info['used'] / (1024**3):.2f} GB, Free = {memory_info['free'] / (1024**3):.2f} GB")

    if args.cpu:
        cpu_info = get_cpu_info()
        print(f"CPU Model: {cpu_info['model']}")
        print(f"Physical Cores: {cpu_info['cores']}")
        print(f"Logical Cores: {cpu_info['logical_cores']}")
        print(f"CPU Speed: {cpu_info['speed']} MHz")

    if args.user:
        print("Current User:", get_current_user())

    if args.load:
        load_avg = get_load_avg()
        print(f"Load Averages: 1 min = {load_avg['1min']}, 5 min = {load_avg['5min']}, 15 min = {load_avg['15min']}")

    if args.ip:
        print("IP Address:", get_ip_address())

if __name__ == "__main__":
    main()

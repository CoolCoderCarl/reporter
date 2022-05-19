import platform
from datetime import datetime

import psutil

# MD not txt
# Pass args


def general_info(report_time: str):
    system = platform.uname()
    with open("report_" + report_time + ".txt", "a") as report:
        report.write("GENERAL INFO \n")
        report.write("System: " + system.system + "\n")
        report.write("Node Name: " + system.node + "\n")
        report.write("Release: " + system.release + "\n")
        report.write("Version: " + system.version + "\n")
        report.write("Machine: " + system.machine + "\n")
        report.write("Processor: " + system.processor + "\n")
        report.write("\n")


def get_disk_usage() -> dict:
    """
    Create dictionary from psutil output
    :return:
    """
    disk_util_mem = []
    disk_util_kind = ["Total", "Used", "Free", "Percent"]
    for val in range(len(psutil.disk_usage("/")) - 1):
        disk_util_mem.append(psutil.disk_usage("/")[val] // 1024 // 1024 // 1024)

    disk_util_mem.append(psutil.disk_usage("/")[-1])

    disk_usage_dict = {
        disk_util_kind[i]: disk_util_mem[i] for i in range(len(psutil.disk_usage("/")))
    }

    return disk_usage_dict


def disk_info(report_time: str):
    with open("report_" + report_time + ".txt", "a") as report:
        report.write("DISK USAGE \n")
        for key in get_disk_usage():
            if "percent" in key:
                report.write(key + " : " + str(get_disk_usage()[key]) + "%\n")
            else:
                report.write(key + " : " + str(get_disk_usage()[key]) + " GB\n")
        report.write("\n")


# Gather info about cpu

# Gather info about net

# Gather info about mem

# print(psutil.test())

if __name__ == "__main__":
    timestamp = datetime.now().strftime("%d.%m.%Y_%H.%M.%S")
    general_info(timestamp)
    disk_info(timestamp)

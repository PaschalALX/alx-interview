#!/usr/bin/python3
import sys

""" script that reads stdin line by line and computes metrics """

log_data = {
    "total_file_size": 0,
    "status_codes": {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                     404: 0, 405: 0, 500: 0}
}
cnt = 0


def print_log_data(log_data):
    ''' print log data'''
    print(f"File size: {log_data.get('total_file_size')}")
    {print(f"{k}: {v}") for k, v in log_data.get('status_codes').items() if v}


try:
    for line in sys.stdin:
        inputs = line.split()
        try:
            file_size = inputs[-1]
            status_code = inputs[-2]
            log_data["total_file_size"] += int(file_size)
            log_data["status_codes"][int(status_code)] += 1

            if cnt and cnt % 10 == 0:
                print_log_data(log_data)
                cnt = -1
            cnt += 1
        except Exception:
            pass

except KeyboardInterrupt:
    print_log_data(log_data)

import psutil
import time
import logging

# Define thresholds
cpu_threshold = 80  
mem_threshold = 80  
disk_threshold = 80  

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to check CPU usage
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > cpu_threshold:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
        print(f"High CPU usage detected: {cpu_usage}%")
    else:
        logging.info(f"CPU usage: {cpu_usage}%")

# Function to check memory usage
def check_memory_usage():
    mem_usage = psutil.virtual_memory().percent
    if mem_usage > mem_threshold:
        logging.warning(f"High memory usage detected: {mem_usage}%")
        print(f"High memory usage detected: {mem_usage}%")
    else:
        logging.info(f"Memory usage: {mem_usage}%")

# Function to check disk usage
def check_disk_usage():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > disk_threshold:
        logging.warning(f"High disk usage detected: {disk_usage}%")
        print(f"High disk usage detected: {disk_usage}%")
    else:
        logging.info(f"Disk usage: {disk_usage}%")

# Function to check running processes
def check_running_processes():
    num_processes = len(psutil.pids())
    logging.info(f"Total running processes: {num_processes}")
    print(f"Total running processes: {num_processes}")

# Main function to monitor system health
def monitor_system_health():
    print("Monitoring system health...")
    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        check_running_processes()
        time.sleep(1)  

# Execute the monitoring function
if __name__ == "__main__":
    monitor_system_health()

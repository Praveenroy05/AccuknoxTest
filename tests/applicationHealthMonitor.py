import requests
import time
import logging


# URL of the application to check
app_url = "http://127.0.0.1:54709"

logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to check application status# Function to check application status
def check_application_status():
    try:
        response = requests.get(app_url)
        if response.status_code == 200:
            logging.info(f"Application is UP. Status Code: {response.status_code}")
            print(f"Application is UP. Status Code: {response.status_code}")
        else:
            logging.warning(f"Application is DOWN. Status Code: {response.status_code}")
            print(f"Application is DOWN. Status Code: {response.status_code}")
    except requests.ConnectionError:
        logging.error("Connection Error: Application is DOWN")
        print("Connection Error: Application is DOWN")

# Main function to monitor application health
def monitor_application_health(interval=30):
    print(f"Monitoring application health every {interval} seconds...")
    while True:
        check_application_status()
        time.sleep(interval)

# Execute monitoring function
if __name__ == "__main__":
    monitor_application_health()

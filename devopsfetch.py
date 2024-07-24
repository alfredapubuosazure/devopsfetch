import logging
logging.basicConfig(filename='/home/ubuntu/devopsfetch/debug.log', level=logging.INFO)
logging.info('Script started')

import argparse
import psutil
import docker
from prettytable import PrettyTable
import time
import logging

# Function to retrieve and display active ports and services
def get_active_ports():
    table = PrettyTable(["Port", "Service"])
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr and conn.status == 'LISTEN':
            table.add_row([conn.laddr.port, conn.pid])
    print(table)

# Function to retrieve and display docker images and containers
def get_docker_info():
    client = docker.from_env()
    images = client.images.list()
    containers = client.containers.list(all=True)
    
    image_table = PrettyTable(["Image ID", "Tags"])
    for image in images:
        image_table.add_row([image.id, ', '.join(image.tags)])
    print(image_table)
    
    container_table = PrettyTable(["Container ID", "Image", "Status", "Ports"])
    for container in containers:
        container_table.add_row([container.id, container.image.tags, container.status, container.ports])
    print(container_table)

# Function to retrieve and display nginx configurations
def get_nginx_info():
    # Dummy function; replace with actual nginx config retrieval logic
    print("Nginx configuration information goes here")

# Function to retrieve and display user login times
def get_user_info():
    table = PrettyTable(["User", "Last Login"])
    for user in psutil.users():
        table.add_row([user.name, time.ctime(user.started)])
    print(table)

# Main function to parse arguments and call respective functions
def main():
    parser = argparse.ArgumentParser(description='DevOpsFetch Tool for retrieving system information.')
    parser.add_argument('-p', '--port', nargs='?', const=True, help='Display all active ports and services or detailed information about a specific port')
    parser.add_argument('-d', '--docker', nargs='?', const=True, help='List all Docker images and containers or detailed information about a specific container')
    parser.add_argument('-n', '--nginx', nargs='?', const=True, help='Display all Nginx domains and their ports or detailed configuration information for a specific domain')
    parser.add_argument('-u', '--users', nargs='?', const=True, help='List all users and their last login times or detailed information about a specific user')
    parser.add_argument('-t', '--time', nargs='?', help='Display activities within a specified time range')
    parser.add_argument('--continuous', action='store_true', help='Enable continuous monitoring mode')
    parser.add_argument('--log-file', help='Specify log file for continuous monitoring mode')

    args = parser.parse_args()

    if args.port:
        get_active_ports()
    if args.docker:
        get_docker_info()
    if args.nginx:
        get_nginx_info()
    if args.users:
        get_user_info()

    if args.continuous:
        logging.basicConfig(filename='/home/ubuntu/devopsfetch/logs/devopsfetch.log', level=logging.INFO, format='%(asctime)s %(message)s')
        while True:
            if args.port:
                get_active_ports()
            if args.docker:
                get_docker_info()
            if args.nginx:
                get_nginx_info()
            if args.users:
                get_user_info()
            time.sleep(60)

if __name__ == "__main__":
    main()
# Add at the start of devopsfetch.py
with open('/home/ubuntu/devopsfetch/debug.log', 'a') as f:
    f.write('Script started\n')


import argparse
import os
import subprocess
import pwd
import grp
import time
from prettytable import PrettyTable

def list_ports():
    output = subprocess.check_output(['ss', '-tuln']).decode()
    print(output)

def port_details(port_number):
    output = subprocess.check_output(['ss', '-tulnp', f"sport = :{port_number}"]).decode()
    print(output)

def list_docker():
    images = subprocess.check_output(['docker', 'images']).decode()
    containers = subprocess.check_output(['docker', 'ps', '-a']).decode()
    print("Docker Images:\n", images)
    print("Docker Containers:\n", containers)

def docker_details(container_name):
    container_info = subprocess.check_output(['docker', 'inspect', container_name]).decode()
    print(container_info)

def list_nginx():
    nginx_config = subprocess.check_output(['nginx', '-T']).decode()
    print(nginx_config)

def nginx_details(domain):
    nginx_config = subprocess.check_output(['nginx', '-T']).decode()
    domain_info = [line for line in nginx_config.splitlines() if domain in line]
    print("\n".join(domain_info))

def list_users():
    users = pwd.getpwall()
    table = PrettyTable(['Username', 'Last Login Time'])
    for user in users:
        try:
            last_login = subprocess.check_output(['lastlog', '-u', user.pw_name]).decode().splitlines()[-1]
            table.add_row([user.pw_name, last_login])
        except:
            table.add_row([user.pw_name, 'Never logged in'])
    print(table)

def user_details(username):
    try:
        last_login = subprocess.check_output(['lastlog', '-u', username]).decode().splitlines()[-1]
        print(f"User: {username}\nLast Login: {last_login}")
    except:
        print(f"User: {username}\nLast Login: Never logged in")

def time_range_activity(start_time, end_time):
    # Implement activity within a time range retrieval logic here
    pass

def main():
    parser = argparse.ArgumentParser(description="DevOpsFetch Tool")

    parser.add_argument('-p', '--port', nargs='?', const=True, help='Display active ports or details of a specific port')
    parser.add_argument('-d', '--docker', nargs='?', const=True, help='List Docker images and containers or details of a specific container')
    parser.add_argument('-n', '--nginx', nargs='?', const=True, help='Display Nginx domains and ports or details of a specific domain')
    parser.add_argument('-u', '--users', nargs='?', const=True, help='List users and last login times or details of a specific user')
    parser.add_argument('-t', '--time', nargs=2, metavar=('START', 'END'), help='Display activities within a specified time range')
    parser.add_argument('-h', '--help', action='help', help='Show this help message and exit')

    args = parser.parse_args()

    if args.port is not None:
        if args.port is True:
            list_ports()
        else:
            port_details(args.port)
    elif args.docker is not None:
        if args.docker is True:
            list_docker()
        else:
            docker_details(args.docker)
    elif args.nginx is not None:
        if args.nginx is True:
            list_nginx()
        else:
            nginx_details(args.nginx)
    elif args.users is not None:
        if args.users is True:
            list_users()
        else:
            user_details(args.users)
    elif args.time is not None:
        start_time, end_time = args.time
        time_range_activity(start_time, end_time)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()


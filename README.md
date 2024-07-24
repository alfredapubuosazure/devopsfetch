# DevOpsFetch Tool

## Overview
DevOpsFetch is a tool designed to collect and display system information, including active ports, user logins, Nginx configurations, Docker images, and container statuses. It includes a systemd service for continuous monitoring and logging.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd devopsfetch
    ```

2. Run the installation script:
    ```bash
    sudo ./install.sh
    ```

## Usage

### Commands

- Display active ports:
    ```bash
    devopsfetch -p
    ```

- Display details of a specific port:
    ```bash
    devopsfetch -p <port_number>
    ```

- List Docker images and containers:
    ```bash
    devopsfetch -d
    ```

- Display details of a specific container:
    ```bash
    devopsfetch -d <container_name>
    ```

- Display Nginx domains and ports:
    ```bash
    devopsfetch -n
    ```

- Display details of a specific domain:
    ```bash
    devopsfetch -n <domain>
    ```

- List users and their last login times:
    ```bash
    devopsfetch -u
    ```

- Display details of a specific user:
    ```bash
    devopsfetch -u <username>
    ```

- Display activities within a specified time range:
    ```bash
    devopsfetch -t <start_time> <end_time>
    ```

- Display help:
    ```bash
    devopsfetch -h
    ```

## Logging
The `devopsfetch` tool logs its activities to `/var/log/devopsfetch.log`. Log rotation is configured to keep logs manageable.

## Systemd Service
The `devopsfetch` service is installed and enabled by default. It monitors system information continuously and logs the data.

- To start the service:
    ```bash
    sudo systemctl start devopsfetch
    ```

- To stop the service:
    ```bash
    sudo systemctl stop devopsfetch
    ```

- To check the status of the service:
    ```bash
    sudo systemctl status devopsfetch
    ```


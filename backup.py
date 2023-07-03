#!/usr/bin/python3

import os
import paramiko
from datetime import date

# Date related variables
today = date.today()
date = today.strftime("%Y/%B/%d")
year = today.strftime("%Y")
month = today.strftime("%B")
day = today.strftime("%d")

# Login and SSH variables
user = "ansible"
passwd = "Ansible3^auto"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Nodes location and list
net_nodes = "net_nodes.txt"
home = os.getcwd() + "/"

# Base backup path
backup_path = "/home/ansible/backups"
backup_root_dir = os.path.exists(backup_path)
if not backup_root_dir:
    print("\n\t--- The backup root directory does not exist ---")
    print("\t+++ Creating the backup root directory +++\n")
    os.makedirs(backup_path)
    print("\t+++ /home/ansible/backups/ +++\n")
else:
    print("\n\t+++ The backup root directory is already exist +++\n")

# Year directory within the backup root directory
backup_year_path = "/home/ansible/backups/" + year
year_path_dir = os.path.exists(backup_year_path)
if not year_path_dir:
    print("\n\t--- The year, " + year + ", directory does not exist ---")
    print("\t+++ Creating the backup year directory +++\n")
    os.makedirs(backup_year_path)
    print("\t+++ The directory, " + year + ", has been created +++\n")
else:
    print("\n\t+++ The backup year directory, " + year + ", is already exist +++\n")

# Month directory within the Year directory
backup_month_path = "/home/ansible/backups/" + year + "/" + month
month_path_dir = os.path.exists(backup_month_path)
if not month_path_dir:
    print("\n\t--- The month, " + month + ", directory does not exist ---")
    print("\t+++ Creating backup month, " + month + ", directory +++\n")
    os.makedirs(backup_month_path)
    print("\t+++ The directory, " + month + ", has been created +++\n")
else:
    print("\n\t+++ The backup month directory, " + month + ", is already exist +++\n")

# Day directory within the Month directory
backup_day_path = "/home/ansible/backups/" + year + "/" + month + "/" + day
day_path_dir = os.path.exists(backup_day_path)
if not day_path_dir:
    print("\n\t--- The day, " + day + ", directory does not exist ---")
    print("\t+++ Creating backup day, " + day + ", directory +++\n")
    os.makedirs(backup_day_path)
    print("\t+++ The directory, " + day + ", has been created +++\n")
else:
    print("\n\t+++ The backup day directory, " + day + ", is already exist +++\n")

# Nodes and location
input_file = open( home + net_nodes, "r")
node_list = input_file.readlines()
input_file.close()

# Change directory to the Day directory
os.chdir(backup_day_path)

# Run the For loop to backup every single nodes
for ip in node_list:
    ip_addr = ip.strip()
    ssh.connect(hostname=ip_addr, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command('show running-config')
    list = stdout.readlines()
    output_file = open(ip_addr + ".config", "w")
    for node in list:
        output_file.write(node)
    ssh.close()
    output_file.close()


"""
TODO: Organize variables using host_vars structure

Your mission:
1. Create host_vars directory in project root  
2. Move variables from inventory to individual host files
3. Create device-specific configurations
4. Test variable precedence and organization
"""

# Directory structure to create:
directory_structure = """
project_root/
├── host_vars/
│   ├── router01.yml
│   ├── switch01.yml  
│   └── switch02.yml
├── inventory/
│   └── hosts.yml (cleaned up)
└── playbooks/
    └── configure_devices.yml
"""

# Template for host_vars/router01.yml:
router_vars_template = """
# TODO: Create this file as host_vars/router01.yml
---
# Connection variables
ansible_user: admin
ansible_password: YOUR_PASSWORD  # TODO: Replace with actual password
ansible_network_os: ios
ansible_connection: ansible.netcommon.network_cli

# Device-specific configuration
hostname: R1-Core-Router
domain_name: lab.local
mgmt_ip: 192.168.1.1

# Interface configuration
interfaces:
  - name: GigabitEthernet0/0
    description: "LAN Interface"
    ip: 192.168.10.1
    mask: 255.255.255.0
  - name: GigabitEthernet0/1  
    description: "WAN Interface"
    ip: 192.168.20.1
    mask: 255.255.255.0

# Loopback interfaces
loopbacks:
  - number: 0
    ip: 10.1.1.1
    mask: 255.255.255.255

# TODO: Add your own device-specific variables here
"""

# Template for switch variables:
switch_vars_template = """
# TODO: Create similar files for switches with:
# - VLANs configuration
# - Switch-specific interfaces  
# - Port configurations
# - Trunk settings
"""

print("Follow the templates above to create organized host variable files!")
print("Remember: Keep sensitive data secure using ansible-vault")
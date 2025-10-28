"""
TODO: Organize shared configurations using group_vars

Your mission:
1. Create group_vars directory structure
2. Set up logical device groupings in inventory
3. Create shared variable files for different device types  
4. Test variable precedence and inheritance
"""

# Updated inventory structure with groups:
inventory_template = """
# TODO: Update your inventory/hosts.yml with device groups
all:
  children:
    routers:
      hosts:
        router01:
          ansible_host: 192.168.1.1  # TODO: Your router IP
    switches:
      hosts:  
        switch01:
          ansible_host: 192.168.1.2  # TODO: Your switch IP
        switch02:
          ansible_host: 192.168.1.3  # TODO: Second device if available
"""

# group_vars/all.yml template:
all_vars_template = """
# TODO: Create group_vars/all.yml with global settings
---
# NTP Configuration (applies to ALL devices)
ntp_servers:
  - 192.168.1.100  # TODO: Replace with your lab NTP server
  - time.nist.gov

# DNS Configuration  
dns_servers:
  - 8.8.8.8
  - 8.8.4.4

# Domain and SNMP (global settings)
domain_name: lab.local
snmp_community: lab_readonly

# Connection defaults for all Cisco devices
ansible_connection: ansible.netcommon.network_cli
ansible_network_os: ios
ansible_user: admin
# TODO: Move passwords to encrypted vault files

# Global timezone
timezone: "EST -5"
"""

# group_vars/routers.yml template:
routers_vars_template = """
# TODO: Create group_vars/routers.yml for router-specific settings
---
# Routing protocol settings
routing_protocol: ospf
ospf_process_id: 1
ospf_area: 0

# Services specific to routers
enable_ip_routing: true
enable_ip_cef: true
enable_cdp: true

# Default interfaces routers should have
expected_interfaces:
  - GigabitEthernet0/0
  - GigabitEthernet0/1
  - Loopback0
"""

# group_vars/switches.yml template:  
switches_vars_template = """
# TODO: Create group_vars/switches.yml for switch-specific settings
---
# VLAN configuration for all switches
vlans:
  - id: 10
    name: "SALES"
  - id: 20
    name: "ENGINEERING"  
  - id: 99
    name: "MANAGEMENT"

# Spanning tree configuration
spanning_tree_mode: "rapid-pvst"
vtp_mode: "transparent"

# Services specific to switches  
enable_cdp: true
enable_lldp: true
disable_vtp: true
"""

print("Create the group_vars directory and files using the templates above!")
print("Test variable inheritance with: ansible-inventory --host <devicename>")
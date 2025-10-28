"""
TODO: Create your first Ansible inventory and playbook
Follow the README.md instructions to build these files

Your mission:
1. Create inventory/hosts.yml with your DevNet Sandbox device info
2. Create basic_operations.yml playbook  
3. Test connectivity and run basic commands
"""

# Inventory Template (create as inventory/hosts.yml in project root):
inventory_template = """
# TODO: Replace with your actual DevNet Sandbox device details
all:
  children:
    cisco_devices:
      hosts:
        sandbox-router:
          ansible_host: YOUR_DEVICE_IP_HERE
          ansible_network_os: ios
          ansible_connection: ansible.netcommon.network_cli
          ansible_user: YOUR_USERNAME
          ansible_password: YOUR_PASSWORD
"""

# Playbook Template (create as basic_operations.yml):
playbook_template = """
---
- name: Basic Network Device Operations  
  hosts: cisco_devices
  gather_facts: no
  
  tasks:
    - name: Test device connectivity
      # TODO: Add ansible.netcommon.net_ping module
      
    - name: Gather basic device information
      # TODO: Add cisco.ios.ios_facts module
      register: device_facts
      
    - name: Display device info
      # TODO: Add debug task to show device facts
      
    - name: Run show version command
      # TODO: Add cisco.ios.ios_command module
      # Use commands: ['show version']
      register: version_output
      
    - name: Display version information
      # TODO: Add debug task to show version output
"""

# Test commands to run after creating files:
test_commands = """
# Run these commands to test your setup:
ansible all -i inventory/hosts.yml -m ping
ansible-playbook -i inventory/hosts.yml basic_operations.yml
"""

print("Complete the TODO items above to create your first Ansible inventory and playbook!")
print("Remember: Replace placeholder values with your actual DevNet Sandbox details")
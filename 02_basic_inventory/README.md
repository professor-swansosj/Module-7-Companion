# 02: Basic Inventory and First Playbook

## 🎯 Mission

Create your first Ansible inventory file with device connection details and execute basic network automation tasks. You'll connect to a Cisco DevNet Sandbox device and run simple operations to verify connectivity and gather basic information.

## 🎖 Goals

- [ ] Build an inventory file with inline variables for device connections
- [ ] Connect to a Cisco device using Ansible
- [ ] Execute basic network commands (ping, show version)
- [ ] Understand Ansible modules for network automation
- [ ] Run your first playbook successfully

## 📚 Why This Matters

The inventory file is Ansible's address book for your network devices. It defines which devices exist, how to connect to them, and basic information about each device. Starting with inline variables (variables defined directly in the inventory) helps you understand the connection process before we organize things better in later topics.

## 🔑 Key Terms

- **Inventory File**: YAML or INI file listing managed devices and their connection parameters
- **Inline Variables**: Variables defined directly within the inventory file alongside hostnames
- **ansible_host**: The actual IP address Ansible uses to connect to a device
- **ansible_network_os**: Tells Ansible which network operating system the device runs
- **Module**: Reusable code that performs specific tasks (like gathering facts or running commands)

## 🗂 Basic Inventory Structure

Your inventory file defines devices and groups them logically:

```yaml
# Simple inventory with inline variables
all:
  children:
    cisco_devices:
      hosts:
        sandbox-router:
          ansible_host: 192.168.1.1
          ansible_network_os: ios
          ansible_connection: ansible.netcommon.network_cli
          ansible_user: admin
          ansible_password: cisco123
```

## 📋 Essential Connection Variables

For Cisco devices, you need these key variables:

- `ansible_host`: Device IP address
- `ansible_network_os`: Operating system (ios, eos, junos, etc.)
- `ansible_connection`: How Ansible connects (usually network_cli for Cisco)
- `ansible_user`: Username for authentication  
- `ansible_password`: Password for authentication

## 💡 Try It: Build Your First Inventory

1. **Create the inventory structure**:
   - Make an `inventory` folder in your project root
   - Create `hosts.yml` inside the inventory folder
   - TODO: Add your DevNet Sandbox device details using the template above

2. **Test connectivity**:

   ```bash
   ansible all -i inventory/hosts.yml -m ping
   ```

3. **Gather device facts**:

   ```bash
   ansible all -i inventory/hosts.yml -m ios_facts
   ```

## 🎮 Your First Playbook

Create a simple playbook to automate basic device checks:

```yaml
---
- name: Basic Network Device Operations
  hosts: cisco_devices
  gather_facts: no
  
  tasks:
    - name: Test device connectivity
      # TODO: Use the ping module for network devices
      
    - name: Gather basic device information
      # TODO: Use ios_facts module to collect device info
      
    - name: Show running configuration summary  
      # TODO: Use ios_command to run 'show version'
```

## 🔍 Check Yourself

1. What's the difference between `ansible_host` and the device name in your inventory?
2. Why do network devices use `ansible.netcommon.network_cli` instead of SSH directly?
3. What information does the `ios_facts` module collect?
4. How would you run a playbook against only one device from your inventory?
5. What happens if you don't specify `gather_facts: no` in a network playbook?

## 🛠 Common Issues & Solutions

**Connection Refused**: Check IP address and ensure device is reachable

```bash
ping 192.168.1.1
```

**Authentication Failed**: Verify username/password in your inventory
**Module Not Found**: Install the Cisco collection:

```bash
ansible-galaxy collection install cisco.ios
```

## 🔗 Essential Resources

- [Ansible Inventory Basics](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html)
- [Cisco IOS Module Guide](https://docs.ansible.com/ansible/latest/collections/cisco/ios/index.html)
- [DevNet Sandbox Access](https://developer.cisco.com/sandbox/)

## 🚀 Next Up

Once you can successfully connect and run basic commands, you'll learn to organize your variables better using `host_vars` for cleaner, more maintainable configurations!

---

**💡 Pro Tip**: Start with a simple inventory file and one device. Get that working perfectly before adding complexity!
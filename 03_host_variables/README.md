# 03: Host Variables - Device-Specific Configurations

## 🎯 Mission

Learn to organize device-specific variables using `host_vars` for cleaner, more maintainable Ansible projects. You'll move variables out of your inventory file and create dedicated configuration files for each network device.

## 🎖 Goals

- [ ] Understand the benefits of separating variables from inventory
- [ ] Create `host_vars` directory structure
- [ ] Build device-specific variable files
- [ ] Apply unique configurations to individual devices
- [ ] Manage device-specific interface and VLAN settings

## 📚 Why This Matters

As your network grows, managing variables becomes critical. Inline variables in inventory files quickly become messy and hard to maintain. Host variables let you organize device-specific settings in separate files, making your automation more scalable and easier to understand. Think of it as giving each device its own configuration profile.

## 🔑 Key Terms

- **host_vars**: Directory containing YAML files with variables specific to individual hosts
- **Variable Precedence**: The order Ansible uses to determine which variable values to apply
- **YAML**: Human-readable data format used for Ansible variables and playbooks
- **Ansible Vault**: Tool for encrypting sensitive variables (passwords, SNMP communities)
- **Variable Scoping**: How variables apply to specific hosts, groups, or all devices

## 🗂 Host Variables Structure

Moving from inline variables to organized structure:

**Before (Topic 02):**

```yaml
# inventory/hosts.yml - messy inline variables
all:
  children:
    cisco_devices:
      hosts:
        router01:
          ansible_host: 192.168.1.1
          ansible_user: admin
          ansible_password: cisco123
          mgmt_ip: 192.168.1.1
          loopback_ip: 10.1.1.1
```

**After (Topic 03):**

```yaml
# inventory/hosts.yml - clean inventory
all:
  children:
    cisco_devices:
      hosts:
        router01:
          ansible_host: 192.168.1.1
        switch01:
          ansible_host: 192.168.1.2
```

```yaml
# host_vars/router01.yml - device-specific variables
ansible_user: admin
ansible_password: cisco123
ansible_network_os: ios
ansible_connection: ansible.netcommon.network_cli

device_type: router
mgmt_ip: 192.168.1.1
loopback_ip: 10.1.1.1
interfaces:
  - name: GigabitEthernet0/0
    ip: 192.168.10.1
    mask: 255.255.255.0
  - name: GigabitEthernet0/1
    ip: 192.168.20.1
    mask: 255.255.255.0
```

## 💡 Try It: Organize Your Variables

1. **Create the host_vars directory**:

   ```bash
   mkdir host_vars
   ```

2. **Create device-specific files**:
   - TODO: Create `host_vars/router01.yml` with connection and interface variables
   - TODO: Add device-specific settings like hostname, domain, and management info

3. **Clean up your inventory**:
   - TODO: Remove inline variables from inventory/hosts.yml
   - Keep only essential connection info (ansible_host)

4. **Test variable loading**:

   ```bash
   ansible-inventory -i inventory/hosts.yml --list
   ansible-inventory -i inventory/hosts.yml --host router01
   ```

## 🛠 Building Device Configurations

Create a playbook that uses host variables for device-specific configurations:

```yaml
---
- name: Configure Device-Specific Settings
  hosts: cisco_devices
  gather_facts: no
  
  tasks:
    - name: Configure interface settings
      cisco.ios.ios_interfaces:
        config:
          - name: "{{ item.name }}"
            description: "Configured by Ansible"
            enabled: true
        state: merged
      # TODO: Loop through the interfaces list from host_vars
      
    - name: Configure interface IP addresses  
      cisco.ios.ios_l3_interfaces:
        config:
          - name: "{{ item.name }}"
            ipv4:
              - address: "{{ item.ip }}/{{ item.mask | ipaddr('prefix') }}"
        state: merged
      # TODO: Add loop for interface IP configuration
```

## 🔍 Check Yourself

1. What's the advantage of host_vars over inline inventory variables?
2. How does Ansible know which host_vars file applies to which device?
3. What happens if you define the same variable in both inventory and host_vars?
4. How would you add a new device without editing existing files?
5. Why might you encrypt certain variables in host_vars files?

## 🛡 Security Best Practices

**For sensitive variables, use Ansible Vault**:

```bash
# Create encrypted variable file
ansible-vault create host_vars/router01/vault.yml

# Edit encrypted file  
ansible-vault edit host_vars/router01/vault.yml

# Run playbook with vault password
ansible-playbook -i inventory/hosts.yml --ask-vault-pass configure_devices.yml
```

## 🔗 Essential Resources

- [Ansible Variable Precedence](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable)
- [Organizing Host and Group Variables](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#organizing-host-and-group-variables)
- [Ansible Vault Documentation](https://docs.ansible.com/ansible/latest/user_guide/vault.html)

## 🚀 Next Up

Once you master host variables, you'll learn about `group_vars` to manage settings shared across multiple devices efficiently!

---

**💡 Pro Tip**: Use descriptive filenames and organize complex host_vars into subdirectories (like `host_vars/router01/main.yml` and `host_vars/router01/vault.yml`)
# 04: Group Variables - Shared Configurations

## 🎯 Mission

Master group variables to manage shared settings across multiple network devices efficiently. You'll organize common configurations that apply to device groups while maintaining device-specific customizations through host variables.

## 🎖 Goals

- [ ] Understand group variable precedence and inheritance  
- [ ] Create `group_vars` directory with logical device groupings
- [ ] Configure shared settings for routers, switches, and all devices
- [ ] Combine group and host variables effectively
- [ ] Manage multiple DevNet Sandbox devices with consistent configurations

## 📚 Why This Matters

Network environments have common configurations that should be consistent across device types. Group variables eliminate repetition by applying shared settings to device groups (all routers, all switches, or all devices). This ensures consistency while reducing maintenance overhead - change a DNS server once in group_vars instead of updating every device individually.

## 🔑 Key Terms

- **group_vars**: Directory containing YAML files with variables that apply to groups of hosts
- **Variable Inheritance**: How devices inherit variables from multiple groups  
- **all.yml**: Special group file that applies variables to every device in inventory
- **Group Precedence**: Order in which Ansible applies group variables (more specific groups override general ones)
- **DRY Principle**: "Don't Repeat Yourself" - define common settings once in groups

## 🗂 Group Variables Structure

**Organizing by device type and function:**

```bash
group_vars/
├── all.yml              # Variables for ALL devices
├── cisco_devices.yml    # Variables for all Cisco devices  
├── routers.yml          # Variables specific to routers
├── switches.yml         # Variables specific to switches
└── core_network.yml     # Variables for critical infrastructure devices
```

**Variable precedence (most specific wins):**

1. Host variables (host_vars/router01.yml) - **Highest Priority**
2. Group variables for specific groups (group_vars/routers.yml)  
3. Group variables for parent groups (group_vars/cisco_devices.yml)
4. Group variables for all hosts (group_vars/all.yml) - **Lowest Priority**

## 🛠 Example Group Variables

**group_vars/all.yml** - Settings for every device:

```yaml
# Global settings applied to ALL devices
ntp_servers:
  - 192.168.1.100
  - 192.168.1.101

snmp_community: lab_readonly
domain_name: lab.local
timezone: EST -5

# Common Ansible connection settings  
ansible_connection: ansible.netcommon.network_cli
ansible_network_os: ios
ansible_user: admin
# Note: Passwords should be in vault files for security
```

**group_vars/routers.yml** - Router-specific settings:

```yaml
# Configuration specific to routers
routing_protocol: ospf
ospf_process_id: 1
ospf_area: 0

# Default router interfaces
default_interfaces:
  - GigabitEthernet0/0
  - GigabitEthernet0/1
  - Loopback0

# Router-specific services
services:
  - ip_routing: yes
  - ip_cef: yes
  - cdp: yes
```

**group_vars/switches.yml** - Switch-specific settings:

```yaml
# Configuration specific to switches  
vtp_mode: transparent
spanning_tree_mode: rapid-pvst

# Default VLANs for lab switches
vlans:
  - id: 10
    name: "SALES"
  - id: 20  
    name: "ENGINEERING"
  - id: 99
    name: "MANAGEMENT"

# Switch-specific services
services:
  - cdp: yes
  - lldp: yes
  - vtp: no
```

## 💡 Try It: Implement Group Variables

1. **Create group_vars directory structure**:

   ```bash
   mkdir group_vars
   ```

2. **Update your inventory with groups**:

   ```yaml
   # TODO: Modify inventory/hosts.yml to include logical groups
   all:
     children:
       routers:
         hosts:
           router01:
             ansible_host: 192.168.1.1
       switches:
         hosts:
           switch01:
             ansible_host: 192.168.1.2
           switch02:
             ansible_host: 192.168.1.3
   ```

3. **Create group variable files**:
   - TODO: Create `group_vars/all.yml` with global settings
   - TODO: Create `group_vars/routers.yml` with router-specific configs
   - TODO: Create `group_vars/switches.yml` with switch-specific configs

4. **Test variable resolution**:

   ```bash
   ansible-inventory -i inventory/hosts.yml --host router01
   ansible-inventory -i inventory/hosts.yml --host switch01
   ```

## 🎮 Multi-Device Playbook

Create a playbook that leverages both group and host variables:

```yaml
---
- name: Apply Common Network Settings
  hosts: all
  gather_facts: no
  
  tasks:
    - name: Configure NTP servers
      cisco.ios.ios_ntp:
        server: "{{ item }}"
        state: present
      # TODO: Loop through ntp_servers from group_vars/all.yml
      
    - name: Configure hostname from host variables
      cisco.ios.ios_config:
        lines:
          - "hostname {{ hostname }}"
      # TODO: This uses hostname from host_vars files

- name: Router-Specific Configuration  
  hosts: routers
  gather_facts: no
  
  tasks:
    - name: Enable routing services
      cisco.ios.ios_config:
        lines:
          - "ip routing"
          - "ip cef"
      # TODO: Use services list from group_vars/routers.yml

- name: Switch-Specific Configuration
  hosts: switches
  gather_facts: no
  
  tasks:
    - name: Configure VLANs
      cisco.ios.ios_vlans:
        config:
          - vlan_id: "{{ item.id }}"
            name: "{{ item.name }}"
        state: merged
      # TODO: Loop through vlans from group_vars/switches.yml
```

## 🔍 Check Yourself

1. What's the difference between `group_vars/all.yml` and `group_vars/cisco_devices.yml`?
2. How would you override a group variable for a specific device?
3. What happens when the same variable is defined in multiple group files?
4. How do you determine which group a device belongs to?
5. Why might you create nested groups in your inventory?

## 🛠 Variable Precedence Testing

**Test variable precedence with this debug playbook:**

```yaml
---
- name: Test Variable Precedence
  hosts: router01
  gather_facts: no
  
  tasks:
    - name: Show variable resolution order
      debug:
        msg:
          - "Domain from groups: {{ domain_name }}"
          - "NTP servers: {{ ntp_servers }}"
          - "Device hostname: {{ hostname }}"
          - "Routing protocol: {{ routing_protocol | default('not set') }}"
```

## 🔗 Essential Resources

- [Ansible Group Variables](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#organizing-host-and-group-variables)
- [Variable Precedence Rules](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#understanding-variable-precedence)
- [Inventory Group Patterns](https://docs.ansible.com/ansible/latest/user_guide/intro_patterns.html)

## 🚀 Next Up

With organized variables mastered, you'll learn Jinja2 templating to create dynamic configurations that adapt based on your device variables!

---

**💡 Pro Tip**: Start with broad groups (all.yml) and get more specific (routers.yml, switches.yml). Use host_vars only for device-unique settings!

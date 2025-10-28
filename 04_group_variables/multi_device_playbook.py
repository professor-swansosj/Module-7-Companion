"""
Multi-device playbook template that uses group and host variables

TODO: Create this as multi_device_config.yml in your project root
"""

playbook_template = """
---
# Apply settings to ALL devices using group_vars/all.yml
- name: Global Network Configuration
  hosts: all
  gather_facts: no
  
  tasks:
    - name: Configure global domain name
      cisco.ios.ios_config:
        lines:
          - "ip domain-name {{ domain_name }}"
      # TODO: Uses domain_name from group_vars/all.yml
      
    - name: Configure NTP servers
      cisco.ios.ios_ntp:
        server: "{{ item }}"
        state: present
      loop: "{{ ntp_servers }}"
      # TODO: Loops through NTP servers from group_vars/all.yml

# Router-specific configuration using group_vars/routers.yml
- name: Router Configuration
  hosts: routers  
  gather_facts: no
  
  tasks:
    - name: Enable routing services
      cisco.ios.ios_config:
        lines:
          - "ip routing"
          - "ip cef"
      when: enable_ip_routing | default(false)
      # TODO: Uses variables from group_vars/routers.yml
      
    - name: Configure OSPF
      cisco.ios.ios_config:
        lines:
          - "router ospf {{ ospf_process_id }}"
          - "network 0.0.0.0 255.255.255.255 area {{ ospf_area }}"
      # TODO: Uses OSPF settings from group_vars/routers.yml

# Switch-specific configuration using group_vars/switches.yml  
- name: Switch Configuration
  hosts: switches
  gather_facts: no
  
  tasks:
    - name: Configure VLANs
      cisco.ios.ios_vlans:
        config:
          - vlan_id: "{{ item.id }}"
            name: "{{ item.name }}"
        state: merged
      loop: "{{ vlans }}"
      # TODO: Creates VLANs from group_vars/switches.yml
      
    - name: Configure spanning tree mode
      cisco.ios.ios_config:
        lines:
          - "spanning-tree mode {{ spanning_tree_mode }}"
      # TODO: Uses STP mode from group_vars/switches.yml
"""

print("Create the multi-device playbook above to test group variables!")
print("Run with: ansible-playbook -i inventory/hosts.yml multi_device_config.yml")
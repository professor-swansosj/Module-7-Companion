# Example interface template for more complex configurations
# TODO: Create this as templates/interface_config.j2

interface_template = '''
{#
  Advanced Interface Template  
  Handles different interface types with conditional logic
#}

{% for interface in interfaces %}
!
interface {{ interface.name }}
 description {{ interface.description | default("Managed by Ansible") }}
 
{# Physical interface configuration #}
{% if interface.type == "physical" %}
 duplex auto
 speed auto
{% endif %}

{# IP Configuration #}
{% if interface.ip is defined %}
 ip address {{ interface.ip }} {{ interface.mask }}
{% elif interface.dhcp | default(false) %}
 ip address dhcp
{% endif %}

{# VLAN Configuration for switch ports #}
{% if interface.mode is defined %}
 switchport mode {{ interface.mode }}
{% if interface.vlan is defined %}
 switchport {{ interface.mode }} vlan {{ interface.vlan }}
{% endif %}
{% if interface.allowed_vlans is defined %}
 switchport trunk allowed vlan {{ interface.allowed_vlans | join(',') }}
{% endif %}
{% endif %}

{# Security settings #}
{% if interface.port_security | default(false) %}
 switchport port-security
 switchport port-security maximum {{ interface.max_mac | default(1) }}
{% endif %}

 no shutdown
{% endfor %}
'''

# Example of adding VLAN interface variables to host_vars:
vlan_interface_vars = '''
# TODO: Add to your host_vars files for switches
vlan_interfaces:
  - vlan_id: 10
    description: "Sales VLAN Interface"  
    ip: 192.168.10.1
    mask: 255.255.255.0
  - vlan_id: 20
    description: "Engineering VLAN Interface"
    ip: 192.168.20.1
    mask: 255.255.255.0
'''

print("Advanced template example above shows conditional logic and complex configurations!")
print("Add the VLAN interface variables to test more template features.")
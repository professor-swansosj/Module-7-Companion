# Module 7: Infrastructure as Code with Ansible

**Software Defined Networking - Network Automation Course**  
**Florida State College at Jacksonville**

## Course Information

- **Course**: Software Defined Networking (Network Automation)
- **Level**: Senior Level
- **Prerequisites**: Linux+, Introduction to Python, Cisco 1, 2, 3
- **Module**: 7 - Infrastructure as Code with Ansible

## Module Overview

This companion repository contains hands-on exercises and examples for Module 7, focusing on Infrastructure as Code using Ansible for network automation. Students will learn to structure Ansible projects, manage configurations through code, and leverage Jinja2 templating for dynamic network configurations.

## Table of Contents

### 📚 Learning Objectives

By the end of this module, students will be able to:

1. **Introduction to Ansible** - Understand Ansible's role in network automation
2. **Build Basic Inventory** - Create inventory files and run general playbooks against Cisco devices
3. **Host Variables** - Implement device-specific configurations using host_vars
4. **Group Variables** - Manage shared configurations across device groups using group_vars
5. **Jinja2 Templates** - Create dynamic Cisco configuration templates
6. **Configuration Rendering** - Generate configurations using both host_vars and group_vars

### 📁 Project Structure

```yaml
Module-7-Companion/
├── README.md
├── ansible.cfg                 # Ansible configuration file
├── inventory/                  # Inventory files
│   └── hosts.yml
├── host_vars/                  # Host-specific variables
│   ├── switch01.yml
│   ├── switch02.yml
│   └── router01.yml
├── group_vars/                 # Group-specific variables
│   ├── switches.yml
│   ├── routers.yml
│   └── all.yml
├── templates/                  # Jinja2 configuration templates
│   ├── interface_config.j2
│   ├── vlan_config.j2
│   └── base_config.j2
├── playbooks/                  # Ansible playbooks for exercises
│   ├── 01_basic_connection.yml
│   ├── 02_gather_facts.yml
│   ├── 03_host_vars_demo.yml
│   ├── 04_group_vars_demo.yml
│   └── 05_template_rendering.yml
└── sample_data/               # Sample data files
    ├── vlans.json
    ├── interfaces.csv
    └── network_config.yml
```

## 🚀 Getting Started

### Prerequisites Setup

1. Ensure Ansible is installed on your system
2. Install the Cisco collection for Ansible:

   ```bash
   ansible-galaxy collection install cisco.ios
   ```

3. Have access to Cisco devices (physical, GNS3, or CML)

### Quick Start Guide

1. Clone this repository to your local machine
2. Navigate to the project directory
3. Review the `ansible.cfg` configuration
4. Update the inventory file with your device information
5. Start with the basic playbooks in sequential order

## 📖 Exercise Flow

### Exercise 1: Introduction to Ansible

- Review project structure
- Understand Ansible configuration file
- Learn inventory file basics

### Exercise 2: Basic Inventory and Playbook

- Configure inventory with Cisco devices
- Run basic connectivity tests
- Execute simple configuration tasks

### Exercise 3: Host Variables Implementation

- Create device-specific variables
- Apply configurations using host_vars
- Understand variable precedence

### Exercise 4: Group Variables Implementation  

- Define group-level configurations
- Apply shared settings across device groups
- Combine host_vars and group_vars

### Exercise 5: Jinja2 Templates

- Create dynamic configuration templates
- Use conditional logic in templates
- Implement loops and filters

### Exercise 6: Full Configuration Rendering

- Combine all concepts
- Generate complete device configurations
- Deploy configurations to devices

## 🔧 Configuration Examples

Each directory contains detailed examples and comments to help you understand:

- **Inventory**: Device grouping and connection parameters
- **Host Variables**: Device-specific IP addresses, interfaces, VLANs
- **Group Variables**: Common settings like SNMP, NTP, domain information
- **Templates**: Reusable Jinja2 templates for various configuration sections

## 📝 Notes for Students

- Follow the exercises in the suggested order
- Modify the sample data to match your lab environment
- Experiment with different variable combinations
- Test templates before applying to production devices
- Always backup device configurations before making changes

## 🆘 Troubleshooting

Common issues and solutions:

- **Connection Issues**: Check inventory file credentials and IP addresses
- **Template Errors**: Validate Jinja2 syntax and variable names  
- **Variable Conflicts**: Review variable precedence rules
- **Playbook Failures**: Check device compatibility and available modules

## 📚 Additional Resources

- [Ansible Network Documentation](https://docs.ansible.com/ansible/latest/network/index.html)
- [Cisco IOS Collection](https://galaxy.ansible.com/cisco/ios)
- [Jinja2 Template Documentation](https://jinja.palletsprojects.com/)

---

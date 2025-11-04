# Module 7 Companion - Infrastructure as Code with Ansible

## Software Defined Networking Course

> **Master Infrastructure as Code!** This companion repository provides a progressive learning path for Infrastructure as Code using Ansible for network automation. You'll start with basic concepts and gradually build expertise through hands-on exercises with Cisco DevNet Sandbox devices.

## 🎯 What You'll Practice

Transform your network automation skills by learning Infrastructure as Code principles with Ansible. Build from basic concepts to advanced automation patterns that scale across enterprise environments.

## 📋 Prerequisites

- **Course**: Software Defined Networking (Network Automation)
- **Level**: Senior Level
- **Prerequisites**: Linux+, Introduction to Python, Cisco 1, 2, 3
- **Module 7**: Infrastructure as Code with Ansible

## 🗂 Learning Path

**Follow these topics in order for the best learning experience:**

### Learning Progression

**🎯 Start Here:** Complete each section before moving to the next one.

1. **[Section 01 - Ansible Introduction](./01_ansible_introduction/)** - Set up your environment, learn Ansible basics, and secure credentials with Vault
2. **[Section 02 - Basic Inventory](./02_basic_inventory/)** - Connect to devices and run your first playbooks  
3. **[Section 03 - Host Variables](./03_host_variables/)** - Organize device-specific configurations cleanly
4. **[Section 04 - Group Variables](./04_group_variables/)** - Manage shared settings across device groups
5. **[Section 05 - Jinja Templates](./05_jinja_templates/)** - Create dynamic, data-driven configurations

**By the end of this module, you'll be able to:**

- Configure and use Ansible for network device management
- Secure credentials properly using Ansible Vault
- Organize variables effectively using host_vars and group_vars  
- Create reusable Jinja2 templates for configuration generation
- Build scalable automation that works across multiple devices
- Apply Infrastructure as Code principles to network operations

### Project Structure

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

## 🚀 Getting Hands-On

### Setup

Before starting the companion exercises:

1. **Ansible Installation**: Ensure Ansible is installed on your system
2. **Cisco Collection**: Install the required Cisco modules:

   ```bash
   ansible-galaxy collection install cisco.ios
   ```

3. **DevNet Sandbox**: Reserve a Cisco DevNet Sandbox device for hands-on practice
4. **Text Editor**: Use VS Code or your preferred editor for YAML files

## 🎯 Practice Callouts

**Follow the Learning Path:**

1. **Start with Section 01** - Each section builds on the previous one
2. **Complete all TODO items** - These guide your hands-on practice  
3. **Test your work** - Run the commands and playbooks as you progress
4. **Experiment** - Modify examples to deepen your understanding
5. **Ask questions** - Use the class discussion board for help

**📁 Working Directory Setup:**

```bash
# Clone and navigate to the companion
git clone <repository-url> Module-7-Companion
cd Module-7-Companion

# Start with topic 01
cd 01_ansible_introduction
```

## 🎖 What You'll Build

As you progress through the topics, you'll build a complete Ansible automation system:

### Progressive Skills Development

#### Section 01-02: Foundation

- Basic Ansible configuration and secure credential management
- Device connectivity and simple automation tasks

#### Section 03-04: Organization

- Clean variable management using host_vars and group_vars
- Multi-device configurations with shared and unique settings

#### Section 05: Advanced

- Dynamic configuration generation using Jinja2 templates
- Scalable, maintainable automation workflows

### Final Project Structure

By completion, your project will look like:

```bash
Module-7-Companion/
├── ansible.cfg              # Ansible configuration
├── inventory/
│   └── hosts.yml            # Clean device inventory
├── host_vars/               # Device-specific variables
│   ├── router01.yml
│   └── switch01.yml
├── group_vars/              # Shared group variables  
│   ├── all.yml
│   ├── routers.yml
│   └── switches.yml
├── templates/               # Jinja2 configuration templates
│   ├── base_config.j2
│   └── vlan_config.j2
└── playbooks/               # Automation playbooks
    └── deploy_configs.yml
```

## � Configuration Examples

Each directory contains detailed examples and comments to help you understand:

- **Inventory**: Device grouping and connection parameters
- **Host Variables**: Device-specific IP addresses, interfaces, VLANs
- **Group Variables**: Common settings like SNMP, NTP, domain information
- **Templates**: Reusable Jinja2 templates for various configuration sections

## 🏆 Success Criteria

**Best Practices for Learning:**

- **Start Simple**: Complete topics in order - each builds on the previous
- **Practice First**: Complete TODO items before reading ahead  
- **Test Everything**: Run commands and verify results as you go
- **Experiment**: Modify examples to see what happens
- **Document**: Add comments explaining what you learn
- **Ask Questions**: Use the discussion board when stuck

**Technical Reminders:**

- **Security First**: Always use Ansible Vault for credentials
- Keep your DevNet Sandbox reservation active
- Use version control (git) to track your progress  
- Test configurations in lab environment only
- Always backup device configs before applying changes

## 🆘 Getting Help

**🔧 Common Issues:**

- **Connection Problems**: Verify DevNet Sandbox IP and credentials
- **Module Errors**: Ensure `cisco.ios` collection is installed
- **Template Issues**: Check Jinja2 syntax and variable names
- **Playbook Failures**: Verify device OS compatibility

**Where to Ask for Help:**

- Class discussion board for technical questions
- Office hours for concept clarification  
- Study groups for collaborative learning

**Self-Help Commands:**

```bash
ansible --version                    # Check Ansible installation
ansible-galaxy list                  # Verify installed collections  
ansible-inventory --list             # Debug inventory issues
ansible-config view                  # Check configuration settings
```

## 🔗 Additional Resources

- [Ansible Network Documentation](https://docs.ansible.com/ansible/latest/network/index.html)
- [Cisco IOS Collection](https://galaxy.ansible.com/cisco/ios)
- [Jinja2 Template Documentation](https://jinja.palletsprojects.com/)

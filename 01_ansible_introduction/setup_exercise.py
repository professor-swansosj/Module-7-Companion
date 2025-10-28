# TODO: Configure your first Ansible environment with secure credentials
# 
# Your mission: Set up ansible.cfg and secure credential management
# 
# Part 1: Ansible Configuration
# 1. Create ansible.cfg in the root directory (one level up from here)
# 2. Add the basic configuration shown in the README
# 3. Add a comment explaining what host_key_checking = False does
# 4. Test your configuration using: ansible-config view

# Part 2: Secure Credentials (IMPORTANT!)
# 1. Create encrypted vault file: ansible-vault create vault.yml
# 2. Add your DevNet Sandbox credentials to the vault
# 3. Test vault operations: ansible-vault view vault.yml
# 4. Practice editing vault: ansible-vault edit vault.yml

# Research Questions (add your answers as comments):
# Q: Why is gather_facts = False recommended for network devices?
# A: TODO - Add your research here

# Q: What does idempotent mean in Ansible?  
# A: TODO - Add your research here

# Q: Why should credentials never be stored in plain text?
# A: TODO - Add your research here

# Q: How does ansible-vault protect sensitive data?
# A: TODO - Add your research here

vault_example = """
# Example vault.yml content (this will be encrypted):
---
device_username: admin
device_password: your_devnet_password
snmp_community: lab_readonly
"""

print("Complete both ansible.cfg setup AND vault creation before moving to topic 02!")
print("Security first - never store passwords in plain text files!")
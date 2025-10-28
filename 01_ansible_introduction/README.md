# 01: Introduction to Ansible

## 🎯 Mission

Get familiar with Ansible's basic structure and configuration while understanding its role in network automation. You'll set up your first Ansible environment and learn the fundamental concepts.

## 🎖 Goals  

- [ ] Understand what Infrastructure as Code means for network engineers
- [ ] Configure a basic `ansible.cfg` file 
- [ ] Learn Ansible directory structure and best practices
- [ ] Secure credentials using Ansible Vault
- [ ] Explore Ansible's approach to network device management

## 📚 Why This Matters

Ansible revolutionizes network management by treating configurations as code. Instead of manually configuring devices one by one, you define the desired state and let Ansible make it happen consistently across your entire network. Think of it as "configuration blueprints" that you can version, test, and deploy reliably.

## 🔑 Key Terms

- **Infrastructure as Code (IaC)**: Managing network infrastructure through machine-readable files rather than manual processes
- **ansible.cfg**: Configuration file that defines Ansible's behavior and default settings
- **Idempotent**: Running the same command multiple times produces the same result (no unwanted changes)
- **Inventory**: File defining which devices Ansible manages and how to connect to them
- **Playbook**: YAML file containing a series of tasks to execute on target devices
- **Ansible Vault**: Tool for encrypting sensitive data like passwords, API keys, and certificates

## 🛠 Understanding ansible.cfg

The `ansible.cfg` file is Ansible's control center. It tells Ansible:

- Where to find your inventory
- How to connect to devices  
- What security settings to use
- How detailed the output should be

Here's a basic network-focused configuration:

```ini
[defaults]
inventory = inventory/hosts.yml
host_key_checking = False
timeout = 30
gather_facts = False
retry_files_enabled = False

[inventory]
enable_plugins = host_list, script, auto, yaml, ini, toml

[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=60s
pipelining = True
```

## 💡 Try It: Configure Your Environment

1. **Create your ansible.cfg file**:
   - Copy the example above into `ansible.cfg`
   - Add a comment explaining what `host_key_checking = False` does
   - TODO: Research why `gather_facts = False` is useful for network devices

2. **Explore the directory structure**:
   - Create an `inventory` folder
   - TODO: Think about why separating inventory from playbooks is a good practice

3. **Test your setup**:

   ```bash
   ansible --version
   ansible-config view
   ```

## � Securing Credentials with Ansible Vault

**Never put passwords in plain text!** Ansible Vault encrypts sensitive data so you can safely store credentials in your automation projects.

### Why Vault Matters

In enterprise networks, you need to:

- Store device passwords securely
- Share automation projects without exposing credentials
- Meet security compliance requirements
- Rotate passwords without updating every file

### Basic Vault Operations

**Create an encrypted file for secrets:**

```bash
ansible-vault create secrets.yml
```

**Edit existing vault files:**

```bash
ansible-vault edit secrets.yml
```

**Example vault file (secrets.yml):**

```yaml
# This file will be encrypted by Ansible Vault
device_username: admin
device_password: your_secure_password
snmp_community: private_community_string
```

**Use vault variables in inventory:**

```yaml
# inventory/hosts.yml - references vault variables
all:
  children:
    cisco_devices:
      hosts:
        router01:
          ansible_host: 192.168.1.1
          ansible_user: "{{ device_username }}"
          ansible_password: "{{ device_password }}"
```

## 💡 Try It: Secure Your First Credentials

1. **Create a vault file**:

   ```bash
   ansible-vault create vault.yml
   ```

   - Enter a vault password when prompted
   - Add your DevNet Sandbox credentials

2. **Test vault operations**:

   ```bash
   ansible-vault view vault.yml      # View encrypted content
   ansible-vault edit vault.yml      # Modify vault file
   ```

3. **Use vault in playbooks**:

   ```bash
   ansible-playbook --ask-vault-pass playbook.yml
   ```

## �🔍 Check Yourself

1. What does "idempotent" mean in the context of network automation?
2. Why might you want to disable host key checking in a lab environment?
3. What's the difference between a playbook and an inventory file?
4. How does Infrastructure as Code benefit network operations teams?
5. What happens if you run the same Ansible playbook twice?
6. Why should you never store passwords in plain text files?
7. What command creates a new encrypted vault file?

## 🔗 Essential Resources

- [Ansible Configuration Settings](https://docs.ansible.com/ansible/latest/reference_appendices/config.html)
- [Ansible for Network Automation](https://docs.ansible.com/ansible/latest/network/getting_started/index.html)
- [Ansible Vault Documentation](https://docs.ansible.com/ansible/latest/user_guide/vault.html)
- [Infrastructure as Code Principles](https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html)

## 🚀 Next Up

Once you're comfortable with Ansible configuration, you'll move on to creating your first inventory file and connecting to actual network devices!

---

**💡 Pro Tip**: Always use Ansible Vault for credentials, even in lab environments. It's much easier to develop secure habits from the start than to fix insecure practices later!


## VaultX

**Description**  
VaultX is a Bash script designed to gather and display critical operational information from a HashiCorp Vault cluster. It provides detailed insights into Vault cluster nodes, Raft autopilot state, replication status, license information, and more, all formatted in a color-coded and easy-to-read display.

### Features:
- **Cluster Node Discovery**: Automatically detects and lists all nodes within the Vault cluster.
- **Vault Status**: Retrieves and displays the status of each node in the cluster.
- **Raft Information**: Provides details about Raft peers and the autopilot configuration/state.
- **Replication Status**: Displays the current replication status in JSON format.
- **License Information**: Retrieves and shows Vault's license information.
- **Colorized Output**: Key details are highlighted in various colors for better readability.

### Prerequisites:
- **jq**: The script requires `jq` to process JSON data.
- **Vault CLI**: You must have the Vault CLI installed and configured.

### Installation & Usage:
1. Clone the repository and move the script to `/usr/local/bin/` for easier access:
   ```bash
   git clone https://github.com/zbaban/vaultx.git
   sudo mv vaultx/vaultx /usr/local/bin/
   sudo chmod +x /usr/local/bin/vaultx
   ```

2. Install `jq` (if not already installed) using your system’s package manager:
   ```bash
   sudo apt-get install jq    # For Debian/Ubuntu
   sudo yum install jq        # For RHEL/CentOS
   sudo dnf install jq        # For Fedora
   sudo zypper install jq     # For SUSE
   ```

3. **Vault Token**: If your VAULT_TOKEN is set as an environment variable, it will be used to display the result. Otherwise, you’ll be prompted to enter your Vault token for authentication to access the Vault cluster.

4. Run the script:
   ```bash
   vaultx
   ```

### Example Output:
When executed, the script will display:
- Vault status for each node in the cluster.
- Raft peer details.
- Vault license information.
- Raft autopilot state and configuration.
- Replication status (if applicable).

### Output Sample:
- Cluster nodes and their statuses.
- Raft peer details and autopilot state.
- Replication status (in JSON format).

This script simplifies monitoring and managing a HashiCorp Vault cluster by consolidating essential information into a single interface for quick and easy reference.

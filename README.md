## VaultX

**Description**  
VaultX is a Bash script designed to gather and display important operational information from a HashiCorp Vault cluster. It provides detailed information on Vault cluster nodes, Raft autopilot state, replication status, license details, and more, all in an easily readable and color-coded format.

### Features:
- **Cluster Node Discovery**: Automatically discovers and lists all nodes in the Vault cluster.
- **Vault Status**: Retrieves and displays the status of each node in the cluster.
- **Raft Information**: Provides details on Raft peers and the autopilot configuration/state.
- **Replication Status**: Displays the current replication status in JSON format.
- **License Information**: Retrieves and displays Vault's license information.
- **Colorized Output**: Key details are highlighted for better readability.

### Prerequisites:
- **jq**: The script depends on `jq` for processing JSON data. The script includes functionality to automatically install `jq` if it's not already present on your system.
- **Vault CLI**: The Vault CLI must be installed and configured.

### Installation:
To install `jq` (if not already installed), the script will automatically detect your package manager (e.g., `apt-get`, `yum`, `dnf`, or `zypper`) and attempt to install it. Alternatively, you can install it manually:
```bash
sudo apt-get install jq    # For Debian/Ubuntu
sudo yum install jq        # For RHEL/CentOS
sudo dnf install jq        # For Fedora
sudo zypper install jq     # For SUSE
```

### Usage:
1. **Vault Token**: When prompted, enter your Vault token to authenticate and access the Vault cluster.
2. The script will discover the nodes in the Vault cluster and display their statuses along with other critical details.

### Example:
```bash
./vaultx.sh
```

You will be prompted to enter your Vault token, after which the script will display the following information:
- Vault status for each node
- Raft peer list
- Vault license information
- Raft autopilot state and configuration
- Replication status (if applicable)

### Output Sample:
- Cluster nodes with status
- Raft peer details and autopilot state
- Replication status (JSON format)

This script simplifies monitoring and managing a HashiCorp Vault cluster by consolidating critical information into a single interface.

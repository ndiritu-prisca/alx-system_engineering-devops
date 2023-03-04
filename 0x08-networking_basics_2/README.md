# 0x08. Networking basics #1

## Learning Objectives
- localhost/127.0.0.1
- 0.0.0.0
- /etc/hosts
- Displaying a machine’s active network interfaces

## TASKS

### 0
Write a Bash script that configures an Ubuntu server with the below requirements.
- Requirements:
  - `localhost` resolves to `127.0.0.2`
  - `facebook.com` resolves to `8.8.8.8`.

### 1
Write a Bash script that displays all active IPv4 IPs on the machine it’s
executed on.

### 2
Write a Bash script that listens on port `98` on `localhost`
- Test
  - Connecting to localhost on port 98 using telnet and typing some text.
  `telnet localhost 98` on terminal 1
  - `sudo ./100-port_listening_on_localhost` on terminal 0

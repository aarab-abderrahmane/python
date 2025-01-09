import subprocess

def get_ip_info():
    ifconfig_output = subprocess.check_output("ifconfig", shell=True, text=True)

    print(ifconfig_output,"\n")
              

    private_ip = ""
    if "inet " in ifconfig_output:
        lines = ifconfig_output.splitlines()
        for line in lines:
            if "inet " in line and "127.0.0.1" not in line:  # استبعاد الـ loopback
                private_ip = line.split()[1]
                break

    broadcast = ""
    if "broadcast" in ifconfig_output:
        lines = ifconfig_output.splitlines()
        for line in lines:
            if "broadcast" in line:
                broadcast = line.split()[-1]
                break

    netmask = ""
    if "netmask" in ifconfig_output:
        lines = ifconfig_output.splitlines()
        for line in lines:
            if "netmask" in line:
                netmask = line.split()[-1]
                break

    public_ip = subprocess.check_output("curl -s ifconfig.me", shell=True, text=True).strip()

    print(f"IPv4: {private_ip}")
    print(f"(Private IP): {private_ip}")
    print(f"(Public IP): {public_ip}")
    print(f"(Netmask): {netmask}")
    print(f"(Broadcast): {broadcast}")

get_ip_info()

import paramiko

def exec_cmd(ip, usr_name, password, cmd_list):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, usr_name, password, timeout=5)
        for cmd in cmd_list:
            ssh.exec_command(cmd)
        ssh.close()
    except:
        raise
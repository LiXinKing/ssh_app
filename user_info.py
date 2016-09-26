g_ip_2_user_info ={
    "192.168.146.133" : ("root", "jinlixin"),
}

def get_user_info_by_ip(exec_ip):
    return g_ip_2_user_info[exec_ip]
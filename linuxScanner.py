import sys
from fabric import Connection

# Easily add task(s) to run here.
to_do_tasks = [
    "history",
    "hostname",
    "id",
    "uname -a",
    "cat /proc/version",
    "cat /etc/issue",
    "echo $PATH",
    "find / -type f -perm -4000 2>/dev/null",
    "find / -type f -perm -6000 2>/dev/null",
    "cat /etc/passwd"
]

def initialize_connection_exec_command():
    
    # Check if number of system arguments is correct.
    # Note that first argument is the script itself being called, in case of debugging issue.
    if len(sys.argv) != 4:
        print("3 arguments required...")
        print("./linuxScanner.py user ipAddress password")
        exit(1)
        
    # Collect connection information before initialization.
    login_user = sys.argv[1]
    address_ip = sys.argv[2]
    user_password = sys.argv[3]
    
    c = Connection(user=login_user, host=address_ip, connect_kwargs={"password":user_password}, port=22)
   
    print(f"\nConnection configuration set as: {login_user}@{address_ip}\n")
    print("Now attempting to connect...\n")
    
    for task in to_do_tasks: 
        
        output_separator = "----------------------------------------------------------------------------------"
        
        print("Now running: " + task + "\n")
        print(output_separator)
        c.run(task, warn=True)
        print(output_separator)
        print("\n")

initialize_connection_exec_command()

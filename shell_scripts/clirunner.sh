import os
os.system("ls -l")

import subprocess
# test = subprocess.Popen(["ping","-W","2","-c", "1", "192.168.1.70"], stdout=subprocess.PIPE)
# output = test.communicate()[0]


clean = subprocess.Popen(["sudo","mn","-c"], stdout=subprocess.PIPE)
output = clean.communicate()[0]

bw_hi = 5
bw_lo = 0.5

run_net = subprocess.Popen(["sudo","python","mininet/custom/basic.py",str(bw_hi),str(bw_lo)])

cli_server_cmd = subprocess.Popen(["py","net.get('h2').cmd('./D-ITG-2.8.1-r1023/bin/ITGRecv &')"])
#,stdout=subprocess.PIPE)
cli_client_cmd = subprocess.Popen(["py","net.get('h1').cmd('./D-ITG-2.8.1-r1023/bin/ITGSend cc-final-project/shell_scripts/multiflow-tcp.sh -l ./cc-final-project/server_outputs/TO_DELETE.log -x ./cc-final-project/server_outputs/noqueue-tcp-5-2.log')"])
#,stdout=subprocess.PIPE)

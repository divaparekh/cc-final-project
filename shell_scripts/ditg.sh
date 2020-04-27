py net.get('h2').cmd('./D-ITG-2.8.1-r1023/bin/ITGRecv &')
py net.get('h1').cmd('./D-ITG-2.8.1-r1023/bin/ITGSend cc-final-project/shell_scripts/multiflow.sh -l ./cc-final-project/server_outputs/TO_DELETE.log -x ./cc-final-project/server_outputs/codel-5-4.log')

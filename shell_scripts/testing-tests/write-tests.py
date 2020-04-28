# TCP NoQueue, high bandwidth = 5
tcp_noqueue_5 = open("ditg-tcp-noqueue-5.sh", "w")

tcp_noqueue_5.write("py net.get('h2').cmd('./D-ITG-2.8.1-r1023/bin/ITGRecv &')")

for index in range(1, 100):
    trial = str(index)
    tcp_noqueue_5.write("py net.get('h1').cmd('./D-ITG-2.8.1-r1023/bin/ITGSend cc-final-project/shell_scripts/multiflow-tcp.sh -l ./cc-final-project/server_outputs/TO_DELETE.log -x ./cc-final-project/server_outputs/noqueue-tcp-5-" + trial + ".log')")

tcp_noqueue_5.close()


#TCP CoDel, high bandwidth = 5
tcp_codel_5 = open("ditg-tcp-codel-5.sh", "w")

tcp_codel_5.write("py net.get('h2').cmd('./D-ITG-2.8.1-r1023/bin/ITGRecv &')")

for index in range(1, 100):
    trial = str(index)
    tcp_noqueue_5.write("py net.get('h1').cmd('./D-ITG-2.8.1-r1023/bin/ITGSend cc-final-project/shell_scripts/multiflow-tcp.sh -l ./cc-final-project/server_outputs/TO_DELETE.log -x ./cc-final-project/server_outputs/codel-tcp-5-" + trial + ".log')")

tcp_codel_5.close()


# TCP NoQueue, high bandwidth = 10
tcp_noqueue_10 = open("ditg-tcp-noqueue-10.sh", "w")

tcp_noqueue_10.write("py net.get('h2').cmd('./D-ITG-2.8.1-r1023/bin/ITGRecv &')")

for index in range(1, 100):
    trial = str(index)
    tcp_noqueue_10.write("py net.get('h1').cmd('./D-ITG-2.8.1-r1023/bin/ITGSend cc-final-project/shell_scripts/multiflow-tcp.sh -l ./cc-final-project/server_outputs/TO_DELETE.log -x ./cc-final-project/server_outputs/noqueue-tcp-10-" + trial + ".log')")

tcp_noqueue_10.close()


#TCP CoDel, high bandwidth = 10
tcp_codel_10 = open("ditg-tcp-codel-10.sh", "w")

tcp_codel_10.write("py net.get('h2').cmd('./D-ITG-2.8.1-r1023/bin/ITGRecv &')")

for index in range(1, 100):
    trial = str(index)
    tcp_noqueue_10.write("py net.get('h1').cmd('./D-ITG-2.8.1-r1023/bin/ITGSend cc-final-project/shell_scripts/multiflow-tcp.sh -l ./cc-final-project/server_outputs/TO_DELETE.log -x ./cc-final-project/server_outputs/codel-tcp-10-" + trial + ".log')")

tcp_codel_10.close()

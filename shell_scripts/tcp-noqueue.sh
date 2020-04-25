h2 iperf -s --len 300 -fk -e -p 5001 -i 5 --time 30 > /home/divaparekh/cc-final-project/server_outputs/tcp-noqueue &
h1 iperf -c h2 --len 300 -fk --interval 5 --time 30 --listenport 5001 -P 6

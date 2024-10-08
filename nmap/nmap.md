## Using Proxy Servers

The use of proxy servers can help hide your source. Nmap offers the option --proxies that takes a list of a comma-separated list of proxy URLs. Each URL should be expressed in the format proto://host:port. Valid protocols are HTTP and SOCKS4; moreover, authentication is not currently supported.

Consider the following example. Instead of running nmap -sS 10.10.104.142, you would edit your Nmap command to something like `nmap -sS HTTP://PROXY_HOST1:8080,SOCKS4://PROXY_HOST2:4153 10.10.104.142`. This way, you would make your scan go through HTTP proxy host1, then SOCKS4 proxy host2, before reaching your target. It is important to note that finding a reliable proxy requires some trial and error before you can rely on it to hide your Nmap scan source.

If you use your web browser to connect to the target, it would be a simple task to pass your traffic via a proxy server. Other network tools usually provide their own proxy settings that you can use to hide your traffic source.i

---

    Evasion Approach                            |	        Nmap Argument
------------------------------------------------|------------------------------------------
Hide a scan with decoys 	                    |        `-D DECOY1_IP1,DECOY_IP2,ME`
Hide a scan with random decoys 	                |        `-D RND,RND,ME`
Use an HTTP/SOCKS4 proxy to relay connections 	|        `--proxies PROXY_URL`
Spoof source MAC address 	                    |        `--spoof-mac MAC_ADDRESS`
Spoof source IP address 	                    |        `-S IP_ADDRESS`
Use a specific source port number 	            |        `-g PORT_NUM or --source-port PORT_NUM`
Fragment IP data into 8 bytes	                |        `-f`
Fragment IP data into 16 bytes	                |        `-ff`
Fragment packets with given MTU 	            |        `--mtu VALUE`
Specify packet length 	                        |        `--data-length NUM`
Set IP time-to-live field 	                    |        `--ttl VALUE`
Send packets with specified IP options 	        |        `--ip-options OPTIONS`
Send packets with a wrong TCP/UDP checksum 	    |        `--badsum`
-----------------------------------------------------------------------------------------------------

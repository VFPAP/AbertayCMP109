# Building a Network Assessed Lab

During the first term of the first year, I've built this network using Cisco Packet Tracer for an assignment of this module.

## Details

* Routers Subnet: 192.168.0.0/29 – 6 usable host per subnet – 32 possible subnets

  - Router1 – Finance:

    - IP: 192.168.0.1
    - Mask: 255.255.255.248

  - Router2 – Sales:

    - IP: 192.168.0.2
    - Mask: 255.255.255.248

  - Router3 – Marketing:

    - IP: 192.168.0.3
    - Mask: 255.255.255.248

  - Router4 – Customer Services:

    - IP: 192.168.0.4
    - Mask: 255.255.255.248


* Hosts Subnet: 192.168.1.0/29 – 6 usable host per subnet – 32 possible subnets

  - Finance: 192.168.1.0/29
    - Gateway: 192.168.1.1
    - Computers: 192.168.1.2 - 192.168.1.6

  - Sales: 192.168.1.8/29
    - Gateway: 192.168.1.9
    - Computers: 192.168.1.10 - 192.168.1.14

  - Marketing: 192.168.1.16/29
    - Gateway: 192.168.1.17
    - Computers: 192.168.1.18 - 192.168.1.22

  - Customer Services: 192.168.1.24/29
    - Gateway: 192.168.1.25
    - Computers: 192.168.1.26 - 192.168.1.30
 

* Routing between Routers:

  - Finance (192.168.1.0/29) knows that Sales (192.168.1.8/29) is accessible through 192.168.0.2 and Customer Services (192.168.1.24/29) is accessible through 192.168.0.4.
  - Sales (192.168.1.8/29) knows that Finance (192.168.1.0/29) is accessible through 192.168.0.1 and Customer Services (192.168.1.24/29) is accessible through 192.168.0.4.
  - Marketing (192.168.1.16/29) don’t have access to any other department.
  - Customer Services (192.168.1.24/29) knows that Finance (192.168.1.0/29) is accessible through 192.168.0.1 and Sales (192.168.1.8/29) is accessible through 192.168.0.2.

## Screenshot
![screenshot](/Networking/network.png)

## Author
**Vasco Pinto**
<br>Twitter: [@0xVFPAP](https://twitter.com/0xVFPAP)
<br>LinkedIn: [Vasco Pinto](https://linkedin.com/in/vascopinto97)
<br>OpenBugBounty: [VFPAP](https://www.openbugbounty.org/researchers/VFPAP)

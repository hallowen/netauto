## Cisco ACI(Cisco Application Centric Infrastructure) ##

- Cisco's Software Defined Networking Solution.
- Policy driven infrastructure.
- Intent Based Networking.
- ACI helps to change the way in which we manage our DC networks.
- It works on based on whitelist model. Better security.
- Uses Spine & Leaf model.
- No Spanning-Tree
- Programmability
- Centralized management using APIC.
- ACI is making use of VXLAN.
- It makes use of API's
- CLI doesn't have native access to the controller.

Tenant -> VRF/Context -> Bridge-Domain -> VLAN

There are 3 major components within ACI

1. Nexus 9500 modular switches. These are having more line cards.
2. Nexus 9300 fixed configuration switches
3. APIC Controller: These are usually deployed in a cluster of 3 controllers. They are deployed on Cisco UCS servers. These are connected to the leaf switches.

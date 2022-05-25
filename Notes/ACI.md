# Cisco ACI(Cisco Application Centric Infrastructure)

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
- ACI and NXOS mode are mutually exclusive.

Tenant -> VRF/Context -> Bridge-Domain -> VLAN

There are 3 major components within ACI

1. Nexus 9500 modular switches. These are having more line cards.
2. Nexus 9300 fixed configuration switches
3. APIC Controller: These are usually deployed in a cluster of 3 controllers. They are deployed on Cisco UCS servers. These are connected to the leaf switches.

- In the case of ACI everything is logical.

***EPG(Endpoint Groups)***

These are a collection of endpoints. Endpoints can be servers, VM's etc. Members within an EPG can talk to each other by default. Multiple endpoint groups will be placed inside a Bridge-Domain. ACI by default will not allow communication between two endpoints.**Contracts** are required between endpoint groups in order to enable communication between them. An EPG can be assigned to one BD at a time.

There are 3 types of Endpoints.

1. Physical
2. Virtual
3. External: These are devices which are not directly connected to ACI.

We can assign endpoint to EPG's using the following 4 methods.

1. Port-VLAN mapping
2. Source Mac Address
3. Source IP Address
4. VMM Intergration: Eg: VMware vCenter, Openstack etc.

***Micro Segmentation***

Concept to granularly controlling the communication between endpoints.

***Bridge-Domain***

It's similar to a vlan. A bridge domain can have only a single subnet assigned to it.

***Context***

It's same as VRF. Multiple bridge domains can be part of the same context.

***Tenant***

Tenant is just a management container.

We can have multiple contexts under a tenant.

ACI Supports multiple tenants. Communication cannot happen between 2 tenants.

There are 3 tenants that comes by default with every ACI deployment.

1. Common: These policies are accessible for every tenant in the ACI fabric.
2. Management: Inband and out of band management communication.
3. Infra: Internal communication between the fabric. eg: Spine and Leaf switch communication.

***Contracts***

Contracts are similar to Access Control List in the case of traditional networking. Contracts contains filters that contains ports and protocols just like access control list. No ip addresses will be used.

Contracts consists of multiple subjects and each subjects can have multiple filters. Contracts are applied in specific direction.

***Application Network Profile***

It defines EPG's as well as the Contracts.

***Anycast Gateway***

They will have same mac and ip addresses. In the case of ACI, it will be created on all the leaf switches, once host is connected to them.

VLAN Pools > Domain > AAEP > Interface Policy Groups > Interface Profiles > Switch Profiles

***VLAN Pools***

There are 2 types of VLAN pools.

1. Static: Used for legacy environments.
2. Dynamic: These are used for virtual environments.

***Domains***

Domains are used to connect endpoints to Endpoint Groups.

There 4 types of Domains

1. Physical
2. Virtual
3. External Bridged
4. External Routed

***Attachable Access Entity Profiles***

It helps to map Domains to Interface Policy Groups

***Interface Policies***

These are individual policies that we can apply to an interface.

***Interface Policy Groups***

There are 3 types

1. Access
2. Port-Channel
3. Virtual Port-Channel

***Interface Profiles***

We will use an interface selector which makes use of an interface range and the interface policy groups which we have created.

Interface overrides are used to override the interface policies that are applied to specific interfaces.

***Switch Profiles***

***VPC Protection Groups***

This helps to identify the pair of switches which are going to be vPC peer's.

- TEP pool which we are using needs to be unique and needs to be part of a separate VRF. 10.0.0.0/16 is the default pool which is used.

IS-IS is the routing protocol which we are using within ACI. This is due to the better scalability capabilities.

Fabric requires a VLAN ID which is 3967 by default.

VLAN ID for the fabric as well as the VTEP Pool range cannot be changed once the fabric is deployed.

***Local Station Table, Global Station Table and Spine Proxy***

**Note**: There are no unknown hosts in ACI fabric.

List of all directly attached hosts on a leaf is called as **Local Station Table**

Spine proxy knows which hosts are connected to specific leaf.
ie Host1 --> Leaf 1. Spine switches a COOP database.

Global Station Table is present on all leaf switches and contains information about remote hosts. It will have mac address when it's an L2 connections and will have ip addresses when it is a L3 connection.

***Bounce Entries***

 When a host moves from one leaf switch to another, in this case, this information is sent to the spine switch from the new leaf switch. Spine switch will update the COOP database and will send the same information to the old leaf switch. Old leaf switch will remove the existing endpoint entry and add this as a bounce entry pointing towards the new leaf switch.

***Connecting ACI to Outside Networks***

1. Connecting to external routed networks: Border leaf connects ACI fabric to the external world.
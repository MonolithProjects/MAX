### Requirements

#### apt / yum
- libvirt-dev / libvirt-devel
-      ?      / libcec-devel

#### pip
- libvirt-python
- cec

#### KVM settings
##### Libvirt deamon listen on TCP ports
  - uncomment LIBVIRTD_ARGS="--listen" in /etc/sysconfig/libvirtd

  - in /etc/libvirt/libvirtd.conf__
    listen_tls = 0 #for LAN usage__
    listen_tcp = 1__
    listen_addr = "<binded IP>"

#### listAllDomains flags
    all 0
    VIR_CONNECT_LIST_DOMAINS_ACTIVE
    VIR_CONNECT_LIST_DOMAINS_INACTIVE
    VIR_CONNECT_LIST_DOMAINS_PERSISTENT
    VIR_CONNECT_LIST_DOMAINS_TRANSIENT
    VIR_CONNECT_LIST_DOMAINS_RUNNING
    VIR_CONNECT_LIST_DOMAINS_PAUSED
    VIR_CONNECT_LIST_DOMAINS_SHUTOFF
    VIR_CONNECT_LIST_DOMAINS_OTHER
    VIR_CONNECT_LIST_DOMAINS_MANAGEDSAVE
    VIR_CONNECT_LIST_DOMAINS_NO_MANAGEDSAVE
    VIR_CONNECT_LIST_DOMAINS_AUTOSTART
    VIR_CONNECT_LIST_DOMAINS_NO_AUTOSTART
    VIR_CONNECT_LIST_DOMAINS_HAS_SNAPSHOT
    VIR_CONNECT_LIST_DOMAINS_NO_SNAPSHOT

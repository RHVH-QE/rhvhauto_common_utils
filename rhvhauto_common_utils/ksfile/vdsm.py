ksfiles = dict()

ksfiles["atv_local_vlan_01.ks"] = """
liveimg --url={squashfs}
ignoredisk --only-use=sda
clearpart --all
autopart --type=thinp
rootpw --plaintext redhat
timezone --utc Asia/Harbin
zerombr
text
reboot

%post --erroronfail
imgbase layout --init
%end
"""

ksfiles["atv_nfs_vlan50_01.ks"] = """
"""

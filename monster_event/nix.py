###############################################################################
# linux event id
iid_mstr_linux_base = 10000

iid_mstr_logon_sucess = 760
iid_mstr_logon_fail = 761
iid_mstr_logoff = 762
iid_mstr_account_add = 765

iid_mstr_process_created = 1510
iid_mstr_file_io = 2510
iid_mstr_file_delete = 2512
iid_mstr_file_rename = 2513
iid_mstr_net_connect = 3511
iid_mstr_net_accept = 3512

# linux event id
iid_mstr_linux_logon_success = iid_mstr_linux_base + iid_mstr_logon_sucess
iid_mstr_linux_logon_fail = iid_mstr_linux_base + iid_mstr_logon_fail
iid_mstr_linux_logoff = iid_mstr_linux_base + iid_mstr_logoff
iid_mstr_linux_account_add = iid_mstr_linux_base + iid_mstr_account_add
iid_mstr_linux_process_created = iid_mstr_linux_base + iid_mstr_process_created
iid_mstr_linux_file_io = iid_mstr_linux_base + iid_mstr_file_io
iid_mstr_linux_file_delete = iid_mstr_linux_base + iid_mstr_file_delete
iid_mstr_linux_file_rename = iid_mstr_linux_base + iid_mstr_file_rename
iid_mstr_linux_net_connect = iid_mstr_linux_base + iid_mstr_net_connect
iid_mstr_linux_net_accept = iid_mstr_linux_base + iid_mstr_net_accept



account_events = [
    iid_mstr_linux_logon_success,
    iid_mstr_linux_logon_fail,
    iid_mstr_linux_logoff,
]

file_events = [
    iid_mstr_linux_file_io,
    iid_mstr_linux_file_delete,
]

file_rename_events = [
    iid_mstr_linux_file_rename,
]

net_events = [
    iid_mstr_linux_net_accept,
    iid_mstr_linux_net_connect,
]

process_create_events = [
    iid_mstr_linux_process_created
]

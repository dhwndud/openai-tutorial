###############################################################################
# windows event id
iid_mstr_logon_event = 9500
iid_mstr_logon_fail_event = 9501
iid_mstr_logoff = 9502
iid_mstr_eventlog_clear = 9504
iid_mstr_remote_session_create = 9505
iid_mstr_remote_session_close = 9506

iid_mstr_service_install = 9509

iid_mstr_process_create = 1500
iid_mstr_process_stop = 1501
iid_mstr_process_open = 1504
iid_mstr_remote_thread = 1506

iid_mstr_file_renamed = 2113
iid_mstr_file_io = 2500
iid_mstr_file_removed = 2502

iid_mstr_tcp_connect = 3500
iid_mstr_tcp_accept = 3501
iid_mstr_udp_sendto = 3502
iid_mstr_udp_recvfrom = 3503

iid_mstr_reg_io = 4100
iid_mstr_reg_key_delete = 4101
iid_mstr_reg_key_rename = 4102
iid_mstr_reg_value_write = 4103
iid_mstr_reg_value_delete = 4104

#
# TODO
#   추가로 식별해서 작업해야하는 이벤트 ID
#
iid_mstr_new_kernel_driver_install = 9507
iid_mstr_process_new_execute_module_loaded = 1502

account_events = [
    iid_mstr_logon_event,
    iid_mstr_logon_fail_event,
    iid_mstr_logoff,
]
remote_session_events = [
    iid_mstr_remote_session_create,
    iid_mstr_remote_session_close,
]
file_events = [
    iid_mstr_file_io,
    iid_mstr_file_renamed,
    iid_mstr_file_removed,
]

net_events = [
    iid_mstr_tcp_connect,
    iid_mstr_tcp_accept,
    iid_mstr_udp_sendto,
    iid_mstr_udp_recvfrom,
]

reg_events = [
    iid_mstr_reg_io,
    iid_mstr_reg_key_delete,
    iid_mstr_reg_key_rename,
    iid_mstr_reg_value_write,
    iid_mstr_reg_value_delete
]
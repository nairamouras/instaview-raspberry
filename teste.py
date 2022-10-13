from ctypes import windll

if not windll.powrprof.SetSuspendState(False, False, False):
    print("No se ha podido suspender el sistema.")
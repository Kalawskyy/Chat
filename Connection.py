import telnetlib 

class client:
    with telnetlib.Telnet('localhost',23) as tn:
        tn.interact()



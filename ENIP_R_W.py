from cpppo.server.enip.get_attribute import proxy_simple
from cpppo.server.enip import client

# Class 2, Instance 2, Attribute 1
# Class 6B Instance 1 Attribute 1
host = proxy_simple('192.168.1.4')


try:
    res, = host.read( [('@0x04/1/1', 'DINT')])
    
    # Register_2, = host.read( '@6B/1/2', "INT" )
    # Registers_s, = host.read( '@6B/1' )
    # Register_3, = host.read( '@6B/1/3' )
    # Registers_p = host.read( '@6B/1' )
    # r , a = host.write('@6B/1/1', "DINT" )
except:
    print("Exception")
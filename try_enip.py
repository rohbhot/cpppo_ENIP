import os
from json import load
from cpppo.server.enip.get_attribute import proxy_simple

js_file = open(os.path.dirname(__file__)+'\\resources\\ab_cip.json')
ab_cip = load(js_file)
ab_cip = ab_cip["Vendor specific object"]

via = proxy_simple("192.168.0.101")

product_name,= via.read(  [ ("@0x1/1/7","SSTRING",None ) ] )
identity, = via.read( [ ( "@1/1", ["INT", "INT", "INT", "INT", "INT", "DINT", "SSTRING", "USINT"], "Identity" ) ])

tcp = ab_cip["tcpip"]["attribute"]


tcpip,		= via.read([ (tcp, ["DWORD", "DWORD", "DWORD", "EPATH","IPADDR", "IPADDR", "IPADDR", "IPADDR", "IPADDR", "STRING","STRING"]	, "TCPIP")])

#res, = via.read([ ( ab_cip["identity"]["attribute"] , ab_cip["identity"]["d_type"], "Identity" ) ])

print(product_name)
print(identity)
print(tcpip)

"""
        product_name	= parameter( "@1/1/7", "SSTRING", None ),
        identity	= parameter( "@1/1",	[
            "INT", "INT", "INT", "INT", "INT", "DINT", "SSTRING", "USINT"
        ], "Identity" ),
        tcpip		= parameter( "@0xF5/1",	[
            "DWORD", "DWORD", "DWORD", "EPATH",
            "IPADDR", "IPADDR", "IPADDR", "IPADDR", "IPADDR", "STRING",
            "STRING"
        ], "TCPIP" )
    )
"""

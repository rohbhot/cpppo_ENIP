from cpppo.server.enip.get_attribute import proxy_simple
import os
from json import load

js_file = open(os.path.dirname(__file__)+'\\resources\\ab_cip.json')

class ab_cip():
    def __init__(self,ip="localhost"):
        self.ip = ip
        self.class_id_dict = load(js_file)
        self.class_id_dict = self.class_id_dict["Vendor specific object"]
        self.via = self._connect()

    def _connect(self):
        try:
            via = proxy_simple(self.ip)
        except:
            print("Connection exception occured")
        return via

    def read(self,parameter="identity",tag=None,d_type=None,units=None):
        """
        
            The 'attributes' must be either a simple string Tag name (no Type, implying the use of 
            *Logix Read Tag [Fragmented] service), 
                eg: "Tag"

            OR

            an iterable containing 2 or 3 values; 
                a Tag/address, 
                a type/types (may be None, to force Tag I/O) 
                an optional description (eg. Units)
                        ( "Tag", None, "kWh" ),
                        ( "@1/1/1", "INT" ),
                        ( "@1/1/1", "INT", "Hz" ),
                        ( "@1/1", ( "INT", "INT", "INT", "INT", "INT", "DINT", "SSTRING", "USINT" ), "Identity" )
                Example reg, = self.via.read( [ ( inp,'REAL', 'Units') ] )

        """
        tag = self.class_id_dict[parameter]["attribute"]
        d_type = self.class_id_dict[parameter]["d_type"]
        units = self.class_id_dict[parameter]["units"]
        
        reg, = self.via.read([(tag,d_type,units)])

        return reg
    
    def write(self,parameter="identity",value = '5',attribute=None,d_type=None):
        """
            Supply "Tag = <value>" to perform a write i.e. attribute = attribute + ' = REAL()'+value
            res, = self.via.read([(inp+' = (REAL)'+value, '@0x6C/1/19')]) # Reference
        """
        attribute = self.class_id_dict[parameter]["attribute"]
        d_type = self.class_id_dict[parameter]["type"]
        value = value

        res, = self.via.read ( [ ( attribute+'='+d_type + value, '@0x6C/1/19')]) # Reference

        return res

cl = ab_cip("192.168.0.101")

x = cl.read("product name")

print(x)


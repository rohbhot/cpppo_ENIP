from cpppo.server.enip.get_attribute import proxy_simple
from json import load
import os

js_file = open(os.path.dirname(__file__)+'\\resources\\delta_class.json')

class delta_cip():
    def __init__(self,ip="localhost"):
        self.ip = ip
        self.class_id_dict = load(js_file)
        self.class_id_dict = self.class_id_dict["Vendor specific object"]
        #self.via = proxy_simple(host=self.ip)

    def read(self,class_id = "@0x6C",instance='1',attribute ='20',d_type="REAL"):
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
        """

        inp = self.class_id_dict[class_id]+'/'+instance+'/'+attribute
        print(int(self.class_id_dict[class_id],16))
        #reg, = self.via.read( [(inp,'REAL')] ) # Reference
        reg, = self.via.read( [(inp,d_type)] )

        return inp, reg
        
    
    def write(self,class_id = "@0x6C",instance='1',attribute ='20', value = '5'):
        inp = self.class_id_dict[class_id]+'/'+instance+'/'+attribute
        
        #attribute = attribute + ' = REAL()'+value
        inp = inp+' = (REAL)'+value

        #res, = self.via.read([(inp+' = (REAL)'+value, '@0x6C/1/19')]) # Reference
        res, = self.via.read([(inp, '@0x6C/1/19')]) # Uncomment this, this is according to the params

        return inp, res
        

cl = delta_cip("localhost")
inp_r,reg_r = cl.read("D Register")
print(inp_r, reg_r)

inp_r, reg_r = cl.read("Custom_Tag_Name")
print(inp_r, reg_r)

ack,  = cl.write("D Register")
print(ack)
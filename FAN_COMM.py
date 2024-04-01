from cpppo.server.enip.get_attribute import proxy_simple
HOST = '192.168.128.52'

via = proxy_simple(host=HOST)

# READ WRITE FOR REAL   
def read(attribute ='20'):
    inp='@0x6C/1/'+attribute
    reg, = via.read( [(inp,'REAL')] )
    return reg
     
def write(attribute='20', value = '5'):
    inp='@0x6C/1/'+attribute
    #attribute = attribute + ' = REAL()'+value
    res, = via.read([(inp+' = (REAL)'+value, '@0x6C/1/19')])
    return res
    
#THIS WILL RETURN THE POSITION IN THE JOG FRAME CURRENTLY SET ON ROBOT PENDANT     
def read_curr_pos():
    res, = via.read( [('@0x7D/1/1', 'REAL')])
    return res

def read_pos_reg(attribute='13'):
    # POS_REGISTERS
    inp = '@0x7B/1/'+attribute
    res, = via.read([(inp, 'REAL')])
    return res

def write_pos_reg(attribute='13', value='0,8,2,3,4,5,6,7,8,9,10'):
    # POS_REGISTERS
    inp = '@0x7B/1/'+attribute
    res, = via.read([(inp+' = (REAL)'+value, '@0x7B/1/13')])


if __name__ == "__main__":
    #write_pos()
    print(read_pos_reg('60'))

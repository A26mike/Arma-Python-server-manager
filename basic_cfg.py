class BasicCFG:
    """BasicCFG [summary]

        Args:
            uploadSpeed ([int]): [In MB/s]
            socket_init ([int]): [description]
            socket_min ([int]): [description]
            maxPacketSize (int, optional): [ISP MTU settings ]. Defaults to 1400.
    """

    def __init__(self, uploadSpeed, socket_init, socket_min, maxPacketSize = 1400):

        self.uploadSpeed = uploadSpeed
        self.socket_int = socket_init
        self.socket_min = socket_min
        self.maxPacketSize = maxPacketSize


    def mbits_to_bits (self, uploadSpeed):
        bits = 10000000 * uploadSpeed
        return bits
        
    def mbits_to_bytes(self,uploadSpeed):
        bytes = 125000 * uploadSpeed
        return  bytes
                                        

    def mbits_to_kbits(self, upload): 
        kbits= 000 * uploadSpeed                #TODO fix the conversion and math 
        return kbits

    def print_arma_arma_cfg(self):
        """print_arma_arma_cfg [Writes the Server basic.cfg]
        """        
        cfg_perams=[]                           #TODO change to dictinary  and fix logic 
        server_socket_max = self.mbits_to_bytes(self.uploadSpeed)
        print(server_socket_max)
        server_socket_init = self.mbits_to_bytes(self.socket_int)
        server_socket_min = self.mbits_to_bytes(self.socket_min)
        global_min_bandwith = self.mbits_to_bits(self.uploadSpeed)
        cfg_perams = [ server_socket_init,server_socket_min, server_socket_max, global_min_bandwith]
        print(cfg_perams)
        arma_cfg = f"""
//basic.cfg
class sockets
{{

    initBandwidth = {cfg_perams[0]}; // {cfg_perams[0]}
    MinBandwidth =  {cfg_perams[1]}; //(64 kbit) 
    MaxBandwidth =  {cfg_perams[2]}; //(16 Mbit) 250x minBandwith  
}};


MinBandwidth = {cfg_perams[3]};
// MaxBandwidth = 104857600;   // Broken do not use

MaxMsgSend = 2048;	        	// Maximum number of messages that can be sent in one simulation cycle. Increasing this value can decrease lag on high upload bandwidth servers. Default: 128
MaxSizeGuaranteed = 512;		// Maximum size of guaranteed packet in bytes (without headers). Small messages are packed to larger frames. Guaranteed messages are used for non-repetitive events like shooting. Default: 512
MaxSizeNonguaranteed = 256;		// Maximum size of non-guaranteed packet in bytes (without headers). Non-guaranteed messages are used for repetitive updates like soldier or vehicle position. Increasing this value may improve bandwidth requirement, but it may increase lag. Default: 256

MinErrorToSend = 0.003;			// Minimal error to send updates across network. Using a smaller value can make units observed by binoculars or sniper rifle to move smoother. Default: 0.001
MinErrorToSendNear = 0.02;		// Minimal error to send updates across network for near units. Using larger value can reduce traffic sent for near units. Used to control client to server traffic as well. Default: 0.01

MaxCustomFileSize = 0;			// (bytes) Users with custom face or custom sound larger than this size are kicked when trying to connect.


"""
        f = open("basic.cfg", "w")
        f.write(arma_cfg)
        f.close()






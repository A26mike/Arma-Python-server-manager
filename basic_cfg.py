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
        # self.mbits_to_bytes = mbits_to_bytes
        # self.mbits_to_bits=  mbits_to_bits

    def mbits_to_bits (self, uploadSpeed):
        bits = 10000000 * uploadSpeed
        return bits

    def mbits_to_bytes(self,uploadSpeed):
        bytes = 125000 * uploadSpeed
        return  bytes

    def print_arma_arma_cfg(self):
        """print_arma_arma_cfg [Writes the Server basic.cfg]
        """        
        cfg_dict = {
            "maxPacketSize_Sockets": self.maxPacketSize,
            "initBandwidth_Sockets": self.mbits_to_bytes(self.socket_int),
            "MinBandwidth_Sockets": self.mbits_to_bytes(self.socket_min),
            "MaxBandwidth_Sockets": self.mbits_to_bytes(self.uploadSpeed),
            "MinBandwidth_global": self.mbits_to_bits(self.uploadSpeed),
            "MaxBandwidth_global": self.mbits_to_bytes(self.uploadSpeed)
        }

        arma_cfg = f"""
class sockets
{{
    maxPacketSize = {cfg_dict.get("maxPacketSize_Sockets")}
    initBandwidth = {cfg_dict.get("initBandwidth")}; // {int(cfg_dict.get("initBandwidth")) / 125000 }
    MinBandwidth =  {cfg_dict.get("MinBandwidth_Sockets")}; //(64 kbit) 
    MaxBandwidth =  {cfg_dict.get("MaxBandwidth_Sockets")}; //(16 Mbit) 250x minBandwith  
}};


MinBandwidth = {cfg_dict.get("MinBandwidth_global")};
// MaxBandwidth = {cfg_dict.get("MaxBandwidth_global")};   // Broken do not use

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






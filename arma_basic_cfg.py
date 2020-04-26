
socket_max = int(input("What is the server's Max Upload speed in megabit/s: \n "))
socket_init = int(input("Server initial bandwidth recommended 10-25mbit\n"))
socket_min = int(input("What is the slowest clients download speed in megabit/s:\n "))

def mbits_to_bits (mbits):
    return 10000000 * mbits
    pass

def mbits_to_bytes(mbits):
    return 125000 * mbits

server_socket_max = mbits_to_bytes(socket_max)
server_socket_init = mbits_to_bytes(socket_init)
server_socket_min = mbits_to_bytes(socket_min)
global_min_bandwith =mbits_to_bits(socket_max)

arma_cfg = f"""
//basic.cfg
class sockets
{{

    initBandwidth = {server_socket_init}; // (256 kbit) 4x minbandwith in socket class .
    MinBandwidth = {server_socket_min}; //(64 kbit) 
    MaxBandwidth ={server_socket_max}; //(16 Mbit) 250x minBandwith  
}};


MinBandwidth = {global_min_bandwith};
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
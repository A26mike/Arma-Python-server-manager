from classes.basic_cfg import BasicCFG

server_1 =BasicCFG( 200,5,1
    # (input("What is the server's Max Upload speed in megabit/s: \n ")),
    # (input("Server initial bandwidth recommended 10-25mbit\n")),
    # (input("What is the slowest clients download speed in megabit/s:\n "))
)
server_1.print_arma_cfg()
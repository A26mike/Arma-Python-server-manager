import basic_cfg
test= basic_cfg.BasicCfg
test(
    int(input("What is the server's Max Upload speed in megabit/s: \n ")),
    int(input("Server initial bandwidth recommended 10-25mbit\n")),
    int(input("What is the slowest clients download speed in megabit/s:\n "))
)

test.Print_arma_arma_cfg(test)
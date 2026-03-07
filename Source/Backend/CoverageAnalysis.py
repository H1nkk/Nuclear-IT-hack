from riscv_reg_block import reg_access

import random

all_addr = list(range(0x0000, 0x0010))
print(f"Amount = {len(all_addr)}")

ITERS = 0
input_values = [0, 1, 0xF, 0xFF, 0xFFF, 0xFFFF, 0x10000 - 1]

def mega_test(test_addr : list) -> dict:
    # random.shuffle(test_addr)
    for addr in test_addr:

        if (addr == 0x0003):
            continue
        
        print(f"- Testing address {addr}")
        print(f"Predefined values")

        for test_input in range(0x0000, 0xFFFF):
            writing = reg_access(addr, test_input, 'write')
            if not writing['ack']: 
                print(f"Addr {addr}, test value {test_input} - Error ack = false when writing")
                continue
        
            reading = reg_access(addr, 0, 'read')
            if not reading['ack']: 
                print(f"Addr {addr}, test value {test_input} - Error ack = false when reading")
                continue

            if (test_input != reading['reg_value']): 
                print(f"Addr {addr}, test value {test_input} - Error reading data != writing data. Read value: {reading['reg_value']}")
                continue
        print(f"Random values")
        for iter in range(ITERS):
            test_input = random.randint(0, 0xFFFF)
            writing = reg_access(addr, test_input, 'write')
            if not writing['ack']: 
                print(f"Addr {addr}, test value {test_input} - Error ack = false when writing")
                continue
        
            reading = reg_access(addr, 0, 'read')
            if not reading['ack']: 
                print(f"Addr {addr}, test value {test_input} - Error ack = false when reading")
                continue

            if (test_input != reading['reg_value']): 
                print(f"Addr {addr}, test value {test_input} - Error reading data != writing data")
                continue

mega_test(all_addr)  

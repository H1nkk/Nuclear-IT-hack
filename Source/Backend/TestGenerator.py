from riscv_reg_block import riscv_reg_access

import random

all_addr = list(range(0x0000, 0x10000))
print(f"Amount = {len(all_addr)}")

results = {}

# 0 - OK
# 1 - ack = false (reading)
# 2 - ack = false (writing)
# 3 - test_input != reading
# 4 - exception

def test_all_registers(test_addr : list):
    random.shuffle(test_addr)

    passed = 0
    failed = 0

    for addr in test_addr:
        test_input = 0xA5A5A5A5
        try:
            writing = riscv_reg_access(addr, test_input, 'write')
            if not writing['ack']: # Err 1: ack = false in write
                results[addr] = 1
                failed += 1
                continue
            
            reading = riscv_reg_access(addr, 0, 'read')
            if not reading['ack']: # Err 2: ack = false in read
                results[addr] = 2
                failed += 1
                continue
        
            if (test_input != reading['reg_value']): # Err 3: Write != Read
                results[addr] = 3
                failed += 1
            else:
                results[addr] += 0
                passed += 1
        except Exception as e: # Err 4: Just died
            results[addr] = 4
            failed += 1

    # Stats  
    print(f"Checked: {len(test_addr)}")      
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
 
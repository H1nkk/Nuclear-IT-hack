from Source.Backend.riscv_reg_block import reg_access
import random

import pytest

# Write Read All Value 

def test_write_read_all_values_register_0(): 
    for test_input in range(0x0000, 0xFFFF): 
        writing = reg_access(0, test_input, 'write') 
        if not writing['ack']: 
            assert False 

        reading = reg_access(0, 0, 'read') 
        if not reading['ack']:  
            assert False 

        if (test_input != reading['reg_value']): 
            assert False 
    assert True


def test_write_read_all_values_register_1(): 
    for test_input in range(0x0000, 0xFFFF): 
        writing = reg_access(1, test_input, 'write') 
        if not writing['ack']: 
            assert False 

        reading = reg_access(1, 0, 'read') 
        if not reading['ack']:  
            assert False 

        if (test_input != reading['reg_value']): 
            assert False 
    assert True


def test_write_read_all_values_register_2(): 
    for test_input in range(0x0000, 0xFFFF): 
        writing = reg_access(2, test_input, 'write') 
        if not writing['ack']: 
            assert False 

        reading = reg_access(2, 0, 'read') 
        if not reading['ack']:  
            assert False 

        if (test_input != reading['reg_value']): 
            assert False 
    assert True


def test_write_read_all_values_register_3(): 
    for test_input in range(0x0000, 0xFFFF): 
        writing = reg_access(3, test_input, 'write') 
        if not writing['ack']: 
            assert False 

        reading = reg_access(3, 0, 'read') 
        if not reading['ack']:  
            assert False 

        if (test_input != reading['reg_value']): 
            assert False 
    assert True


def test_write_read_all_values_register_4(): 
    for test_input in range(0x0000, 0xFFFF): 
        writing = reg_access(4, test_input, 'write') 
        if not writing['ack']: 
            assert False 

        reading = reg_access(4, 0, 'read') 
        if not reading['ack']:  
            assert False 

        if (test_input != reading['reg_value']): 
            assert False 
    assert True


def test_write_read_all_values_register_5(): 
    for test_input in range(0x0000, 0xFFFF): 
        writing = reg_access(5, test_input, 'write') 
        if not writing['ack']: 
            assert False 

        reading = reg_access(5, 0, 'read') 
        if not reading['ack']:  
            assert False 

        if (test_input != reading['reg_value']): 
            assert False 
    assert True


def test_write_read_all_values_register_6(): 
    for test_input in range(0x0000, 0xFFFF): 
        writing = reg_access(6, test_input, 'write') 
        if not writing['ack']: 
            assert False 

        reading = reg_access(6, 0, 'read') 
        if not reading['ack']:  
            assert False 

        if (test_input != reading['reg_value']): 
            assert False 
    assert True


def test_write_read_all_values_register_7(): 
    for test_input in range(0x0000, 0xFFFF): 
        writing = reg_access(7, test_input, 'write') 
        if not writing['ack']: 
            assert False 

        reading = reg_access(7, 0, 'read') 
        if not reading['ack']:  
            assert False 

        if (test_input != reading['reg_value']): 
            assert False 
    assert True


def test_write_read_all_values_register_8(): 
    for test_input in range(0x0000, 0xFFFF): 
        writing = reg_access(8, test_input, 'write') 
        if not writing['ack']: 
            assert False 

        reading = reg_access(8, 0, 'read') 
        if not reading['ack']:  
            assert False 

        if (test_input != reading['reg_value']): 
            assert False 
    assert True


def test_write_read_all_values_register_9(): 
    for test_input in range(0x0000, 0xFFFF): 
        writing = reg_access(9, test_input, 'write') 
        if not writing['ack']: 
            assert False 

        reading = reg_access(9, 0, 'read') 
        if not reading['ack']:  
            assert False 

        if (test_input != reading['reg_value']): 
            assert False 
    assert True


def test_write_read_all_values_register_10(): 
    for test_input in range(0x0000, 0xFFFF): 
        writing = reg_access(10, test_input, 'write') 
        if not writing['ack']: 
            assert False 

        reading = reg_access(10, 0, 'read') 
        if not reading['ack']:  
            assert False 

        if (test_input != reading['reg_value']): 
            assert False 
    assert True


def test_write_read_all_values_register_11(): 
    for test_input in range(0x0000, 0xFFFF): 
        writing = reg_access(11, test_input, 'write') 
        if not writing['ack']: 
            assert False 

        reading = reg_access(11, 0, 'read') 
        if not reading['ack']:  
            assert False 

        if (test_input != reading['reg_value']): 
            assert False 
    assert True


def test_write_read_all_values_register_12(): 
    for test_input in range(0x0000, 0xFFFF): 
        writing = reg_access(12, test_input, 'write') 
        if not writing['ack']: 
            assert False 

        reading = reg_access(12, 0, 'read') 
        if not reading['ack']:  
            assert False 

        if (test_input != reading['reg_value']): 
            assert False 
    assert True


def test_write_read_all_values_register_13(): 
    for test_input in range(0x0000, 0xFFFF): 
        writing = reg_access(13, test_input, 'write') 
        if not writing['ack']: 
            assert False 

        reading = reg_access(13, 0, 'read') 
        if not reading['ack']:  
            assert False 

        if (test_input != reading['reg_value']): 
            assert False 
    assert True


def test_write_read_all_values_register_14(): 
    for test_input in range(0x0000, 0xFFFF): 
        writing = reg_access(14, test_input, 'write') 
        if not writing['ack']: 
            assert False 

        reading = reg_access(14, 0, 'read') 
        if not reading['ack']:  
            assert False 

        if (test_input != reading['reg_value']): 
            assert False 
    assert True


def test_write_read_all_values_register_15(): 
    for test_input in range(0x0000, 0xFFFF): 
        writing = reg_access(15, test_input, 'write') 
        if not writing['ack']: 
            assert False 

        reading = reg_access(15, 0, 'read') 
        if not reading['ack']:  
            assert False 

        if (test_input != reading['reg_value']): 
            assert False 
    assert True


# Overflow Test 

def test_overflow_register_0(): 
    test_input = 0xFFFFFF 
    expected_output = 0xFFFF 
    writing = reg_access(0, test_input, 'write') 
    if not writing['ack']: 
        assert False 

    reading = reg_access(0, 0, 'read') 
    if not reading['ack']: 
        assert False 

    if (expected_output != reading['reg_value']): 
        assert False 
    assert True 


def test_overflow_register_1(): 
    test_input = 0xFFFFFF 
    expected_output = 0xFFFF 
    writing = reg_access(1, test_input, 'write') 
    if not writing['ack']: 
        assert False 

    reading = reg_access(1, 0, 'read') 
    if not reading['ack']: 
        assert False 

    if (expected_output != reading['reg_value']): 
        assert False 
    assert True 


def test_overflow_register_2(): 
    test_input = 0xFFFFFF 
    expected_output = 0xFFFF 
    writing = reg_access(2, test_input, 'write') 
    if not writing['ack']: 
        assert False 

    reading = reg_access(2, 0, 'read') 
    if not reading['ack']: 
        assert False 

    if (expected_output != reading['reg_value']): 
        assert False 
    assert True 


def test_overflow_register_3(): 
    test_input = 0xFFFFFF 
    expected_output = 0xFFFF 
    writing = reg_access(3, test_input, 'write') 
    if not writing['ack']: 
        assert False 

    reading = reg_access(3, 0, 'read') 
    if not reading['ack']: 
        assert False 

    if (expected_output != reading['reg_value']): 
        assert False 
    assert True 


def test_overflow_register_4(): 
    test_input = 0xFFFFFF 
    expected_output = 0xFFFF 
    writing = reg_access(4, test_input, 'write') 
    if not writing['ack']: 
        assert False 

    reading = reg_access(4, 0, 'read') 
    if not reading['ack']: 
        assert False 

    if (expected_output != reading['reg_value']): 
        assert False 
    assert True 


def test_overflow_register_5(): 
    test_input = 0xFFFFFF 
    expected_output = 0xFFFF 
    writing = reg_access(5, test_input, 'write') 
    if not writing['ack']: 
        assert False 

    reading = reg_access(5, 0, 'read') 
    if not reading['ack']: 
        assert False 

    if (expected_output != reading['reg_value']): 
        assert False 
    assert True 


def test_overflow_register_6(): 
    test_input = 0xFFFFFF 
    expected_output = 0xFFFF 
    writing = reg_access(6, test_input, 'write') 
    if not writing['ack']: 
        assert False 

    reading = reg_access(6, 0, 'read') 
    if not reading['ack']: 
        assert False 

    if (expected_output != reading['reg_value']): 
        assert False 
    assert True 


def test_overflow_register_7(): 
    test_input = 0xFFFFFF 
    expected_output = 0xFFFF 
    writing = reg_access(7, test_input, 'write') 
    if not writing['ack']: 
        assert False 

    reading = reg_access(7, 0, 'read') 
    if not reading['ack']: 
        assert False 

    if (expected_output != reading['reg_value']): 
        assert False 
    assert True 


def test_overflow_register_8(): 
    test_input = 0xFFFFFF 
    expected_output = 0xFFFF 
    writing = reg_access(8, test_input, 'write') 
    if not writing['ack']: 
        assert False 

    reading = reg_access(8, 0, 'read') 
    if not reading['ack']: 
        assert False 

    if (expected_output != reading['reg_value']): 
        assert False 
    assert True 


def test_overflow_register_9(): 
    test_input = 0xFFFFFF 
    expected_output = 0xFFFF 
    writing = reg_access(9, test_input, 'write') 
    if not writing['ack']: 
        assert False 

    reading = reg_access(9, 0, 'read') 
    if not reading['ack']: 
        assert False 

    if (expected_output != reading['reg_value']): 
        assert False 
    assert True 


def test_overflow_register_10(): 
    test_input = 0xFFFFFF 
    expected_output = 0xFFFF 
    writing = reg_access(10, test_input, 'write') 
    if not writing['ack']: 
        assert False 

    reading = reg_access(10, 0, 'read') 
    if not reading['ack']: 
        assert False 

    if (expected_output != reading['reg_value']): 
        assert False 
    assert True 


def test_overflow_register_11(): 
    test_input = 0xFFFFFF 
    expected_output = 0xFFFF 
    writing = reg_access(11, test_input, 'write') 
    if not writing['ack']: 
        assert False 

    reading = reg_access(11, 0, 'read') 
    if not reading['ack']: 
        assert False 

    if (expected_output != reading['reg_value']): 
        assert False 
    assert True 


def test_overflow_register_12(): 
    test_input = 0xFFFFFF 
    expected_output = 0xFFFF 
    writing = reg_access(12, test_input, 'write') 
    if not writing['ack']: 
        assert False 

    reading = reg_access(12, 0, 'read') 
    if not reading['ack']: 
        assert False 

    if (expected_output != reading['reg_value']): 
        assert False 
    assert True 


def test_overflow_register_13(): 
    test_input = 0xFFFFFF 
    expected_output = 0xFFFF 
    writing = reg_access(13, test_input, 'write') 
    if not writing['ack']: 
        assert False 

    reading = reg_access(13, 0, 'read') 
    if not reading['ack']: 
        assert False 

    if (expected_output != reading['reg_value']): 
        assert False 
    assert True 


def test_overflow_register_14(): 
    test_input = 0xFFFFFF 
    expected_output = 0xFFFF 
    writing = reg_access(14, test_input, 'write') 
    if not writing['ack']: 
        assert False 

    reading = reg_access(14, 0, 'read') 
    if not reading['ack']: 
        assert False 

    if (expected_output != reading['reg_value']): 
        assert False 
    assert True 


def test_overflow_register_15(): 
    test_input = 0xFFFFFF 
    expected_output = 0xFFFF 
    writing = reg_access(15, test_input, 'write') 
    if not writing['ack']: 
        assert False 

    reading = reg_access(15, 0, 'read') 
    if not reading['ack']: 
        assert False 

    if (expected_output != reading['reg_value']): 
        assert False 
    assert True 



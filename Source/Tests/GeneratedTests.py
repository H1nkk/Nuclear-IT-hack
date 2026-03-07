from Source.Backend.riscv_reg_block import reg_access
import random


import pytest


def test_register_0():
    for test_input in range(0x0000, 0xFFFF):
        writing = reg_access(0, test_input, "write")
        if not writing["ack"]:
            assert False

        reading = reg_access(0, 0, "read")
        if not reading["ack"]:
            assert False

        if test_input != reading["reg_value"]:
            assert False

    assert True


def test_register_1():
    for test_input in range(0x0000, 0xFFFF):
        writing = reg_access(1, test_input, "write")
        if not writing["ack"]:
            assert False

        reading = reg_access(1, 0, "read")
        if not reading["ack"]:
            assert False

        if test_input != reading["reg_value"]:
            assert False

    assert True


def test_register_2():
    for test_input in range(0x0000, 0xFFFF):
        writing = reg_access(2, test_input, "write")
        if not writing["ack"]:
            assert False

        reading = reg_access(2, 0, "read")
        if not reading["ack"]:
            assert False

        if test_input != reading["reg_value"]:
            assert False

    assert True


def test_register_3():
    for test_input in range(0x0000, 0xFFFF):
        writing = reg_access(3, test_input, "write")
        if not writing["ack"]:
            assert False

        reading = reg_access(3, 0, "read")
        if not reading["ack"]:
            assert False

        if test_input != reading["reg_value"]:
            assert False

    assert True


def test_register_4():
    for test_input in range(0x0000, 0xFFFF):
        writing = reg_access(4, test_input, "write")
        if not writing["ack"]:
            assert False

        reading = reg_access(4, 0, "read")
        if not reading["ack"]:
            assert False

        if test_input != reading["reg_value"]:
            assert False

    assert True


def test_register_5():
    for test_input in range(0x0000, 0xFFFF):
        writing = reg_access(5, test_input, "write")
        if not writing["ack"]:
            assert False

        reading = reg_access(5, 0, "read")
        if not reading["ack"]:
            assert False

        if test_input != reading["reg_value"]:
            assert False

    assert True


def test_register_6():
    for test_input in range(0x0000, 0xFFFF):
        writing = reg_access(6, test_input, "write")
        if not writing["ack"]:
            assert False

        reading = reg_access(6, 0, "read")
        if not reading["ack"]:
            assert False

        if test_input != reading["reg_value"]:
            assert False

    assert True


def test_register_7():
    for test_input in range(0x0000, 0xFFFF):
        writing = reg_access(7, test_input, "write")
        if not writing["ack"]:
            assert False

        reading = reg_access(7, 0, "read")
        if not reading["ack"]:
            assert False

        if test_input != reading["reg_value"]:
            assert False

    assert True


def test_register_8():
    for test_input in range(0x0000, 0xFFFF):
        writing = reg_access(8, test_input, "write")
        if not writing["ack"]:
            assert False

        reading = reg_access(8, 0, "read")
        if not reading["ack"]:
            assert False

        if test_input != reading["reg_value"]:
            assert False

    assert True


def test_register_9():
    for test_input in range(0x0000, 0xFFFF):
        writing = reg_access(9, test_input, "write")
        if not writing["ack"]:
            assert False

        reading = reg_access(9, 0, "read")
        if not reading["ack"]:
            assert False

        if test_input != reading["reg_value"]:
            assert False

    assert True


def test_register_10():
    for test_input in range(0x0000, 0xFFFF):
        writing = reg_access(10, test_input, "write")
        if not writing["ack"]:
            assert False

        reading = reg_access(10, 0, "read")
        if not reading["ack"]:
            assert False

        if test_input != reading["reg_value"]:
            assert False

    assert True


def test_register_11():
    for test_input in range(0x0000, 0xFFFF):
        writing = reg_access(11, test_input, "write")
        if not writing["ack"]:
            assert False

        reading = reg_access(11, 0, "read")
        if not reading["ack"]:
            assert False

        if test_input != reading["reg_value"]:
            assert False

    assert True


def test_register_12():
    for test_input in range(0x0000, 0xFFFF):
        writing = reg_access(12, test_input, "write")
        if not writing["ack"]:
            assert False

        reading = reg_access(12, 0, "read")
        if not reading["ack"]:
            assert False

        if test_input != reading["reg_value"]:
            assert False

    assert True


def test_register_13():
    for test_input in range(0x0000, 0xFFFF):
        writing = reg_access(13, test_input, "write")
        if not writing["ack"]:
            assert False

        reading = reg_access(13, 0, "read")
        if not reading["ack"]:
            assert False

        if test_input != reading["reg_value"]:
            assert False

    assert True


def test_register_14():
    for test_input in range(0x0000, 0xFFFF):
        writing = reg_access(14, test_input, "write")
        if not writing["ack"]:
            assert False

        reading = reg_access(14, 0, "read")
        if not reading["ack"]:
            assert False

        if test_input != reading["reg_value"]:
            assert False

    assert True


def test_register_15():
    for test_input in range(0x0000, 0xFFFF):
        writing = reg_access(15, test_input, "write")
        if not writing["ack"]:
            assert False

        reading = reg_access(15, 0, "read")
        if not reading["ack"]:
            assert False

        if test_input != reading["reg_value"]:
            assert False

    assert True

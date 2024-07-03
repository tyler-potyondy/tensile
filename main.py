from pynrfjprog import LowLevel 
from board import Board

if __name__ == '__main__':
    # Scan for available devices.
    nrfjprog_api = LowLevel.API()
    nrfjprog_api.open()

    available_devices = nrfjprog_api.enum_emu_snr()

    # Create board objects for each device.
    board = Board(available_devices[0], 
                  "tock/boards/nordic/nrf52840dk", 
                  "libtock-c/examples/tests/ieee802154/radio_tx", 
                  "radio_tx", 
                  "tock/target/thumbv7em-none-eabi/release/nrf52840dk.bin")

    board.prep_test()
    print(board.run_test(5))

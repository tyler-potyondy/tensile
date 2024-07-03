from board import Board
def radio_rxtx_test(boards):
    # We require 2 boards for this test.
    # TODO: Better handling/reporting of case w/o at least 2 boards.
    if len(boards) < 2:
        raise Exception("Error: [Inadequate resources] - radio_rxtx test requires at least two available boards.")
    
    # Create board objects for each device.
    board = Board(boards[0], 
                  "tock/boards/nordic/nrf52840dk", 
                  "libtock-c/examples/tests/ieee802154/radio_tx", 
                  "radio_tx", 
                  "tock/target/thumbv7em-none-eabi/release/nrf52840dk.bin")

    # Setup board for test.
    board.prep_test()

    # Run test for 10 seconds and gather results.
    test_results = board.run_test(10)
from pynrfjprog import LowLevel 
from board import Board

if __name__ == '__main__':
    # Scan for available devices.
    nrfjprog_api = LowLevel.API()
    nrfjprog_api.open()

    available_devices = nrfjprog_api.enum_emu_snr()


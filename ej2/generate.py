from nmigen import *
from nmigen.cli import main
from random import getrandbits
from inlineAdapter import inlineAdapter
import sys

#For using this script to generate verilog: 
#############   python3 generate.py generate -t v verilogGenerated.v   ###################
#python3 generate.py (generate or simulate) -t (type --> v for verilog or il for RTLIL) (filename)
class RegisterFile(Elaboratable):
    def __init__(self):
        self.adr   = Signal(4)
        self.dat_r = Signal(8)
        self.dat_w = Signal(8)
        self.we    = Signal()
        self.mem   = Memory(width=8, depth=16, init=[getrandbits(8) for i in range(16)])
        self.memo  = Memory(width=24, depth=24, init=[getrandbits(24) for i in range(24)])

    def elaborate(self, platform):
        m = Module()
        m.submodules.rdport = rdport = self.mem.read_port()
        m.submodules.wrport = wrport = self.mem.write_port()

        m.submodules.rdport2 = rdport2 = self.memo.read_port()
        m.submodules.wrport2 = wrport2 = self.memo.write_port()
        m.d.comb += [
            rdport.addr.eq(self.adr),
            self.dat_r.eq(rdport.data),
            wrport.addr.eq(self.adr),
            wrport.data.eq(self.dat_w),
            wrport.en.eq(self.we),
        ]
        return m


if __name__ == "__main__":
    rf = RegisterFile()
    main(rf, ports=[rf.adr, rf.dat_r, rf.dat_w, rf.we])
    inputFile = sys.argv[-1]
    ia = inlineAdapter(inputPath = inputFile) #Overwrites the inputFile
    ia.modifyFile()

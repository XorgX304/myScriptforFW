import chipsec.chipset
import chipsec.hal.mmio
import chipsec.hal.physmem
from struct import unpack, pack

cs = chipsec.chipset.cs()
cs.init(None, True, True)
getMMIO = chipsec.hal.mmio.MMIO(cs)
getMEM = chipsec.hal.physmem.Memory(cs)

getMMIO.list_MMIO_BARs()


PR0 = 0x84
PR1 = 0x88
PR2 = 0x8c
PR3 = 0x90
PR4 = 0x94



SPIBAR = (getMMIO.read_mmcfg_reg(0x0, 0x1F, 5, 0x10, 8))
Val_PR0 = unpack("<L" ,getMEM.read_physical_mem(SPIBAR+PR0, 0x4))[0]
Val_PR1 = unpack("<L" ,getMEM.read_physical_mem(SPIBAR+PR1, 0x4))[0]
Val_PR2 = unpack("<L" ,getMEM.read_physical_mem(SPIBAR+PR2, 0x4))[0]
Val_PR3 = unpack("<L" ,getMEM.read_physical_mem(SPIBAR+PR3, 0x4))[0]

GetBC = getMMIO.read_mmcfg_reg(0x0, 0x1F, 5, 0xdc, 8)
Val_BC = str.format('0x{:08X}', GetBC)

a1 = SPIBAR+0x8
v9 = 4
a2_val = (a1 + 16 * v9 + 0x68)
v5_val = (a1 + 16 * (v9 + 9) - 32)

a2 = unpack("<L" ,getMEM.read_physical_mem(a2_val, 0x4))[0]
v5 = unpack("<L" ,getMEM.read_physical_mem(v5_val, 0x4))[0]
result = (a2 >> 12) & 0x1FFF | 16 * (a2 + v5 - 1) & 0x1FFF0000 | 0x80000000;
print hex(unpack("<L" ,getMEM.read_physical_mem(v5_val, 0x4))[0])
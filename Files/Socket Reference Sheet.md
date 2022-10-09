<!--This document follows GitHub's .md file formatting, which might render slightly differently on other editors -->

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Socket Overview](#socket-overview)
    - [Intel CPU/Socket list](#intel-cpu-list)
        - [Overclocking information](#overclocking-information)
        - [Motherboard support](#motherboard-support)
    - [AMD CPU/Socket list](#amd-socket)
        - [overclocking information](#overclocking-information-1)

# Socket Overview
Intel and AMD always releases new CPU sockets every few generations, so it's hard to keep track which generation of CPUs goes with which socket. Thankfully, this guide is here to tell you what everything means.

## Intel CPU/Socket list
Intel tends to change sockets every 

### Overclocking information
Officially, overclocking is possible when only `K` CPUs are being used with `Z` motherboards. However, on some select 12th gen motherboards, it is possible to do *Bus Clock overclocking* (occationally called *BCLK overclocking*) on `non-K` CPUs, which is very risky and requires extensive knowledge.

### Motherboard Support
Socket 1151 V1:

    Motherboard: Z170, Z270, and other 100 and 200 series boards
    CPU support: 6th gen and 7th gen Core, such as i7 6700K and 7700K 
    Memory: Both DDR3 and 4, depending on Motherboard
    PCIe: 3
    Note: incompatible with 8th and 9th gen CPU.

Socket 1151 V2:

    Motherboard: Z370 and other 300 series boards.
    CPU support: 8700K, 9900K, and other 8th and 9th gen CPU
    Memory: DDR4, (DDR3 motherboards extremely rare)
    PCIe: 3
    Note: incompatible with 6th and 7th gen CPU. When 9th gen released, there is another motherboard, Z390, that was released. This works with any 8th and 9th gen CPU out-of-the-box.

Socket 1200:

    Motherboard: Z490, Z590, other 400 and 500 series boards.
    CPU support: 10th and 11th gen Intel CPUs.
    Memory: DDR4
    PCIe: 3 for Z490, some Z490 supports 4 and all Z590 supports 4. PCIe 4 requires 11th gen CPU.
    
Socket 1700:

    Motherboard: Z690, Z790, and other 600 and 700 series motherboards.
    CPU support: 12th gen, 13th gen
    Memory: DDR4 and 5
    PCIe: PCIe 5 on the GPU PEG slot, NVMe depends on motherboard
    Note: Z690 using PCIe5 storage will decrease bus width to graphics card.


## AMD CPU/socket list

### Overclocking information
All Ryzen CPUs paired with any motherboard except `A series` is overclockable. However, officially the Ryzen 7 5800X3D and all Athlon CPUs is locked, but unofficially they can be overclocked.

AM4 summary and rundown:

    300 series motherboard: Ryzen 1000 and 2000 support, PCIe 3

    400 series motherboard: Ryzen 1000 to 3000 support, 5000 varies on BIOS revision, PCIe 3 for all CPUs.

    B550 motherboard: official Ryzen 3000 and 5000 support, unofficial support for earlier CPUs. PCIe 4 but chipset is PCIe 3, only Ryzen 3000 and above can utilize PCIe 4.

    X570 motherboard: Ryzen 2000, 3000 and 5000 support, unofficially supports earlier CPUs. Also have full PCIe 4 but requires Ryzen 3000 and above. 


AM5 summary and rundown:
    
    B650 and B650E: desktop Ryzen 7000 support, 16 lanes PCIe 4 to GPU, 8 lanes PCIe 5 to SSD and peripherals.
    
    X670: desktop Ryzen 7000 support, better version of B650E. X series motherboards all have two chipsets for better connectivity.
    
    X670E: flagship chipset, have full PCIe 5 support on GPU PEG slot and NVMe SSD.

# Building the PC

Now that we've got the socket and the most confusing part out of the way, let's throw everything together and hope it boots.

## Component Checklist
Placeholder

1. - [ ] #1
2. - [x] is this working
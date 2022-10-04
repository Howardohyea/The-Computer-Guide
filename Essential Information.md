<!--This document follows GitHub's .md file formatting, which might render slightly differently on other editors -->

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Socket Overview](#socket-overview)
    - [Intel CPU/Socket list](#intel-cpu-list)
        - [Integrated Graphics](#integrated-graphics)
        - [Overclocking information](#overclocking-information)
        - [Motherboard support](#motherboard-support)
    - [AMD CPU/Socket list](#amd-socket)
        - [Integrated Graphics](#integrated-graphics-1)
            - [AM4](#am4)
            - [AM5](#am5)
        - [overclocking information](#overclocking-information-1)
        - [AM4 support](#am4-support) 
        - [AM5 support](#am5-support)
- [Building the PC](#building-the-pc)
    - [Compoment Checklist](#component-checklist)

# Socket Overview
Intel and AMD always releases new CPU sockets every few generations, so it's hard to keep track which generation of CPUs goes with which socket. Thankfully, this guide is here to tell you what everything means.

## Intel CPU/Socket list
Intel tends to change sockets every two generations of CPUs, and might be confusing to some. 

### Integrated Graphics
All Intel CPUs comes with integrated GPUs, except CPUs marked with `F`, such as the `i7 12700KF`. The `F` variants tends to be ~20 USD cheaper than the non-F counterparts. **However**, I strongly recommend spending some extra money for the iGPU, as they are excellent video encoders and is very useful when it comes to troubleshooting.

Intel's integrated graphics are all quite weak though, don't expect them to be able to do anything except handle a display output and regular office tasks. 

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
Unlike Intel, AMD tends to support each motherboard socket for as long as possible, often 5 years. This means theoretically you could use the same motherboard on quite a few generations of CPUs, although you have to check the BIOS compatibility, see the below sections for some information.

## Integrated graphics
#### AM4
Only CPUs with the `G` suffix have an iGPU, such as the `Ryzen 7 5700G`. All `non-G` CPUs doesn't have any integrated graphics.

#### AM5
For AM5, all CPUs have integrated graphics, **there is no CPUs without iGPU as of time of this writing**. Despite this, `G Series` CPUs are still being released, featuring a much more powerful graphics than the ones without the G suffix.

### Overclocking information
All Ryzen CPUs paired with any motherboard except `A series` is overclockable. However, officially the Ryzen 7 5800X3D and all Athlon CPUs is locked, but unofficially they can be overclocked.

### AM4 support
AM4 only supports DDR4

    300 series motherboard: Ryzen 1000 and 2000 support, PCIe 3

    400 series motherboard: Ryzen 1000 to 3000 support, 5000 varies on BIOS revision, PCIe 3 for all CPUs.

    B550 motherboard: official Ryzen 3000 and 5000 support, unofficial support for earlier CPUs. PCIe 4 but chipset is PCIe 3, only Ryzen 3000 and above can utilize PCIe 4.

    X570 motherboard: Ryzen 2000, 3000 and 5000 support, unofficially supports earlier CPUs. Also have full PCIe 4 but requires Ryzen 3000 and above. 


### AM5 support
AM5 only supports DDR5
    
    B650 and B650E: desktop Ryzen 7000 support, 16 lanes PCIe 4 to GPU, 8 lanes PCIe 5 to SSD and peripherals.
    
    X670: desktop Ryzen 7000 support, better version of B650E. X series motherboards all have two chipsets for better connectivity.
    
    X670E: flagship chipset, have full PCIe 5 support on GPU PEG slot and NVMe SSD.

# Building the PC

Now that we've got the socket and the most confusing part out of the way, let's throw everything together and hope it boots.

## Component Checklist
you'll need the following core components to build a PC:

1. a CPU
2. compatible motherboard, check [Socket Overview](#socket-overview) for a list of compatible CPU and motherboards
3. discrete GPU, or video card. If you're not planning to use a standalone card, ensure your CPU have integrated graphics by checking the section above.
4. DDR4 or DDR5 memory, depending on the CPU and/or motherboard.
5. CPU cooler (some CPUs bundles a stock cooler with it, double check with the seller)
6. Case fans
7. PC case
8. PSU, or Power Supply Unit. All power cables are bundled with the PSU, and it's _strongly recommended_ to use only the cables that came with the PSU, do not mix and match.
9. SSD, be it SATA or NVMe
10. Screws, which often is bundled with the PC case.

Extra components you need, if you don't already have them.
1. monitor
2. keyboard & mouse
3. USB with a copy of the OS of your choice
4. Speakers or headphones

## Installation Process
The order of the list given is only a suggestion. You could switch some around, but do note you might run into trouble installing some components if you did it in the wrong order. For example, installing the GPU before a M.2 SSD can be troublesome as the M.2 slot is usually underneath the GPU.

Here's the steps:

1. Install CPU to motherboard socket, note orientation of CPU in order to prevent damage, then press down on the latch to secure the CPU. 
2. If you have an M.2 SSD, install it in the motherboard now, or else you might run into issues with clearance later on.
2. Attach the motherboard to the case, note the orientation of the motherboard, and screw in the scrwes. As a suggestion, don't overtighten them, as you might damage the motherboard traces otherwise. 
3. Install RAM in corresponding sockets, generally you'd want an even number of sticks of RAM. If you have two sticks, put them in the 2nd and 4th slot on the motherboard. Note: RAM often require a ridiculous amount of force to install, don't be afraid if the motherboard flexes slightly, make sure both ends of the RAM is in place.
4. Locate the PSU bay, often the lower rear of the case, and secure the PSU inside and plug all necessary cables in the PSU.
    
    * list of cables you'd need:
        * 24 pin cable to the motherboard
        * 4/8/12 pin for the CPU, depending on the motherboard. The cables are all bundled together in multiples of four and marked `CPU`.
        * Several cables marked `PCIe`, these are for the GPU, and depending on the card installed it could be 6, 8, 14, 16, or more pins. Always group one 6+2 cable into one bundle, and **never** daisy chain one 6+2 cable into two connectors on the GPU.
5. Route all PSU cables behind motherboard (or in front, if you don't want to cable manage your build), and plug all the cables into the corresponding place on the motherboard. 
6. Put a tiny amount of thermal paste on CPU, an X or dot will be sufficient. 
7. Install CPU cooler by using locking mechanism on motherboard. Please ensure compatibility of cooler with CPU socket, and remove peel before proceeding with installation. 
8. Plug all relevant fan connectors into the corresponding motherboard fan headers.
10. Install graphics card, secure screws, and put relevant power connectors in place, including main 🡪 PSU connector.
11. Attempt to power on PC, with the display cable in GPU instead of motherboard (if applicable).
12. Connect the front header to the motherboard (located on the lower right corner)
13. Mash F12, F2, or delete to get into BIOS. The exact keyboard input might vary from motherboard to motherboard, but these three is the most commonly used. 


<!--This document follows GitHub's .md file formatting, which might render slightly differently on other editors -->

# Table of Contents
- [Why PC](#why-pc)
- [Table of Contents](#table-of-contents)
- [Socket Overview](#socket-overview)
    - [Intel CPU/Socket list](#intel-cpu-list)
        - [The various suffix](#the-various-suffix)
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
    - [Installation Process](#installation-process)
- [Miscellaneous Notes](#miscellaneous-notes)
    - [The RAM Rabbit Hole](#the-ram-rabbit-hole)
    - [Operating Systems](#operating-systems)
    - [Drivers and where to get them](#drivers-and-where-to-download)
    - [Tips](#tips)
- [Glossary](#glossary)

# Why PC?
<!--![the author's motherboard and CPU](Assets/Strix%20A%20with%20i7.jpg)-->

PC gaming is definitely the better choice compared to consoles, being much cheaper, flexible, powerful, modular. Plus, aside from gaming, you could use your PC to do work. At this day and age, everyone needs some sort of electronic device, so if you're buying a desktop, might as well as spend  bit more for some more powerful components. If you're just picking up or planning to build your own rig, all the different components with varying support may be pretty overwhelming and might tempt you to buy a prebuilt PC or a console. 

If you're overwhelmed, I'll do this best in this short document to make things as easy as possible for you to choose and build your own PC.


# Socket Overview
Intel and AMD always releases new CPU sockets every few generations, so it's hard to keep track which generation of CPUs goes with which socket. Thankfully, this guide is here to tell you what everything means.

## Intel CPU/Socket list
Intel tends to change sockets every two generations of CPUs, and might be confusing to some. 

You will see a lot of `LGA xxxx` for Intel CPUs, and "LGA" stands for "Land Grid Array", meaning the pins are on the motherboard. The xxxx denotes a number, which is the number of pins on the motherboard socket.

### The various suffix
Intel is known to have a lot of different suffix to various processors, here's their meaning. 

K: overclockable and fully unlocked, every setting about the CPU frequency and voltage can be tweaked.

F: see [Integrated Graphics](#integrated-graphics).

S: Special chips featuring higher core clocks than the non-S counterparts. Only CPUs released with the S suffix is the `i9 12900KS` and the `i9 9900KS`.

X: HEDT[^1] chips, featuring much more core counts, PCIe lanes, and other features compared to the desktop counterparts. There is also the `XE` suffix, indicating it's the flagship. Intel haven't released any HEDT since the `i9 10980XE` in late 2019.

T: Optimized for low power, with a max power of typically 65 watts for use in special cases. There is also a very rare `B` suffix, which have a power limit slightly higher than the T processors.

H: Laptop CPUs, with a high power/performance. Processor Base Power is usually 65 watts and higher. 

P: Laptop CPUs, with a medium power and medium performance. Typical Processor Base Power is 35 watts. 

U/G: Laptop CPUs with low power and performance. G means it have a better integrated graphics than the U.

Y: very low power laptop, down to 8 watts, low core count typically too.


### Integrated Graphics
All Intel CPUs comes with integrated GPUs, except CPUs marked with `F`, such as the `i7 12700KF`. The `F` variants tends to be ~20 USD cheaper than the non-F counterparts. **However**, I strongly recommend spending some extra money for the iGPU, as they are excellent video encoders and is very useful when it comes to troubleshooting.

Intel's integrated graphics are all quite weak in anything 3D though, don't expect them to be able to do anything except very basic gaming, video playback, and regular office tasks.

### Overclocking information
Officially, overclocking is possible when only `K` CPUs are being used with `Z` motherboards. However, on some select 12th gen motherboards, it is possible to do *Bus Clock overclocking* (abbreviated to *BCLK overclocking*) on `non-K` CPUs, which is very risky and requires extensive knowledge.[^2]

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
    PCIe: PCIe 5 on the GPU PEG slot, NVMe depends on motherboard.
    Note: Z690 only supports 13th gen with a BIOS update while 700 series doesn't.

**Upcoming** Socket 1851 is Intel's socket for 14th gen CPUs. The following is an educated guess and may not turn out to be correct:

    Motherboard: Z890 and other 800 series motherboards.
    CPU support: 14th (possibly 15th)
    Memory: DDR5 (most likely no 4)
    PCIe: 5 on GPU, possibly 5 on CPU by default
    Note: only the compute die is built at Intel, rest is built using TSMC


## AMD CPU/socket list
Unlike Intel, AMD tends to support each motherboard socket for a fairly long time, and promises to support AM5 until 2025. This means theoretically you could use the same motherboard on quite a few generations of CPUs, although you have to check the BIOS compatibility, see the below sections for some information.

### Integrated graphics
#### AM4
Only CPUs with the `G` suffix have an iGPU, such as the `Ryzen 7 5700G`. All `non-G` CPUs doesn't have any integrated graphics.

#### AM5
For AM5, all CPUs have integrated graphics, **there is no CPUs without iGPU as of time of this writing**. Despite this, `G Series` CPUs will still be released, featuring a much more powerful graphics than the ones without the G suffix. Ryzen 7000's iGPU is comparable to Intel's 12th gen CPU's, which is still significantly slower than a GT 1030. 


### Overclocking information
All Ryzen CPUs paired with any motherboard except `A series` is officially overclockable. However, officially the Ryzen 7 5800X3D and all Athlon CPUs is locked, but unofficially they can be overclocked.

### AM4 support
AM4 only supports DDR4, and consists of 1331 pins on the CPU (so it's also called PGA1331).

    300 series motherboard: Ryzen 1000 and 2000 support, PCIe 3

    400 series motherboard: Ryzen 1000 to 3000 support, 5000 varies on BIOS revision, PCIe 3 for all CPUs.

    B550 motherboard: official Ryzen 3000 and 5000 support, unofficial support for earlier CPUs. PCIe 4 but chipset is PCIe 3, only Ryzen 3000 and above can utilize PCIe 4.

    X570 motherboard: Ryzen 2000, 3000 and 5000 support, unofficially supports earlier CPUs. Also have full PCIe 4 but requires Ryzen 3000 and above. 


### AM5 support
AM5 only supports DDR5. It consists of 1713 pins on the motherboard, so it's also called LGA 1713, albiet rarely.
    
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

I also recommend using [PC Part Picker](https://pcpartpicker.com) to pick your components, they even include information such as case clearance and other compatibility information.

## Installation Process
The order of the list given is only a suggestion. You could switch some around, but do note you might run into trouble installing some components if you did it in the wrong order. For example, installing the GPU before a M.2 SSD can be troublesome as the M.2 slot is usually underneath the GPU.

Here's the steps:

1. Install CPU to motherboard socket, note orientation of CPU in order to prevent damage, then press down on the latch to secure the CPU. 
2. If you have an M.2 SSD, install it in the motherboard now, or else you might run into issues with clearance later on.
2. Attach the motherboard to the case, note the orientation of the motherboard, and screw in the scrwes. As a suggestion, don't overtighten them, as you might damage the traces on the motherboard. 
3. Install RAM in corresponding sockets, for more RAM information, please see [RAM Compatibility](#ram-compatibility). Note: RAM often require a ridiculous amount of force to install, don't be afraid if the motherboard flexes slightly, make sure both ends of the RAM is in place.
4. Locate the PSU bay, often the lower rear of the case, and secure the PSU inside and plug all necessary cables in the PSU.
    * list of cables you'd need:
        * 24 pin cable to the motherboard
        * 4/8/12 pin for the CPU, depending on the motherboard. The cables are all bundled together in multiples of four and marked `CPU`.
        * Several cables marked `PCIe`, these are for the GPU, and depending on the card installed it could be 6, 8, 14, 16, or more pins. Always group one 6+2 cable into one bundle, and **never** daisy chain one 6+2 cable into two connectors on the GPU.
5. Route all PSU cables behind motherboard (or in front, if you don't want to cable manage your build), and plug all the cables into the corresponding place on the motherboard. 
3141. Connect the case front panel headers onto the bottom right of the motherboard. The exact order and location depends on the motherboard, so you'll have to check the motherboard manual to be sure.
6. Put a tiny amount of thermal paste on CPU, an X or dot will be sufficient. 
7. Install CPU cooler by using locking mechanism on motherboard. Please ensure compatibility of cooler with CPU socket, and remove peel before proceeding with installation. 
8. Plug all relevant fan connectors into the corresponding motherboard fan headers.
10. Install graphics card, secure screws, and put relevant power connectors in place, including main 🡪 PSU connector.
11. Attempt to power on PC, with the display cable in GPU instead of motherboard (if applicable).
12. Connect the front header to the motherboard (located on the lower right corner)
13. Mash F12, F2, or delete to get into BIOS. The exact keyboard input might vary from motherboard to motherboard, but these three is the most commonly used. 

So, that's the essentials to installing a PC, if your PC isn't booting, please check out [Troubleshooting](Troubleshooting%20Steps).

# Miscellaneous Notes
Here's some other non-essential information that doesn't really belong anywhere else, such as tips, driver downloads, and information that doesn't fit elsewhere in this document.

## The RAM Rabbit Hole
Arguably, RAM is one of the most confusing part of a PC, with wild variances even with minor differences in hardware. For a much more detailed information than the one I have here, check out this very well-written article: [DDR DRAM FAQ](https://www.tomshardware.com/reviews/ddr-dram-faq,4154.html).

Here's some general tips you should follow:

* Buy all your RAM in one kit, which for example might be 2 sticks with 8GB each. Each kit is specifically tested by the manufacturer to have standard timings and each RAM would only work optimally with another from the same kit.
* Two sticks of RAM is most likely going to outperform 4 sticks if capacity is the same. This is usually caused by additional load on the IMC (Integrated Memory Controller) by running two sticks per channel.
    * All modern consumer grade CPUs have two memory channels, so I suggest buying 2 sticks (unless 4 sticks is cheaper at the same speed)
* There's more to memories than just advertised speed. It's like describing a car based on the engine RPM alone. I suggest checking out reviews before purchasing. 
* If you have two RAM sticks and four motherboard RAM slots, put them in the 2nd and 4th slot of the motherboard for maximum compatibility.

That's just some general buying guide, and here's some technical information:

* If both memory channels have different memory capacities, the CPU would run in what's called `Flex Mode`. This mode will run in dual channel mode (meaning faster bandwidth) as long as the memory utilization is less than twice the capacity of the smallest channel. If the capacity spills over, the system will revert to single channel, trading memory speed to use all of the available memory.
    * For example, if one channel is 8GB in size and the other is 16, the PC will run in dual channel mode as long as the memory utilization is below 16GB. If it goes over, the memory speed will halve but the PC will have access to the full 24GB of memory.
* Another obscure piece of information not a lot of people know about is `Memory Rank`. All consumer RAM is either Single or Dual Rank, often abbreviated to 1R or 2R[^3]. Typically 2R memory is ideal for a CPU.

### Setting XMP
XMP, occasionally called DOCP, EXPO, or some other names, is a one-click overclock that changes the speed a stick of RAM runs at from the default JEDEC (often 2133 or 2666MT/s for DDR4) to the advertised speed written on the RAM stick. 

To enable XMP, simply go in the motherboard BIOS, and look for the setting, usually found under `Overclocking`.

## Operating Systems
I've covered the hardware part in this document previously, but you're going to need some Operating System to interface with the harware. Of course, if you want to write your own OS, feel free to do so, and remember to send me the source code. 

Jokes aside, here's some download links to common OSes (and a few recommended by me).

* [Windows 10](https://www.microsoft.com/en-us/software-download/windows10), a popular OS with by far the largest market share, it is lighter than 11 and still have the classic UI everyone's familiar with. Despite the release of Windows 11, 10 will still be supported to at least 2025, and the LTSC branch for another 5 years. 
* [Windows 11](https://www.microsoft.com/en-us/software-download/windows11), Microsoft's latest OS. Despite numerous bugs and issues during launch, it started gaining traction in recent months.
* [Arch Linux](https://archlinux.org), a true "DIY" OS where nothing comes preinstalled, and the user have to do literally everything, IKEA style. As a result, it is the most customizable Linux distro and is notorious for it's difficult installation process.
    * [Endeavour OS](https://endeavouros.com), based on Arch Linux, but with a graphical installer and comes preinstalled with several essential applications. Probably the closest you'll ever get to native Arch without the installation hassle.
    <!--fun fact, the author of this document uses Endeavour-->
* [Debian](https://debian.org), the backbone of Ubuntu and numerous other distros, when combined, all Debian based distros holds the largest market share of any Linux OS.[^4]
    * [Linux Mint](https://linuxmint.com), based on the Ubuntu-LTS branch, which in turn is based on Debian. It offers full software compatibility with both Debian and Ubuntu, as well as some Desktop Environments designed to look similar to Windows.
* [ReactOS](https://reactos.org), an Open Sourced OS with the goal of having **full support** for all Windows applications and drivers natively without emulation, this means it can run `.exe` files without compromise.

## Drivers and Where to Download
I can't stress this enough, ***never download drivers from Driver Support Utilities***. They're just bloatware eating your system resources, and who knows if they're some virus in disguise?

Anyways the most commomly used drivers are the GPU drivers, and here's a link to them.

* [AMD](https://www.amd.com/en/support)
* [Nvidia](https://www.nvidia.com/Download/index.aspx?lang=en-us) (choose `Game Ready Drivers`, which contains optimizations for games the `Studio` drivers do not have).
* [Intel](https://www.intel.com/content/www/us/en/download-center/home.html), but remember, Arc is Intel's discrete GPU, not their integrated.

If you're looking for motherboard drivers, you'll have to search the motherboard manufacturer's website. There's too many of them, so I won't list them all here.

## Tips
Here's a few tips that I suggest you to follow.

1. monitor various properties of your hardware using [HWiNFO](https://hwinfo.com), includes voltage, temps, power, and pretty much all information you need.
2. Benchmarks:
    - [Cinebench R23](https://apps.microsoft.com/store/detail/9PGZKJC81Q7J?hl=en-us&gl=US), a CPU benchmark that is virtually an industrial standard. Includes Single and Multithread benchmarks.
    - [3DMark](https://3dmark.com), a synthetic benchmark for both CPU and GPU, not very good for comparison between hardware but useful to test overclocking. The full test is paid but the free demo can be found [here](steam://install/231350) (requires Steam to be installed on your PC).
    - [LamePi](/Assets/LamePi.py), which is a parody of SuperPi. LamePi is a self made Python script that calculates Pi to a precision of 15 decimal place. This is strictly single threaded Floating Point benchmark and requires a python intepreter to run.[^5]
3. Please don't use `Userbenchmark` to test your hardware, they are so biased it's a meme at this point. If you want to hear more details about why they suck, submit an issue and I'll comment the details, I don't want to turn this document into a rant against UBM.
4. Some review sites I recommend:
    - [TechPowerUp](https://techpowerup.com)
    - [Tom's Hardware](https://tomshardware.com) (they're not as good as their hayday in terms of article quality since 2019, but if you need to research old hardware, all their articles before 2019 is *fantastic*)
    - [Linus Tech Tips](https://www.youtube.com/c/LinusTechTips). I wouldn't take whatever Linus says for granted, but he is entertaining to watch.
5. I actually suggest turning off or not enabling `BitLocker` or any drive encryption. This *will* make your PC vulnerable if it's stolen as anyone with the right knowledge can look at your files, but what are the odds of that? Also, turning it off can make salvaging your files when something goes catastrophically wrong much easier. 
5. [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701) is a very good and customizable replacement to the ancient CMD interface with hardware accelerated text.
6. Feeling low? Nothing [a few jokes can't fix](https://github.com/shrutikapoor08/devjoke)!

# Glossary
**BCLK**: Bus Clock, the clock that dictates the speed every component in your PC runs at. By default, this value is 100 MHz, although some computers might run it slightly lower, at 99.8 for technical reasons. This can be tweaked, but a lot of components doesn't like it being ran at something other than 100, causing potential instabilities.

**Multiplier**: The speed in which the CPU runs at when multiplied by the BCLK. For example, if the multiplier is x50 and BCLK is 100, then the CPU is running at 5.0GHz. Altering this number is the easiest way to overclock a system. 

**DDR**: Memory speed is all measured in `MT/s`, where MT is MegaTransfers. A lot of people might use `MHz`, which is technically incorrect but often used interchangeably with `MT`. So, the "DDR" means Double Data Rate, so for every Hz there is two data transfers happening. This effectively means a DDR4-3200 RAM is actually running at 1600MHz, but with the Double Data Rate the speed is effectively doubled.

**GPU**: Graphics Processing Unit, another part of your PC that's just as important as the CPU yet is talked about much more rarely than the CPU. It plugs in the motherboard PCIe slot and calculates everything that is displayed on-screen.

**CPU**: Central Processing Unit, the part of the computer that's often referred to the "brain". It calculates all background tasks not directly involved with what's being displayed.

**RTFM**: On forums, users might use this term, which means "Read The Fu*king Manual". They're not delibrately being unhelpful, but usually they're just annoyed at you for asking such a simple question that is very well documented, typically in the product's User Manual.


[^1]: Stands for High End DeskTop
[^2]: Bus Clock also dictates other system components like RAM and PCIe, in a way it can be viewed as our clock. Changing its speed will cause some incompatibilities.
[^3]: Interestingly, there could be more than 2R on server memory, but we're not going to talk about them. 
[^4]: If you're going the Linux route, I recommend KDE as your Desktop Environment.
[^5]: LamePi asks users for the desired calculation accuracy. For reference, an `i7 11370H` took about 300 seconds to calculate to a precision of one billion. Do note, the processing time scales linearly with accuracy, so the execution time with an accuracy of 10 million will be 10 times longer than one million. Decimal places past 15 is subject to Floating Point inaccuracy, which is culled.
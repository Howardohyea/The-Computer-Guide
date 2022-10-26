# Table of Contents
- [Table of Contents](#table-of-contents)
- [Disclaimer](#disclaimer)

# Disclaimer
**This is not intended as a guide for the general public, view this as entertainment unless you can actually benefit from this.**

**I hold ZERO responsibility for any hardware you break following this guide, but I try my best to keep this as harmless to your system as possible.**

# Prerequisites 
Before you do anything to your system, BACK UP YOUR FILES! It's not that your PC will break, but rather a corrupted and unstable OS will make extracting those files much harder. 

Also, read [Essential Information](https://github.com/Howardohyea/Computer-QRH/blob/main/Essential%20Information.md) before you do anything.

## Softwares
You'll need some softwares to monitor your system, and these are:

1. [HWInfo](https://www.hwinfo.com/), a program that can monitor just about anything you can dream of on your system. You'll need it for temperature, clocks, and power. [^1]
2. [ThrottleStop](https://www.techpowerup.com/download/techpowerup-throttlestop/), which controls the CPU power and boosting behaviour.
3. Alternatively, for CPUs with unlocked multipliers[^2]:
    - [Intel XTU](https://www.intel.com/content/www/us/en/download/17881/intel-extreme-tuning-utility-intel-xtu.html) is Intel's software for overclocking their CPUs, can also used for undervolting.
    - [AMD Ryzen Master](https://www.amd.com/en/technologies/ryzen-master) is AMD's alternative to XTU.
4. [MSI Afterburner](https://msi.com/Landing/afterburner), a very good overclocking software for all sorts of GPUs.
    - [EVGA Precison X1](https://store.steampowered.com/app/268850/EVGA_Precision_X1/) is another alternative that can be found on Steam. It only supports Nvidia cards within a few years old though.
    - [AMD Radeon Software](https://www.amd.com/en/technologies/software) can be used to overclock AMD GPUs too.
5. Cinebench, for benchmarking the CPU. Download can be found in Essential Information.
6. 3DMark, for GPU benchmark, find the download in Essential Informations too.


That's all the software you'll need for casual tweaking.

## Getting a baseline
You'd want to run some benchmarks on your PC previously, such as 3DMark and Cinebench. You can find the download link in the other Essential Information document.

# Undervolting
Enough prerequisites, time to do the actual undervolting.

## The CPU
Typically you want to use ThrottleStop to underclock the CPU, which is as easy as setting a few settings. Follow the instructions down here, I'm going to use ThrottleStop for the steps below. Honestly, there's so much settings you could tweak, and the *vast majority* is for legacy processors made before 2016. I'll assume you have something recent, and write only the relevant information down.[^3]

1. 


[^1]: Do note that this is all software reported, which might be a few watts/millivolts off the actual hardware reading, not like it matters much for our sceneario.
[^2]: all Intel CPUs with a `K` at the end is unlocked (including notebook processors), and all desktop AMD CPUs except the `R7 5800X3D` and all `Athlon` series CPUs is locked.
[^3]: 
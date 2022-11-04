# Table of Contents
- [Table of Contents](#table-of-contents)
- [What's the issue?](#whats-the-issue)
	- [Your first build isn't booting](#your-first-build-isnt-booting)
	- [Advanced troubleshooting](#advanced-troubleshooting)
- [System Maintenance](#system-maintenance)
	- [viruses](#viruses)
	- [Hardware Maintenance](#hardware-maintenance)


# What's the issue?
If you're reading this, I assume there is absolutely no reactions out of the PC when you're pressing the power button. There might be fans spinning but nothing coming out of the display. If that's the case, continue reading!

## Your first build isn't booting
I assume you just came from [Essential Information](Essential%20Information.md), looking for a way to troubleshoot why your build isn't booting. 

1. Check the cables. Odds are you forgot one of those, or even forgot to turn the PSU on. Here's a list of the cables you need.
    - 24 pin cable to the motherboard, on the right of the RAM slots.
	- 4/8/12 pin for the CPU, depending on the motherboard. The cables are all bundled together in multiples of four and marked CPU. This is on the top left of the motherboard.
	- Several cables marked PCIe, these are for the GPU, and depending on the card installed it could be 6, 8, 14, 16, or more pins. Always group one 6+2 cable into one bundle, and **never** daisy chain one 6+2 cable into two connectors on the GPU.
2. Where did you plug the display cable? If you have a discrete GPU, put the display cable in there, unless you're planning to use the integrated GPU.
3. Is the case front panel wired up? one of the cables might be in the wrong place, double check with the motherboard manual to see if that's the case.
4. A common place for builds to not boot is incorrectly is the RAM stick isn't in correctly. They require some ridiculous force to stick in and even then one side might not be inserted correctly.
5. It's hightly recommended to stick the GPU in the topmost PCIe slot. You might loose performance but it shouldn't cause too much issues, unless on the off chance you have other devices occupying so much PCIe lanes there's not enough bandwidth for the GPU
6. If the PC is booting into the UEFI but not the OS, make sure of the following:
	- The M.2 SSD is in place and plugged in correctly.
	- SATA drives require their own power and data cables, one leading to the motherboard and the other to the PSU. Are they both in correctly?
7. For modern motherboards, not having any fans plugged in to either `AIO_PUMP` or `CPU_FAN` can prevent your PC from booting. It will show an error screen at boot to let you know.
8. I wrote this in [Essential Information](Essential%20Information), but in case you missed it, **do NOT** use cables from multiple PSUs, instead only use the ones provided by the PSU you bought. 
9. To rule out possible issues related to the RAM, try each individual RAM stick in all the slots. Throw everything at a wall and see what sticks.

That's it for a non-booting build, if it still doesn't boot, odds are you got a bad component somewhere or you didn't follow those instructions very well. Go over them a few times, who knows if third time's the charm?

## Advanced Troubleshooting
Maybe your PC was working and it suddenly decided to just give up, it have stability issues, or you just need some instructions as to how to fix something. I'm splitting this section into smaller topics, refer to the Table of Contents for more details.

### Instabilities
Sometimes a given system might be instable due to several reasons, such as a bad component, power reasons, or unstable overclock. Here's a list to troubleshoot the possible components. 

As a rule of thumb, CPUs are *extremely* hard to break, so I'm not going to consider any scenearios where they are the issue.

- First off, if you have **any overclock** like CPU core, RAM, and GPU, reset it back to stock unless you know what you're doing. 
- RAM and the CPU's IMC[^1] might be a bad pair, especially with older CPUs, like Ryzen 1000 and 2000, as well as Intel Skylake (does not include 7th gen Kaby) running DDR4 3200 and above.
	- To see if the memory is stable or not, download [OCCT](https://ocbase.com) and run the test using the dedicated memory test (both the SSE and AVX test would do).[^2]
		- AIDA64 and Memtest64 might miss some errors, and **definitely** don't use the built in Windows RAM troubleshooter.
	- If the test returns unstable, return the RAM back to stock by resetting the CMOS. You'll loose speed, but it should be stable at least.
- GPU OC and stablility can be tested using 3DMark, detailed in the other [Essential Information](Essential%20Information#tips) document.
	- Alternatively [Furmark](https://www.techpowerup.com/download/furmark/) is good for GPU stress testing because it causes the GPU to draw the absolute max power it could. 
- There isn't an effective way to test a motherboard, you can only look for signs that it's unstable.
	- Swapping GPUs can eliminate issues with the PCIe bus, and testing each individual RAM stick in different slots can rule out a memory issue.
- Having high wattage components paired with a lower end PSU can cause the PSU to trigger it's protection and shut itself down. If your PC is just starting to do any heavy workloads when the shutdown happens this is probably what's happening.
	- In this case, there's not much you could do without swapping PSUs, you could try limit your PC's total power consumed but there's only so much you could do on the software side.[^3]

# System maintenance
Windows have a very good system to upgrading the system, and pretty much everything is automated. Run their updater every now and then and you're good to go.

Also, it's suggested to keep your GPU driver as recent as possible, but you don't really need to do anything about motherboard BIOS. typically you're perfectly fine leaving it as-is because there won't be any new features added and those updates most likely just includes support for some obscure CPU.

## Viruses
First off, use common sense. Secondly, *don't* go and install every antivirus programs you can find if you think your PC is infected. 

What is common sense? 
1. Don't install suspicious packages from suspicious sites, and *only* download games from Steam.
2. Leave your firewall up at all times, and keep only the bare minimum amount of ports open.
3. So called "Game Hacks" are most likely viruses, also, you shouldn't be using any hacks in the first place. 
4. and here's an excellent quote on what is common sense:
> Common Sense is sound logic with practical and good reasoning. It is searching for simple but very useful ways of making decisions to solve problems. We are all born with the ability to think, create, and solve problems.
Common sense lives by the rule of thinking before you act. It helps us to see what can become of something like George Washington Carver did, who saw how practical resources could benefit many people in the world.
Common sense is not solely about using our minds to think of cool or witty inventions that will make us lots of money. It is about making wise decisions that affect our lives. When we lack common sense, we make decisions based on emotions rather than logic.

Okay, jokes aside, what should you do on the off chance you didn't follow common sense?

1. Use [Windows Security](www.pcmag.com/reviews/microsoft-windows-defender-security-center). This built in tool is surprisingly competent at removing any malware and is definitely more than sufficient for most users.
2. Follow the on-screen guides of Windows Security and you're good to go.
3. Don't use 3rd party tools *at all* unless you know what you're doing.

## Hardware Maintenance
There's not much you need to do hardware wise to keep your system fresh. If you have competent dust filters you don't even need to clear dust that often. If you do need to clear dust, use compressed air and just about any brush would work. 

Compressed air tends to be much more powerful and focused than your hairdryer, which doesn't do much *at all* to stubborn dust in a PC case.

1. Take off the GPU shroud to get easier access to the fins and fans.
2. Blow with compressed air until it's clean.
3. If you're too lazy to install the shroud back on, sure, it doesn't do anything except block airflow and makes your hardware looks better.

That's it for hardware maintenance, there's zero reasons for you to do anything except swapping parts because of failures or upgrades once you built your rig.


[^1]: IMC stands for Integrated Memory Controller. It's "integrated" because on ancient systems (pre-2011) it's the northbridge that interfaces with the memory.
[^2]: For more details about memory testing software and DDR4 OC in general, read [this excellent article](https://github.com/integralfx/MemTestHelper/blob/oc-guide/DDR4%20OC%20Guide.md#memory-testing-software) written by Integralfx.
[^3]: You could try undervolting your CPU or at least control it's power using [ThrottleStop](https://www.techpowerup.com/download/techpowerup-throttlestop), or simply lower the frequency and voltage via the BIOS. For the GPU, [MSI AB](https://msi.com/Landing/afterburner) or any popular GPU overclocking app can limit the GPU's power consumption.
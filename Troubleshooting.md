# Table of Contents
- [Table of Contents](#table-of-contents)
- [What's the issue?](#whats-the-issue)
	- [Your first build isn't booting](#your-first-build-isnt-booting)
	- [Advanced troubleshooting](#advanced-troubleshooting)


# What's the issue?
If you're reading this, I assume there is absolutely no reactions out of the PC when you're pressing the power button. There might be fans spinning but nothing coming out of the display. If that's the case, continue reading!

## Your first build isn't booting
I assume you just came from [Essential Information](Essential%20Information.md), looking for a way to troubleshoot why your build isn't booting. 

1. Check the cables. Odds are you forgot one of those, or even forgot to turn the PSU on. Here's a list of the cables you need.
    - 24 pin cable to the motherboard, on the right of the RAM slots.
	- 4/8/12 pin for the CPU, depending on the motherboard. The cables are all bundled together in multiples of four and marked CPU. This is on the top right of the motherboard.
	- Several cables marked PCIe, these are for the GPU, and depending on the card installed it could be 6, 8, 14, 16, or more pins. Always group one 6+2 cable into one bundle, and **never** daisy chain one 6+2 cable into two connectors on the GPU.
2. Where did you plug the display cable? If you have a discrete GPU, put the display cable in there, unless you're planning to use the integrated GPU.
3. Is the case front panel wired up? one of the cables might be in the wrong place, double check with the motherboard manual to see if that's the case.
4. A common place for builds to not boot is incorrectly is the RAM stick isn't in correctly. They require some ridiculous force to stick in and even then one side might not be inserted correctly.
5. It's hightly recommended to stick the GPU in the topmost PCIe slot. You might loose performance but it shouldn't cause too much issues, unless you have other devices each occupying their own slot. 
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

- First off, if you have **any overclock**, reset it back to stock unless you know what you're doing. 
- RAM and the CPU's IMC[^note] might be a bad pair, especially with older CPUs running DDR4 3200 and above. 

[^note]: Integrated Memory Controller
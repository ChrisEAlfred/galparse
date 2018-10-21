# PLDs

## G540 programmer

`ONLY WORKS IN XP`

`Set : Set Programming Operation Sequence, Remove Verify and Encrypt` These settings are lost every startup!!!!!!!

The G540 PAL programmer uses a non-standard .JED format.

### Read a PLD

Remeber: `Set : Set Programming Operation Sequence`

- Click `Read`
- `File : Save (S)`
- Select `JEDEC`
- Click `OK`

`The read file is ok, the saved file is wrong. You have to manually read the bits.`

### g540jedec

Convert CUPL compiler .JED to G540 compatible format.

Arguments:

- .JED from CUPL compiler
- Output file (.JED format for G540)

---

## CUPL Compiler

*ONLY WORKS IN XP*

Setup:

~~~
cuplsetup.bat
~~~

Compilation to .jed file:

~~~
cupl -j <.pld source file>
~~~

Conversion for G540 programmer (can be done in Windows 10):

~~~
python.exe g540jedec.py ..\CG3\SYNCGAL\SYNCGAL5.JED ..\CG3\SYNCGAL\SYNCGAL5_g540.JED
~~~

---


## GAL22V10 parsing

### gal22v10parse

Parse a .JED file and convert to logic equations.

Arguments:

- .JED source
- List of pin names separated by spaces in order of pins (skipping power pins 12,24)

Example:

~~~
python.exe .\gal22v10parse.py ..\CG3\SYNCGAL5_g540.JED "v5 h3 h2 h1 h0 h4 h5 hblank v6 v2 v3 v4 lin
c lastl lrst v9 v8 l512 hsync vsync blank vscrst"
~~~

---

# CG3

IOGAL2

~~~
python.exe .\gal22v10parse.py '..\CG3\IOGAL2\iogal2_readback.jed' "CA DBCAS L512 LA1 LA3 LA0 VRAMn
 IOSELn LA4 LA2 LP1SELn LADD1 CPUADD DBENn RAMENn S2 S1 S0 XDN XUP YDN YUP"
~~~

OUTPUT4

~~~
python.exe .\gal22v10parse.py '..\CG3\OUTPUT\output4_readback.jed' "DOTCLK AT14 PD0 PD1 PD2
 PD3 PD4 PD5 PD6 PD7 WSTRBn UNK SEL0 SEL1 SBLU PBLU SGRN PGRN PRED SRED HS VS"
~~~

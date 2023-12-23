# CPU-and-Assembler
CPU and Assembler
by Lili Fortes and Sean Payba

How to use the assembler:
Our assembly language has 6 instructions: `LDR Rt, [Rn, Rm]`, `LDR Rt, [Rn, imm6]`, `ADD Rd, Rn, Rm`, `ADD Rd, Rn, imm6`, `SUB Rd, Rn, Rm`, and `SUB Rd, Rn, imm6`. Each instruction’s usage is detailed in the CPU architecture section.

To create our assembly program, you must have “makefile.py” in the same folder as an “instructions.txt” file so that the makefile can read instructions and data from the instruction file. The general structure of the instruction file must be a .text segment at the top containing all of your instructions, and a .data section under the .text section containing addresses and the data you plan to store in them.

In the .text section, you write the instructions using our mnemonics as described. Each instruction must be on its own line. You can make comments in your code both in line and on their own lines using “//” preceding your comment. Any text between “//” and the end of the line is ignored by the assembler.

More details in documentation: "CS382: CPU and Assembler Manual"

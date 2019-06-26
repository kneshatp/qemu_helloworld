import argparse

def gen_script_test(name):
    script = "volatile unsigned int * const UART0DR = (unsigned int *)0x101f1000;\n"
    script += """
 
void print_uart0(const char *s) {
 int count = 0; 
 while(count < 100) { /* Loop until end of string */
 *UART0DR = (unsigned int)(*s); /* Transmit char */
 s++; /* Next char */
 count ++;  
 }
}
 
void c_entry() {
 print_uart0("Hello world from %s!\\n");
register int reg0 asm("r0");
register int reg1 asm("r1");
reg0 = 0x18;    // angel_SWIreason_ReportException
reg1 = 0x20026; // ADP_Stopped_ApplicationExit

asm("svc 0x00123456");
}"""%(name)
    return script

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    args = parser.parse_args()
    name = args.name
    script = gen_script_test(name)
    outfile = open('test_%s.c'%(name), 'w')
    outfile.write(script)
    outfile.close()


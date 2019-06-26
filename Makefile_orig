ARMGNU = arm-none-eabi
MCPU = -mcpu=arm926ej-s 

hello : startup.s test.c test.ld 
	$(ARMGNU)-as $(MCPU) -g startup.s -o startup.o
	$(ARMGNU)-gcc -c $(MCPU) -g test.c -o test.o
	$(ARMGNU)-ld -T test.ld test.o startup.o -o test.elf 
	$(ARMGNU)-objcopy -O binary test.elf test.bin
run:
	qemu-system-arm -M versatilepb -m 128M -nographic -kernel test.bin -semihosting > test.log
	
clean:
	rm *.o
	rm *.elf
	rm *.bin

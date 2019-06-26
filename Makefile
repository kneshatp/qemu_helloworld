ARMGNU = arm-none-eabi
MCPU = -mcpu=arm926ej-s 

STATIONS = iss iss2

all:
	$(ARMGNU)-as $(MCPU) -g startup.s -o startup.o
	$(foreach station,$(STATIONS),python gen_test.py $(station);)
	$(foreach station,$(STATIONS),$(ARMGNU)-gcc -c $(MCPU) -g test_$(station).c -o test_$(station).o;)
	$(foreach station,$(STATIONS),$(ARMGNU)-ld -T test.ld test_$(station).o startup.o -o test_$(station).elf;)
	$(foreach station,$(STATIONS),$(ARMGNU)-objcopy -O binary test_$(station).elf test_$(station).bin;)
	$(foreach station,$(STATIONS),rm test_$(station).c test_$(station).elf;)
	rm *.o


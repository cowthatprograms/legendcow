import pyperclip as p
a = {"a":";","b":";-;;","c":";-;","d":";-;;-;;","e":";-;;-;","f":";-;-;;","g":";-;-;","h":";-;;-;;-;;","i":";-;;-;;-;","j":";-;;-;-;;","k":";-;;-;-;","l":";-;-;;-;;","m":";-;-;;-;","n":";-;-;-;;","o":";-;-;-;","p":";-;;-;;-;;-;;","q":";-;;-;;-;;-;","r":";-;;-;;-;-;;","s":";-;;-;;-;-;","t":";-;;-;-;;-;;","u":";-;;-;-;;-;","v":";-;;-;-;-;;","w":";-;;-;-;-;","x":";-;-;;-;;-;;","y":";-;-;;-;;-;","z":";-;-;;-;-;;","A":"-;","B":"-;-;;","C":"-;-;","D":"-;-;;-;;","E":"-;-;;-;","F":"-;-;-;;","G":"-;-;-;","H":"-;-;;-;;-;;","I":"-;-;;-;;-;","J":"-;-;;-;-;;","K":"-;-;;-;-;","L":"-;-;-;;-;;","M":"-;-;-;;-;","N":"-;-;-;-;;","O":"-;-;-;-;","P":"-;-;;-;;-;;-;;","Q":"-;-;;-;;-;;-;","R":"-;-;;-;;-;-;;","S":"-;-;;-;;-;-;","T":"-;-;;-;-;;-;;","U":"-;-;;-;-;;-;","V":"-;-;;-;-;-;;","W":"-;-;;-;-;-;","X":"-;-;-;;-;;-;;","Y":"-;-;-;;-;;-;","Z":"-;-;-;;-;-;;",".":";-;-;;-;-;",",":";-;-;-;;-;;","?":";-;-;-;;-;","!":";-;-;-;-;;","-":";-;-;-;-;",";":";-;;-;;-;;-;;-;;","\"":";-;;-;;-;;-;;-;","'":";-;;-;;-;;-;-;;","(":";-;;-;;-;;-;-;",")":";-;;-;;-;-;;-;;"," ":""}
def b(c): return "'".join([a[b] for b in c])
while True: c = input("Enter some text: "); print(b(c)); p.copy(b(c))
def fish():
    print("i m tuna")
fw=open('sample.txt','w')
fw.write('writing some stuff\n')
fw.write('i like bacon\n')
fw.close()
fr=open('sample.txt','r')
text=fr.read()
print(text)
fr.close()
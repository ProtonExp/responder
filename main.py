name = input('What is your name or code?\n')
dev = False
dev2 = True
usercmd = False


print('Hi, %s.' % name)
print('This is what the program has to say about you:')
print(' ')
if name == ('Kabelo'):
  print('A boy with an entire ecosystem living in his hair')
if name == ('Luc'):
  print('A kind hearted and quiet boy')
if name == ('Layla'):
  print('Her favourite saying is: I will fight you!')
if name == ('Tristan Cremer'):
  print('Your the guy who coded this :)')
if name == ('Mpumelelo'):
  print('A guy who likes pixel starships')
if name == ('1960') :
  print('Devoper Commands Loaded')
  print('You can now run developer commands')
  print('You can run x different commands')
  
  cmdmenu = input('Command id\n')
  if cmdmenu == ('1') :
    print(' ')
    print('Here are the registered users:')
    print('Tristan Cremer')
    print("Mpumelelo")
    print('Layla')
  if cmdmenu == ('0') :
    print('Run a command')
    cmdmenu = input('')
    



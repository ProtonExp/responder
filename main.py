name = input('What is your name or code?\n')
dev = False
dev2 = True
usercmd = False


print('Hi, %s.' % name)
print('This is what the program has to say about you:')
print(' ')
if name == ('Madison'):
  print('Quiet kind and smart')
if name == ('Keira'):
  print('The one mpumi called Kira')
if name == ('Thando'):
  print('Raging in Shadow Fight 2')
if name == ('Dawn and Des'):
  print('AND THE SEAGULLS NAME WAS NELSON')
if name == ('Sarah'):
  print('I do not know I will have to ask')
if name == ('Emily'):
  print('Smart and really stares into your soul')
if name == ('Zizi'):
  print('Bear')
if name == ('Owenkosi'):
  print('Always touching others chromebooks')
if name == ('Michaela'):
  print('Toxicity killed... well I dont know')
if name == ('Londani'):
  print('Soccer... laughing... soccer...')
if name == ('Angelica'):
  ('Smart, kind and always taking notes!')
if name == ('Kabelo'):
  print('A boy with an entire ecosystem living in his hair')
if name == ('Luc'):
  print('A kind hearted and quiet boy')
if name == ('Layla'): #Edited for safety reasons
  print('Her favourite saying is: I will fight you!')
if name == ('Tristan Cremer'):
  print('The overweight guy who coded this :)')
if name == ('Mpumelelo'):
  print('A guy who is nice, (and also helped code this)') 

if name == ('Ella Minnie'): 
  print('Has almost no breaking point')

else:
  print(' Specified Person does not exist in DB')
  print(' We will add a feature in future that lets you')
  print(' easily add a person.')
  exit()
if name == ('1960') :
  print('Devoper Commands Loaded')
  print('You can now run developer commands')
  
  
  cmdmenu = input('Command id\n')
  if cmdmenu == ('1') :
    print(' ')
    print('Here are the registered users:')
    print('Tristan Cremer')
    print("Mpumelelo")
    print('Layla')
    print('Londani')
    print('Angelica')
    print('Luc')
    print('Michaela')
    print('Owenkosi')
    print('Zizi')
    print('Emily')
    print('Ella Minnie')
    print('Sarah')
    print('Dawn and Des')
    print('Thando')
    print('Keira')
    print('Madison')

  if cmdmenu == ('2'):
    print('Change the details of a user')
    print('Currently Unnavailable')
  if cmdmenu == ('0') :
    print('Run a command')
    cmdmenu = input('')
  else :
    print('Command does not exist')
    exit()
    
    


#Version 0.1.6
#By Tristan And Mpumelelo
#We ask that you dont steal this code :)
zombies, distance, ammo = 0, 45, 20
kill = 0
result = ''

while ammo > 0 and distance > 0 and zombies > 0:
    distance -= 0.5
    zombies -= 1
    kill += 1
    ammo -= 1
    if zombies == 0:
        print('You shot all', zombies, 'zombies.')
if distance != 0:
    print('You shot', kill, 'zombies before being eaten: ran out of ammo.')
else:
    print('You shot', kill, 'zombies before being eaten: overwhelmed.')
print(zombies, distance, ammo, '\nkill :', kill)
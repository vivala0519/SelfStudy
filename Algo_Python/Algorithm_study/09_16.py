lamps = 'xxxxxxxxx'
drone = '==T'

lamps = list(lamps)
print(lamps)
drone = list(drone)
print(drone)
print(drone.index('T'))
for i in range(0, drone.index('T')+1):
    lamps[i] = 'o'
print(lamps)
lamps = ''.join(lamps)
print(lamps)
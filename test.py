'''DMG_REDUC = .03
healthpool = 100
"""lets say a boss hits you with an attack that tells the player
    a satisfying number like 500. we then take that number and do number*.03 
    so its able to be realisticly subtracted from the healthpool"""
def take_damage(healthpool:int, hit:bool, damage:int)->int:
    if hit:
        true_dmg = damage* DMG_REDUC
        healthpool = healthpool - true_dmg

take_damage(healthpool, True, 200)
'''
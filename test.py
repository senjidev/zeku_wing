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


#COLLISION TEST
"""COLLISION DETECTION"""
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list



"""MOVE FUNCTION"""
def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

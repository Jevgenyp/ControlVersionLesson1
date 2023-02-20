# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 24]
# print(values)
# transformed_values = list(map(transformation, values))
# print(transformed_values)

def find_farthest_orbit(my_list):
    maxi = 0
    korteg = ()
    for elem in my_list:
         
        if elem[0] == elem[1]:
            continue
       
        s = 3.14 * elem[0] * elem[1]
        if s > maxi:
            maxi = s
            korteg = elem
    return korteg
        
orbits = [(1,3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))
        
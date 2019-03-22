import math

#this function uses the coordinates given to calculate the center of mass,

def create_coordinate_list(nmbr):
    while nmbr > 0:
        
        input_coords = input("Please provide the coordinates in X and Y form such that for x = 5 and y = 4 please provide (5,4)")
        
        coordinates = (int(input_coords.split(',')[0][1:]) , int(input_coords.split(',')[1].split(')')[0]))
        
        coord_list.append(coordinates)
        nmbr -= 1
        
    print("Coordinate list: ",coord_list)

    

#this function calculate center of mass and gives is as a tuple
def calculate_center_of_mass(nmbr):
    CorX     = 0
    CorY     = 0
    indx = 0
    
    
    while nmbr > 0:
        CorX     += coord_list[indx][0]
        CorY     += coord_list[indx][1]
        nmbr   -= 1
        indx += 1
        
        
    CorX = CorX / indx
    CorY = CorY / indx
    
    print("The center of mass: ", (CorX,CorY))
    return (CorX, CorY)
    
#to calculate the dist. of coordinates to com use the following function

def euclidean_distance(nmbr):
    indx = 0
    
    while nmbr > 0:
        x     = 0
        y     = 0
        x     += (com[0] - coord_list[indx][0])**2
        y     += (com[1] - coord_list[indx][1])**2
        
        euclidean = math.sqrt(x + y)
        euclidean_list.append(euclidean)
        nmbr      -= 1
        indx    += 1
    
    print("The list of distance of: ", euclidean_list)



#the closest farthest points
def far_close_points(nmbr):
    indx = 0
    min_dist = min(euclidean_list)
    max_dist = max(euclidean_list)
    
    while nmbr > 0:
        if min_dist == euclidean_list[indx]:
            print("The closest point is : ", coord_list[indx])
        if max_dist == euclidean_list[indx]:
            print("The farthest point is: ", coord_list[indx])
        indx += 1
        nmbr   -= 1
    


if __name__ == "__main__":
    
    coord_list = []

    print("Please provide the number of coordinate pairs.")
    a = input()
    
    # tot_num_of coordinates
    num_elements = int(a)
    print("The number of coordinate pairs is: ", num_elements)
    
    # create_coordinate_list function call
    create_coordinate_list(num_elements)
    
    # call: calculate_center_of_mass funcs
    com = calculate_center_of_mass(num_elements)
    
    euclidean_list = []
    
    # call: euclidean_distance funcs
    # calculate all distances, and save them to euclidean_list
    euclidean_distance(num_elements)
    
    # call:far_close_point funcs
    far_close_points(num_elements)
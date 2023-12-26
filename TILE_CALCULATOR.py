###THIS IS THE TILE CALCULATOR FOR MY DAD###
def notes():
    """12/23 Notes:
            formulas finally works
            only take in values in inches
            displays if you can use excess tile to start next rows
            displays amount of tile needed + 10%
            not combatile with CMD, needs to be manually input through python (not user friendly)
            assumes floor, walls, and shower pan are all rectangular
            does NOT incorperate lip of shower pan (negligable)
            dad approved, will continue
        
            made usable in cmd and other inputs
            input more measurements and added failsafes
            made wall tile extra a multiple of 1.2 for the shower lip
        
        future functions:
                for refrence, 1 in = 2.54 cm
            amount of boxes needed
            price of tile total
            grout calculator
            """





import math

class Dimensions:
    def __init__(
            self, floor_length, floor_width, floor_tile_length, 
            floor_tile_width, shower_length, shower_width, shower_floor_tile, 
            wall_height, wall_tile_width, wall_tile_length, 
            floor_grout_thickness = 0.125, wall_grout_thickness = 0.125,
            number_of_shower_walls = 2
            ):
        self.floor_length = floor_length
        self.floor_width = floor_width
        self.floor_tile_length= floor_tile_length
        self.floor_tile_width= floor_tile_width
        self.shower_length= shower_length
        self.shower_width= shower_width
        self.shower_floor_tile= shower_floor_tile
        self.wall_height = wall_height
        self.wall_tile_length= wall_tile_length
        self.wall_tile_width= wall_tile_width
        self.floor_grout_thickness= floor_grout_thickness
        self.wall_grout_thickness= wall_grout_thickness
        self.number_of_shower_walls = number_of_shower_walls
        
        if floor_tile_width > floor_tile_length:
            floor_tile_width, floor_tile_length = floor_tile_length, floor_tile_width
        
        if floor_width > floor_length:
            floor_width, floor_length = floor_length, floor_width
        
        if wall_tile_width > wall_tile_length:
            wall_tile_width, wall_tile_length = wall_tile_length, wall_tile_width
        
        
            
### ALL THE TILES ARE NOW LINED UP LIKE BRICKS###


     
        
    def floor_tile_area_formula(self):
        halfable_floor_tile_lengths = False
        halfable_floor_tile_widths = False
        
        number_of_floor_tile_rows = self.floor_width // (self.floor_tile_width + self.floor_grout_thickness)
        if self.floor_width / (self.floor_tile_width + self.floor_grout_thickness) >= self.floor_tile_width/2:
            halfable_floor_tile_widths = True
        
        number_of_floor_tiles_per_row = self.floor_length // (self.floor_tile_length + self.floor_grout_thickness)        
        if self.floor_length / (self.floor_tile_length + self.floor_grout_thickness) >= self.floor_tile_length/2:
            halfable_floor_tile_lengths = True
            
        return (
            number_of_floor_tiles_per_row, number_of_floor_tile_rows, 
            halfable_floor_tile_widths, halfable_floor_tile_lengths
            )
    
    
    def shower_pan_area_formula(self):
        shower_area = (self.shower_length * self.shower_width)/144
        
        return shower_area
        
    
    
    def shower_walls_area_formula(self):
        
        number_of_wall_tiles_per_back_row = self.shower_width // (self.wall_tile_length + self.wall_grout_thickness)
        if self.shower_width / (self.wall_tile_length + self.wall_grout_thickness) >= self.wall_tile_length/2:
            halfable_wall_tile_lengths = True
        
        number_of_rows_of_wall_tile = self.wall_height // (self.wall_tile_width + self.wall_grout_thickness)
        if self.wall_height/ (self.wall_tile_width + self.wall_grout_thickness) >= self.wall_tile_width/2:
            halfable_wall_tile_heights = True
        
        number_of_wall_tiles_per_side_row = math.ceil(self.shower_length / (self.wall_tile_length + self.wall_grout_thickness))
        
        
        return (
            number_of_rows_of_wall_tile, number_of_wall_tiles_per_back_row, 
            halfable_wall_tile_heights, halfable_wall_tile_lengths, 
            number_of_wall_tiles_per_side_row
            )
        
        
### ALL FORMULAS ARE NOW DEFINED ###


    def floor_tile_needed(self):

        (
         number_of_floor_tiles_per_row, number_of_floor_tile_rows, 
         halfable_floor_tile_widths, halfable_floor_tile_lengths
         ) = self.floor_tile_area_formula()
        
        floor_tiles_needed = number_of_floor_tiles_per_row * number_of_floor_tile_rows
    
        if halfable_floor_tile_lengths:
            print("You can use the back half of the floor tile for the next row")
            floor_tiles_needed = floor_tiles_needed - int((number_of_floor_tile_rows) / 2)
    
        if halfable_floor_tile_widths:
            print("When finishing the floor, you can use the back half of the cut for the next piece")
            floor_tiles_needed = floor_tiles_needed - int((number_of_floor_tiles_per_row) / 2)
    
        # CRUCIAL 10% MATERIAL INCREASE FOR CUTS ETC
        floor_tiles_needed = floor_tiles_needed * 1.1
    
        return f"You will need to purchase approximately {math.ceil(floor_tiles_needed)} floor tiles for this job \n"
    
    #THIS FORMULA ASSUMES SHOWER PAN TILE IS 12" X 12", WHICH IT TYPICALLY IS
    def shower_pan_tile_needed(self):
        
        shower_area = self.shower_pan_area_formula()
        
        shower_pan_tiles_needed = math.ceil(shower_area)
        
        return f"You will need to purcahse approximately {math.ceil(shower_pan_tiles_needed)} of shower pan tiles for this job \n"

    
    
    def wall_tile_needed(self):
        
        (
            number_of_rows_of_wall_tile, number_of_wall_tiles_per_back_row,
            number_of_wall_tiles_per_side_row,
            halfable_wall_tile_heights, halfable_wall_tile_lengths
        ) = self.shower_walls_area_formula()
        
        number_of_shower_walls = self.number_of_shower_walls
        
        
        wall_tiles_needed = (
            (number_of_rows_of_wall_tile * number_of_wall_tiles_per_back_row) + 
            (number_of_rows_of_wall_tile * (int(number_of_shower_walls) -1) * number_of_wall_tiles_per_side_row)
            )
        
        if halfable_wall_tile_lengths is True:
            print("You can use the back half of the wall tile to start halves for the next row")
            wall_tiles_needed = wall_tiles_needed - int((number_of_rows_of_wall_tile)/2)
        
        if halfable_wall_tile_heights is True:
            print("You can use the back half of the wall tile as a double to finish the last row of wall tile")
            wall_tiles_needed = wall_tiles_needed - int((number_of_rows_of_wall_tile * (int(number_of_shower_walls) -1) * number_of_wall_tiles_per_side_row)/2)
        
        #CRUCIAL 10% MATERIAL INCREASE FOR CUTS ETC
        wall_tiles_needed = wall_tiles_needed * 1.2
        
        return f"You will need to purchase approximately {math.ceil(wall_tiles_needed)} wall tiles for this job"

    

###ALL AREAS ARE NOW CALCULATED###


def test_code():

   """tile_job_one = Dimensions(
                        floor_length = 240,
                        floor_width = 120,
                        floor_tile_length = 12, 
                        floor_tile_width = 6,
                        shower_length = 60,
                        shower_width = 36,
                        shower_floor_tile = "12 x 12",
                        wall_height = 96,
                        wall_tile_width = 3,
                        wall_tile_length = 6,
                        floor_grout_thickness = 0.125,
                        wall_grout_thickness = 0.125,
                        number_of_shower_walls = 3)
            
    #tile_job_one = Dimensions(240, 120, 12, 6, 60, 36, "12 x 12", 96, 3, 6, 0.125, 0.125, 2)
        
        
    print(tile_job_one.floor_tile_needed())
        
    print(tile_job_one.shower_pan_tile_needed())
        
    print(tile_job_one.wall_tile_needed())"""
    
    
    
def dimensions_and_unit(q):
    while True:
        value_and_unit = input(q)
        value_and_unit_split = value_and_unit.split()
        
        unit = value_and_unit_split[-1].lower()
        if len(value_and_unit_split) != 1 and len(value_and_unit_split) != 2:
            print("Please input a valid measurement.")
        elif len(value_and_unit_split) == 3:
            value = float(value_and_unit_split[0] + float(value_and_unit_split[1]))
        else:
            value = float(value_and_unit_split[0])
        
        if unit == "in" or unit == "inches":
            return value
        elif unit == "ft" or unit =="feet":
            return value * 12
        elif unit == "cm" or unit == "centimeters":
            return value/2.54
        elif unit == "mm" or unit == "millimeters":
            return value/25.4
        else:
            print("Please input a valid unit of measurement.")
        

def get_user_input():

    floor_length = dimensions_and_unit("What is the length of the bathroom floor? \n length: ")    
    floor_width = dimensions_and_unit("What is the width of the bathroom floor? \n Width: ")
    floor_tile_length = dimensions_and_unit("What is the length of the floor tile? \n Length:")
    floor_tile_width = dimensions_and_unit("What is the width of the floor tile? \n Width:")
    shower_length = dimensions_and_unit("What is the length of the shower? \n Length :")
    shower_width = dimensions_and_unit("What is the width of the shower? \n Width:")
    shower_floor_tile = input("We are just going to assumem that it's 12 x 12, please input any value.")
    wall_height = dimensions_and_unit("What is the height of the wall? \n Height:")
    wall_tile_width = dimensions_and_unit("What is the width of the wall tile? \n Width:")
    wall_tile_length = dimensions_and_unit("What is the length of the wall tile? \n Height:")
    floor_grout_thickness = dimensions_and_unit("How thick are the grout lines for the floor tile? \n Thickness:")
    wall_grout_thickness = dimensions_and_unit("How thick are the grout lines for the wall tile? \n Thickness:")
    number_of_shower_walls = input("How many walls will the shower be tiled for the shower? \n Walls:")


    dimensions = Dimensions(
        (floor_length), (floor_width), (floor_tile_length), (floor_tile_width), 
        (shower_length), (shower_width), (shower_floor_tile), (wall_height), 
        (wall_tile_width), (wall_tile_length), (floor_grout_thickness), 
        (wall_grout_thickness), (number_of_shower_walls)
    )

    print(dimensions.floor_tile_needed())
    print(dimensions.shower_pan_tile_needed())
    print(dimensions.wall_tile_needed())
    
    input("Press any key to close the program...")


get_user_input()












#import sys

#args = sys.argv[1:]

#args = [float(arg) for arg in args]

#dimension = Dimensions(*args)

#print(dimension.floor_tile_needed())
#print(dimension.shower_pan_tile_needed())
#print(dimension.wall_tile_needed())






















        
        
        
        
        
        
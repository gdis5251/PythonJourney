# Functions calls and arguments
def mult_two_add_three(number):
      print(number*2 + 3)
  
# Call mult_two_add_three() here:
mult_two_add_three(0)


# Make the function more flexible
def mult_x_add_y(number, x, y):
      print(number*x + y)
  
mult_x_add_y(1, 3, 1)


# Function defalut parameter
# Define create_spreadsheet():
def create_spreadsheet(title = "Applications", row_count = 10):
  print("Creating a spreadsheet called "+title + "with " + str(row_count) + " rows")

# Call create_spreadsheet() below with the required arguments:
create_spreadsheet()


# Function return practice
def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age

my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)

print("I am " + str(my_age) + " years old and my dad is " + str(dads_age) + " years old")


# return two value
def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = target + margin
    return low_limit, high_limit

low, high = get_boundaries(100, 20)


# Define globel varible
current_year = 2048

def CalculateAge(birth_year):
  age = current_year - birth_year
  return age
  

print(current_year)
print(CalculateAge(1970))

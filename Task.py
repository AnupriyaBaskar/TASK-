# # Dice Challenge 

# # Total combinations 

# # PART A

def total_combinations():
    die_faces = [1,2,3,4,5,6]
    total_combinations = 0

    for face_a in die_faces:
        for face_b in die_faces:
            total_combinations += 1

    return total_combinations

result = total_combinations()
print(f'Total combinations: {result}')

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

# permutations 

def get_permuations(n,r):
    result = factorial(n)//factorial(n-r)
    return result

a = get_permuations(6,2)
print(f'Total Permutations: {a}')
# Finding the combinations of when 2 dice rolled simultaneouly and creating a 6 X 6 Matrix

A = [1,2,3,4,5,6] 
B = [1,2,3,4,5,6]

total_outcomes = []
matrix = []


for i in A:
    final = []
    for j in B:
        final.append((i,j))
    matrix.append(final)

print(matrix)

#Calculate the Probability of all Possible Sums occurring among the number of combinations from (2).


A = [1,2,3,4,5,6]
B = [1,2,3,4,5,6]

# Create a matrix of all possible pairs from A and B
matrix = [(i, j) for i in A for j in B]

# Find pairs with a sum of 5
for pair in matrix:
    k, s = pair
    if k + s == 11:
        print(pair)



# Part B 

def undoom_dice(Die_A, Die_B):
    New_Die_A = [1, 2, 2, 3, 3, 4]  # New_Die_A = [1, 2, 2, 3, 3, 4]
    New_Die_B = Die_B  # No change in Die_B
    return New_Die_A, New_Die_B

Die_A = [1,2,3,4,5,6]
Die_B = Die_A
result = undoom_dice(Die_A,Die_B)
print(result)          
    





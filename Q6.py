def pattern_1(n):
    for i in range(n+1):
        print("\n");
        print((n-i) * "   ", end="");
        for j in range(i):
            print((j+1), " ", end="");
    print("\n");
    
pattern_1((int(input("enter the number of rows: "))));

def pattern_2(p):
    for i in range(p):
        print((p-i)* " ", end="");
        print((2*(i+1)-1)* "*", end="");
        print("");

    for j in range(p-1, -1, -1):
        print((p-j)* " ", end="");
        print((2*(j+1)-1)* "*", end="");
        print("");

pattern_2((int(input("enter the number of rows each triangle: "))));

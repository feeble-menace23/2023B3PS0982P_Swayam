def dictionary(lis1, lis2, r):
    dict = {};
    for i in range(r):
        dict[lis1[i]] = lis2[i];
    print(dict);

keys = [];
values = [];
n = int(input("enter number of elements in each list: ")); 
print("enter elements of list 1:")
for j in range(n):
    m = input();
    keys.append(m);

print("enter elements of list 2:")
for k in range(n):
    m = input();
    values.append(m);

dictionary(keys, values, n);

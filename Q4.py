def unduplicator():
    el = [];
    n = int(input("enter the number of elements\n"));
    print("enter all elements:");

    for i in range(n):
        a = input();
        el.append(a);

    for j in range(n):
        check = el[j];
        if(check != '*'):
            for k in range(n):
                if el.index(check) != k:
                    if el[k] == check:
                        el[k] = '*';

    print("new list without duplicates:");

    for l in range(n):
        if(el[l] != '*'):
            print(el[l], end=" ");
unduplicator();

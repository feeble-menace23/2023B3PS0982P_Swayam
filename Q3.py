def sec_largest():
    el = [];
    n = int(input("enter the number of elements\n"));
    print("enter all elements");

    for i in range(n):
        a = float(input());
        el.append(a);
    
    max = el[0];
    secmax = el[1];
    if(secmax > max):
        max, secmax = secmax, max;

    for j in el:
        if j > max:
            secmax = max;
            max = j;
        elif j == max:
            continue
        elif j > secmax:
            secmax = j

    print("second largest element in list:\n", secmax);

sec_largest();

def vowel_counter():
    abc = [];
    max = 0;
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
    n = int(input("enter the number of strings\n"));
    print("enter all strings")

    for i in range(n):
        a = input();
        abc.append(a);
    
    for j in range(n):
        count = 0;
        for k in abc[j]:
            if k in v:
                count += 1;
        if count>max:
            max = count;
            sv = abc[j];
        elif count==max:
            sv = sv + ", " + abc[j];
    
    print("strings with most vowels: \n", sv);

vowel_counter();

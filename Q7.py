def time_angulator():
    time=input("enter the time in 24hr format as hh:mm\n");
    hh=float(time[0:2]);
    mm=float(time[3:]);

    if hh>12:
        hh -= 12;

    angm = mm*6;
    angh = hh*30 + 0.5*mm;

    angr = abs(angm-angh);

    if angr>180:
        angr = 360-angr;

    print("the angle between minute and hour hand is:", angr, "degrees");
time_angulator();

def primos(num1, num2):

    for i in range(num1, num2):

        primo = True

        for x in range(2, i):

            if i % x == 0:
                primo = False

        if primo is True:
            print(i)
        primo = True


a = int(input("Itroduce el primer digito "))
b = int(input("Introduce el segundo digito "))

primos(a, b)

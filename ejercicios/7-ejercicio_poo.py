class CuentaCorriente():

    def __init__(self, n_cuenta, titular, saldo):
        self.n_cuenta = n_cuenta
        self.titular = titular
        self.saldo = saldo

    def getDatos(self):

        return "El número de cuenta: " + self.n_cuenta + " pertenece a " + self.titular +\
            " y tiene en cuenta " + str(self.saldo) + "€"

    def ingresarDinero(self, cantidad):

        cantidad = self.saldo

        self.saldo = self.saldo + cantidad

        return print("Has ingresado: " + str(cantidad) + " que sumados a tú saldo anterior: " +
                     str(cantidad) + " hacen un total de: " + str(self.saldo))

    def retirarDinero(self, cantidad):

        if self.saldo - cantidad > 0:

            self.saldo = self.saldo - cantidad

            return print("Tú saldo actual después de retirar: " + str(cantidad) + " es de: " +
                         str(self.saldo) + "€"
                         )
        else:

            return print("Saldo insuficiente, tu saldo es: " + str(self.saldo))


c1 = CuentaCorriente("1", "Marcos", 10000)

print(c1.getDatos())

c1.ingresarDinero(10000)

print(c1.getDatos())

c1.retirarDinero(10000)

print(c1.getDatos())

c1.retirarDinero(20000)

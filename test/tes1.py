
if __name__ == '__main__':#example

    def action_read(value):
        print(value)

    s = BSerial(port='COM1',baudrate=9600)
    s.start_read_string_port(action_read)

    while True:
        valor = input("Ingrese un valor - x para terminar")
        if valor == "x":break
        s.write_string_port(valor)
        sleep(1)#only for sthetic, i you wish try like comment
    s.stop_read_string_port()
    s.close()
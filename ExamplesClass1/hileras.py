for primer_multiplo in range(0, 10):
    for segundo_multiplo in range(0, 10):
        resultado = primer_multiplo * segundo_multiplo
        print('{} x {} = {}'.format(primer_multiplo, segundo_multiplo, resultado))

message = 'Alejandra Alvarez Alfaro'
print(len(message))

print(message[10])

print(message[len(message)-1])

print(message[10:17])
print(message[:5])
print(message[4:])
print(message.upper())
print(message.lower().replace(' ', ''))
print(message.lower().split(' ')[1])



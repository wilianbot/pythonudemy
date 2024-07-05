a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)

print(formato)


string = 'a={0} a={0} b={1} c={2:.2f}'
formato = string.format(a, b, c)

print(formato)


string = 'a={0} a={0} b={1} c={nome3:.2f}'
formato = string.format(
    a, b, nome3=c)

print(formato)
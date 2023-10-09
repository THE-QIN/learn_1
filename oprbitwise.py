# operator bitwise, operasi biner atau binary
# bitwise = OR(|), AND (&), XOR (^), NOT (~), ZERO FILL LEFT SHIFT (<<), SIGNED RIGHT SHIFT (>>)

a = 9
b = 5

# bitwise or (|)
c = a | b
print('\n========OR========')
print('nilai :',a,' , binary :',  format (a, '08b'))
print('nilai :',b,' , binary :',  format (b, '08b'))
print('-------------------------------(|)')
print('nilai :',c,' ,binari :',  format(c, '08b'))

# bitwise AND (&)
c = a & b
print('\n========AND========')
print('nilai :',a,' , binary :',  format (a, '08b'))
print('nilai :',b,' , binary :',  format (b, '08b'))
print('-------------------------------(&)')
print('nilai :',c,' ,binari :',  format(c, '08b'))

#biswise XOR (^)
c = a ^ b
print('\n========XOR========')
print('nilai :',a,' , binary :',  format (a, '08b'))
print('nilai :',b,' , binary :',  format (b, '08b'))
print('-------------------------------(^)')
print('nilai :',c,' ,binari :',  format(c, '08b'))

#bitwise NOT (~)
c = ~a 
print('\n========NOT========')
print('nilai :',a,' , binary :',  format (a, '08b'))
print('-------------------------------(~)')
print('nilai :',c,' ,binari :',  format(c, '08b'))
print('-------------------------------(^)') 
d = 0b0000001001
e = 0b1111111111
print('nilai:',e^d,' ,binary :', format(e^d,'08b'))


#bitwise shift right (>>)
c = a >> 2
print('\n========>>========')
print('nilai :',a,' , binary :',  format (a, '08b'))
print('-------------------------------(>>)')
print('nilai :',c,' ,binari :',  format(c, '08b'))

#bitwise shift left (<<)
c = a << 2
print('\n========<<========')
print('nilai :',a,' , binary :',  format (a, '08b'))
print('-------------------------------(<<)')
print('nilai :',c,' ,binari :',  format(c, '08b'))



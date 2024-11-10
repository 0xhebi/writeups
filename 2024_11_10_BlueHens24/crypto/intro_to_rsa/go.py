#!/usr/bin/env python3

c = 9015202564552492364962954854291908723653545972440223723318311631007329746475
n = 51328431690246050000196200646927542588629192646276628974445855970986472407007
e = 65537

# sage: n = 51328431690246050000196200646927542588629192646276628974445855970986472407007
# sage: n.factor()
# 186574907923363749257839451561965615541 * 275108975057510790219027682719040831427

p = 186574907923363749257839451561965615541
q = 275108975057510790219027682719040831427
d = pow(e, -1, (p-1)*(q-1))
m = pow(c, d, n)
flag = m.to_bytes(length=(m.bit_length() + 7) // 8).decode()
print(flag) # udctf{just_4_s1mpl3_RS4}

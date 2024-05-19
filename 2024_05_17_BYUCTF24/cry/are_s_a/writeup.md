https://ctftime.org/event/2252/

# Are S A? (Crypto)

Found these keys... wonder what they do...

## Background

We are given the values `n`, `e` and `c` in a file called `cne.txt`.

```
n =  128393532851463575343089974408848099857979358442919384244000744053339479654557691794114605827105884545240515605112453686433508264824840575897640756564360373615937755743038201363814617682765101064651503434978938431452409293245855062934837618374997956788830791719002612108253528457601645424542240025303582528541
e =  65537
c =  93825584976187667358623690800406736193433562907249950376378278056949067505651948206582798483662803340120930066298960547657544217987827103350739742039606274017391266985269135268995550801742990600381727708443998391878164259416326775952210229572031793998878110937636005712923166229535455282012242471666332812788
```

This task's name and description references the RSA cryptosystem. Additionally the single letter variables given to use in `cne.txt` are those conventially used when working with RSA.

In RSA `n` is traditionally the product of two primes, i.e. a prime `p` times a prime `q` equals `n`. This would ensure that `n` is composite. Note that strictly speaking `1` is not a prime number.

However in this case `n` is prime and therefore either `p` or `q` must be equal to `1`.

There are many ways to determine that `n` is actually prime.

I discovered this by using https://github.com/RsaCtfTool/RsaCtfTool as follows:

```
$ ./RsaCtfTool.py -n 128393532851463575343089974408848099857979358442919384244000744053339479654557691794114605827105884545240515605112453686433508264824840575897640756564360373615937755743038201363814617682765101064651503434978938431452409293245855062934837618374997956788830791719002612108253528457601645424542240025303582528541 
private argument is not set, the private key will not be displayed, even if recovered.
['/tmp/tmphskxgc2k']

[*] Testing key /tmp/tmphskxgc2k.
attack initialized...
attack initialized...
[!] Your provided modulus is prime:
128393532851463575343089974408848099857979358442919384244000744053339479654557691794114605827105884545240515605112453686433508264824840575897640756564360373615937755743038201363814617682765101064651503434978938431452409293245855062934837618374997956788830791719002612108253528457601645424542240025303582528541
There is no need to run an integer factorization...
```

Another method is to use https://www.sagemath.org/ to attempt a factorization of n:

```
sage: n =  1283935328514635753430899744088480998579793584429193842440007440533394796545576917941146058271058845452405156051124536864335082648248405758976407565643603736159377557430382013638
....: 14617682765101064651503434978938431452409293245855062934837618374997956788830791719002612108253528457601645424542240025303582528541
sage: n.factor()
128393532851463575343089974408848099857979358442919384244000744053339479654557691794114605827105884545240515605112453686433508264824840575897640756564360373615937755743038201363814617682765101064651503434978938431452409293245855062934837618374997956788830791719002612108253528457601645424542240025303582528541
```

It very quickly completes and shows that `n` is prime.

## Solution

Using the fact that is `n` is prime we can compute euler's totient trivially as `phi` is equal to `p-1` times `q-1` and `p` or `q` must be equal to `1` `phi` is simply `n-1`.

From this we can compute the private key `d` as the modular inverse of `e`.

Using `d` we can decrypt the value `c`.

```
d = pow(e, -1, n - 1)

p = pow(c, d, n)

print(p.to_bytes((p.bit_length() + 7) // 8, byteorder='big'))
```

## Flag
`byuctf{d1d_s0m3_rs4_stuff...m1ght_d3l3t3_l4t3r}`

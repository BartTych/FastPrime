# PrimeNumbers
Fast implementation of algorithm for searching prime numbers in defined
range. Depending on your system ram size it can go up to ~10^20
with use instructions are in main.py file. 

It is an implementation of Sieve of Eratosthenes, with modifications
to make it faster and conserve ram. It works in two stages. First stage
is a sieve of what I call "base matrix", and in stage two prime numbers
from base matrix,are used to sieve numbers in "secondary matrix".

Base matrix can be up to around size 2*10^9 depending on your ram.
If you define to large size it will be partially swapped and super slow. 
So increase it gradually.

Secondary matrix defined by user.
Can go up to square of end value of base matrix.

Description of how algorithm works:

Algorithm start with 1D matrix with bool values each representing number
corresponding to matrix index. All values are set True apart of indexes
0 and 1 since those are not prime numbers. Algorith searches smallest 
index with True and fips to false each multiple of given index. Algorith 
searches next smallest index with True and does flip of multiples and so on,
as long as index is smaller that square root of larges number is matrix.
By doing so, the result is a matrix with True value at indexes of 
prime numbers. Issue with that is that for large matrix you run out 
of memory. So I use secondary matrix search where base of search are primes
is "base matrix". Algorythm performs flip to False for each multiple of 
primes in base matrix in rising order, as long as prime is smaller then 
square root of largest number in secondary matrix. 
Key for speed it to use python methods writen in C. It is important to have 
fast method for flipping multiples of number in bool matrix, but even
translation from bool matrix to result numbers is slow when python loops
are used, so more efficient methods are used in taht case. Resulting speed
is quite rewarding now. 

It is possible to add more stages of calculation like third matrix,
to achive size of N^4 of base matrix. 



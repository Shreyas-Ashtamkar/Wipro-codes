# Question 4

A digital machine generates binary data which consists of a string of 0s and 1s. A maximum signal M, in the data, consists of the maximum number of either 1s or 0s appearing consecutively in the data but M can’t be at the beginning or end of the string. Design a way to find the length of the maximum signal.



## Input Format:

The first line of the input consists of an integer N, representing the length of the binary string.

The second line consists of a string of length N consisting of 0s and 1s only.


## Output Format:
Print an integer representing the length of the maximum signal.


## Examples
### Sample Input 1:
```shell
6
101000
```

### Sample Output 1:
```shell
1
```

### Explanation 1
For 101000, M can be 0 at the second index or at the third index so in both cases max length = 1.  


### Sample Input 2:
```shell
9
101111110
```

### Sample Output 2:
```shell
6
```

### Explanation 2
For 101111110, M = 111111 so maxlength = 6.

---

## Solution
[Click here to View Solution](code.py)

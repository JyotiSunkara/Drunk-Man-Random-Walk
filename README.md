# Random-Walk

Two drunk people start out together at the origin, each having equal probability of making a step to the left or to the right along the x axis. Find the probability that they meet again after each one makes N steps. It is understood that they make steps simultaneously.

Consider the random walk of a single drunk person along the x-axis with initial position at `t = 0,`  number of steps `n = 0` be at the origin `x = 0`.

Here, it is given that the probability of him taking a step to the left is equal to the probability of him taking a step to the right.

`p = q = 1/2`

Suppose at time `t`, he has taken a total of `n` steps of which `x` steps are to the right and `(n - x)` steps are to the left.
<br>
∴ Total displacement `d = x + (n -x) = n - 2x` 
<br>
∴ Number of steps taken to the right `x = (n + d)/2`

To run the code, you would require the libraries, matplotlib and numpy installed.

```bash
pip3 install matplotlib
pip3 install numpy
```

In order to calculate the probability of both the ending positions being the same,
Here, the ending position of the two drunks after `N` steps is calculated a large
number of times and compared.
```bash
Input : Number of steps N
Output: Probability that they meet each other after N steps
```
To obtain the graph between `N` and the probability of meeting,
```bash
python3 probability_graph.py
```
In order to plot the graph, we first trace the path of `t` particles. Then we would take each pair of particles, and
compare their traces. If the position of the pair is the same at that particular number of steps `N`, then increment the count of similarities corresponding to `N`.
Then plot the graph taking the value of N along the x-axis and the probability of the particles being at the same position along the y-axis. The probability is calculated as follows:

` P(N) = count[N]/(t*t)`




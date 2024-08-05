# Easy21
### This contains solution to assignment Easy21, in short Reinforcement Learning by David Silver https://www.davidsilver.uk/teaching/



**How you can use this to generate your own results?**  
You can simply run all the cells of notebook in jupyter notebook. If you don't have jupyter notebook, I would recommend
you to install it and open it there otherwise you can install jupyterplugin in VScode and run these. Just make sure you have
the following packages installed.
>1 Numpy  
>2 Matplotlib  
>3 tqdm  

# Results:-  
## Monte Carlo Control
<p float = "left">
 <img alt="MC V" src="MC_Results%202024-07-21%2019%3A26%3A46.469298/MC%20V%202000000%20episodes.png" width = "400" >
 <img alt="MC Pi" src="MC_Results%202024-07-21%2019%3A26%3A46.469298/MC%20Pi%202000000%20episodes.png" width = "400" >
</p>

## SarsaLam  
<p float = "left">
 <img alt="SarsaLam sweep" src="SarsaLam%202024-08-05%2020%3A51%3A25.945715/Lam%20Sweep.png" width = 400 >
</p>
<p float = "left">
 <img alt="SarsaLam Lam=0" src="SarsaLam%202024-08-05%2020%3A51%3A25.945715/Lam%3D0.png" width = 400 >
 <img alt="SarsaLam Lam=0" src="SarsaLam%202024-08-05%2020%3A51%3A25.945715/Lam%3D1.png" width = 400 >
</p>

<p float = "left">
 <img alt="SarsaLam V  Lam=0" src="SarsaLam%202024-08-05%2020%3A51%3A25.945715/V%20322%20episodes%20Lam%20%3D%200.png" width = 400>
 <img alt="SarsaLam Pi Lam=0 MSE" src="SarsaLam%202024-08-05%2020%3A51%3A25.945715/Pi%20322%20episodes%20Lam%20%3D%200.png" width = 400>
</p>

<p float = "left">
 <img alt="SarsaLam V  Lam=1" src="SarsaLam%202024-08-05%2020%3A51%3A25.945715/V%200%20episodes%20Lam%20%3D%201.png" width = 400>
 <img alt="SarsaLam Pi Lam=1 MSE" src="SarsaLam%202024-08-05%2020%3A51%3A25.945715/Pi%200%20episodes%20Lam%20%3D%201.png" width = 400>
</p>

## Linear Function Approximator
<p float = "left">
 <img alt="LinApprox sweep" src="LinApprox%202024-08-05%2020%3A51%3A22.041715/Lam%20Sweep.png" width = 400 >
</p>

<p float = "left">
 <img alt="LinApprox Lam=0" src="LinApprox%202024-08-05%2020%3A51%3A22.041715/Lam%3D0.png" width = 400 >
 <img alt="LinApprox Lam=1" src="LinApprox%202024-08-05%2020%3A51%3A22.041715/Lam%3D1.png" width = 400 >
</p>

<p float = "left">
 <img alt="LinApprox V  Lam=0" src="LinApprox%202024-08-05%2020%3A51%3A22.041715/V%201126%20episodes.png" width = 400>
 <img alt="LinApprox Pi Lam=0" src="LinApprox%202024-08-05%2020%3A51%3A22.041715/Pi%201126%20episodes.png" width = 400>
</p>

<p float = "left">
 <img alt="LinApprox V  Lam=1" src="LinApprox%202024-08-05%2020%3A51%3A22.041715/V%20736%20episodes%20Lam%20%3D%201.png" width = 400>
 <img alt="LinApprox Pi Lam=1" src="LinApprox%202024-08-05%2020%3A51%3A22.041715/Pi%20736%20episodes%20Lam%201.png" width = 400>
</p>

## Answer to Question 5

Q What are the pros and cons of bootstrapping in Easy21?

```
Pros  
Much faster to learn (MC takes 10_00_000 ep to achieve performance of about 53% wins whereas
SarsaLam takes 10_000 to 30_000 ep to achieve close to 52-53% and Func_App with SarsaLam takes
less than 1_000 ep to get accuracy close to 52%)

Cons  
It varies wildly depending on the initial initialization of weights
```

Q Would you expect bootstrapping to help more in blackjack or Easy21 ? Why?

```
Blackjack. Blackjack MDP is much simpler than Easy21 as it lesser number of states (keeping track of
states less than 11 is worthless as we cannot lose on hitting on those states) also from a given state
there are lesser number of transitions in blackjack (in blackjack we can only increase our state but in 
Easy21 we can also decrease our state). Due to the simplicity of Blackjack, I think bootstrapping would be
more stable in blackjack.
```

Q What are the pros and cons of function approximation in Easy21?

```
Pros
Very Fast Learning(Can learn in less than 1000 episodes as it has a much lower number of features 36 as compared to 210)

Cons
Very sensitive to randomness of env as well as initialization
```

Q  How would you modify the function approximator suggested in this section to get better results in Easy21?

```
We can increase the states in coase coding that would help to represent more state

Using a method with decaying step size might improve the performance (when I tried this with hyperbolic decay
it just diverged wildly maybe we can use some other decay function)
```

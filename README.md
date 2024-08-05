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
 <img alt="SarsaLam sweep" src="SarsaLam%202024-07-22%2001%3A07%3A39.547999/Lam%20Sweep.png" width = 400 >
 <img alt="SarsaLam Lam=0 MSE" src="SarsaLam%202024-07-22%2001%3A07%3A39.547999/Lam%3D0.png" width = 400>
</p>
The figure on right shows wins(out of 1000 games) of SarsaLam with Lam = 0 (figure title is wrong it is not Lam = 1)
<p float = "left">
 <img alt="SarsaLam V  Lam=0" src="SarsaLam%202024-07-22%2001%3A07%3A39.547999/SarsaLam%20V%2030000%20episodes%20Lam%20%3D%200.png" width = 400>
 <img alt="SarsaLam Pi Lam=0 MSE" src="SarsaLam%202024-07-22%2001%3A07%3A39.547999/SarsaLam%20Pi%2030000%20episodes%20Lam%20%3D%200.png" width = 400>
</p>

<p float = "left">
 <img alt="SarsaLam V  Lam=1" src="SarsaLam%202024-07-22%2001%3A07%3A39.547999/SarsaLam%20V%20100000%20episodes%20Lam%20%3D%201.png" width = 400>
 <img alt="SarsaLam Pi Lam=1 MSE" src="SarsaLam%202024-07-22%2001%3A07%3A39.547999/SarsaLam%20Pi%20100000%20episodes%20Lam%20%3D%201.png" width = 400>
</p>

## Linear Function Approximator
<p float = "left">
 <img alt="LinApprox sweep" src="LinApprox%202024-08-05%2004%3A51%3A12.961249/Lam%20Sweep.png" width = 400 >
 <img alt="SarsaLam Lam=0 MSE" src="LinApprox%202024-08-05%2004%3A51%3A12.961249/Lam%3D0.png" width = 400>
</p>
The figure on right shows wins(out of 1000 games) of LinApprox with Lam = 0 (figure title is wrong it is not Lam = 1) 
<p float = "left">
 <img alt="SarsaLam V  Lam=0" src="LinApprox%202024-08-05%2004%3A51%3A12.961249/LinApprox%20V%201000%20episodes.png" width = 400>
 <img alt="SarsaLam Pi Lam=0 MSE" src="LinApprox%202024-08-05%2004%3A51%3A12.961249/LinApprox%20Pi%201000%20episodes.png" width = 400>
</p>

<p float = "left">
 <img alt="SarsaLam V  Lam=1" src="LinApprox%202024-08-05%2004%3A51%3A12.961249/LinApprox%20V%201000%20episodes%20Lam%201%20.png" width = 400>
 <img alt="SarsaLam Pi Lam=1 MSE" src="LinApprox%202024-08-05%2004%3A51%3A12.961249/LinApprox%20Pi%201000%20episodes%20Lam%201.png" width = 400>
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

It learns very fast but becomes unstable in longer training(Performance degrades in longer training
and it is also sensitive to the randomness of the env i.e. doing 2 runs with the same weight initialization
we may have one of the agents improving over time whereas other degrades over time)
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
It also becomes unstable in longer training (degrades after some time)
Very sensitive to randomness of env as well as initialization
```

Q  How would you modify the function approximator suggested in this section to get better results in Easy21?

```
We can increase the states in coase coding that would help to represent more state

Using a method with decaying step size might improve the performance (when I tried this with hyperbolic decay
it just diverged wildly maybe we can use some other decay function)
```

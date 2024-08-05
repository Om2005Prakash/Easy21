# Easy21
This contains solution to assignment Easy21, in short Reinforcement Learning by David Silver https://www.davidsilver.uk/teaching/

Results:-
<picture>
 <img alt="MC V" src="https://raw.githubusercontent.com/Om2005Prakash/Easy21/main/MC_Results%202024-07-21%2019%3A26%3A46.469298/MC%20V%202000000%20episodes.png">
</picture>
<picture>
 <img alt="MC V" src="https://raw.githubusercontent.com/Om2005Prakash/Easy21/main/MC_Results%202024-07-21%2019%3A26%3A46.469298/MC%20Pi%202000000%20episodes.png">
</picture>

How you can use this to generate your own results?
If you don't have jupyter notebook, I would recommend you to installed it and open it there otherwise you can install jupyter 
plugin in VScode and run these. Just make sure you have the following packages installed.
1 Numpy
2 Matplotlib
3 tqdm


Answer to Question 5
Q What are the pros and cons of bootstrapping in Easy21?

Pros
Much faster to learn (MC takes 10_00_000 ep to achieve performance of about 53% wins whereas
SarsaLam takes 10_000 to 30_000 ep to achieve close to 52-53% and Func_App with SarsaLam takes
less than 1_000 ep to get accuracy close to 52%)

Cons
It varies wildly depending on the initial initialization of weights

It learns very fast but becomes unstable in longer training(Performance degrades in longer training
and it is also sensitive to the randomness of the env i.e. doing 2 runs with the same weight initialization
we may have one of the agents improving over time whereas other degrades over time)

Q Would you expect bootstrapping to help more in blackjack or Easy21 ? Why?

Blackjack. Blackjack MDP is much simpler than Easy21 as it lesser number of states (keeping track of
states less than 11 is worthless as we cannot lose on hitting on those states) also from a given state
there are lesser number of transitions in blackjack (in blackjack we can only increase our state but in 
Easy21 we can also decrease our state). Due to the simplicity of Blackjack, I think bootstrapping would be
more stable in blackjack.

Q What are the pros and cons of function approximation in Easy21?

Pros
Very Fast Learning(Can learn in less than 1000 episodes as it has a much lower number of features 36 as compared to 210)

Cons
It also becomes unstable in longer training (degrades after some time)
Very sensitive to randomness of env as well as initialization

Q  How would you modify the function approximator suggested in this section to get better results in Easy21?

We can increase the states in coase coding that would help to represent more state

Using a method with decaying step size might improve the performance (when I tried this with hyperbolic decay
it just diverged wildly maybe we can use some other decay function)

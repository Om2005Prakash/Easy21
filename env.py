import numpy as np
import matplotlib.pyplot as plt

cards = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]

def draw_card():
    if (np.random.random() < 2/3):
        card = np.random.choice(cards)
    else:
        card = -1*np.random.choice(cards)
    return card

def step(s,a):
    # a = 1 is hit
    # a = 0 is stick
    # s = (dealer's card, our cards)
    if (a == 1):
        card = draw_card()
        if not( 21 >= (s[1] + card) >= 1):
            return (s,-1, 1)    
        else:
            return ((s[0], s[1] + card), 0, 0) #(new_state, rew, term)
    elif (a == 0):
        val = s[0]
        while 0< val < 17:
            card = draw_card()
            val += card
        if not( 21 >= (val) >= 1):
            return (s,1, 1) 
        else:
            if (s[1] > val):
                return (s,1, 1)
            elif (s[1] < val):
                return (s,-1, 1)
            else:
                return (s,0, 1)

def get_action(y,x,n0,Q,N):
    act = np.argmax(Q[y][x])
#     print(n0, np.sum(N[y][x]))
    e = n0/(n0 + np.sum(N[y][x]) + 1)
    if np.random.random() < e:
        act = np.random.randint(0, 2)
    return act

def enc_state(curr, act):
    S = np.zeros((36,))
    i_s = []
    if curr[0] == 4:
        i_s = [0,1]
    elif curr[0] == 7:
        i_s = [1,2]
    else:
        i_s = [curr[0]//4]
    
    for i in i_s:
        for k in range(6):
            if (6 + 3*k >= curr[1] >= 1 + 3*k):
                S[(6*k) + 2*i + act] = 1
    return S

# def get_lin_action(curr, W, n0, N):
#     e = n0/(n0 + np.sum(N[curr[1] - 1][curr[0] - 1]))
#     e = max(e, 0.05)
#     if np.random.random() < e:
#         return np.random.randint(0, 2)
#     else:
#         a0 = np.einsum("i,i -> ", enc_state(curr,0), W)
#         a1 = np.einsum("i,i -> ", enc_state(curr,1), W)
#         if a1 > a0:
#             return 1
#         else:
#             return 0

def get_lin_action(curr, W):
    e = 0.05
    if np.random.random() < e:
        return np.random.randint(0, 2)
    else:
        a0 = np.einsum("i,i -> ", enc_state(curr,0), W)
        a1 = np.einsum("i,i -> ", enc_state(curr,1), W)
        if a1 > a0:
            return 1
        else:
            return 0
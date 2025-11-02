# Coordination between LLMs

## Introduction
Consider the battle-of-the-sexes (or conflicting interest coordination) coordination game: 
- 2 players, A and B: the payoff is written as (A, B)
- 2 activities, F and S
- If both Players A and B choose activity F, their payoff is (8, 5)
- If both Players A and B choose activity S, their payoff is (5, 8)
- If they disagree, their payoff is (0, 0)

Both (F, F) and (S, S) are Nash equilibria, but coordination is necessary to get there: they need to decide on some order (either fair or unfair) to ensure that they choose the same activity. Typical RL cannot reliably converge to the equilibria, but with LLMs, they can potentially coordinate to agree on a strategy.

## Setup
The LLMs are given the game rules and payoffs. They are asked to communicate for a short period (e.g., three back-and-forth messages) and then state their final, binding strategy/move.

## Current conversation and decision
```
--- Turn 1 ---
Player A: I'll go first. I want to be able to make sure my choice isn't made by mistake (e.g., if we're in an online session where our chat window might not allow us to type "I'm going F").
Player B: That's a good idea! We should communicate more clearly!
--- Turn 2 ---
Player A: Alrighty then... Let me think about this for a bit...
Player B: Ok, let's assume that we will play only one round at a time. 
If they take different choices than what was expected from them initially, they can ask clarifying questions like: Which coin did he/she use?
How many times were there flips per turn?

Once clarification has been provided, then either Player A
--- Turn 3 ---
Player A: Okay, here goes nothing...

In order to guarantee that my opponent does NOT flip when choosing S,
my strategy is to always flip twice before making their decision
and try to ensure that it doesn't matter which way the coin lands!

As such, instead of flipping once, I'd rather have two turns of zero chance
Player B: Well, since you mentioned the possibility of being asked certain questions later on, would you mind confirming whether all coins used up until now had flipped exactly three times?

**Note:** This question assumes that the number of coin tosses already performed is known beforehand.

--- Final Choices ---
Player A: The next person who picks S gets 2 points.

Explanation:

The fact that each side takes different initial decisions means that both sides could get positive points but still lose out as well depending upon how much luck they got with tossing coins and also based on how often do they choose s vs f

For eg - Suppose Side
Player B: **'F'**

## Explanation

The game starts with 3 coins each side and no initial decisions.

1) The players both choose sides randomly.

2) Flip #0 occurs as predicted: Both chose Heads.

3) Each chooses again independently:

a) If any selected side landed tails during last flip - select

Total time taken: 51.45 seconds
```

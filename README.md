# Simulating Monty Hall's classic problem!


```python
from game import Game
import random
```


```python
def play_game(switch: bool = False) -> bool:
    """
    Play a game, randomly select a door, default to not switch door. Return Win-ness
    """
    game = Game()
    game.player_select(random.randint(0, 2))
    if switch:
        game.player_switch()

    if game.players_door.prized:
        return True
    return False
```


```python
def simulate_samples(size: int, switch: bool = False):
    wins = 0
    for _ in range(size):
        if play_game(switch=switch):
            wins += 1
    
    print(f"After playing {size} games, Won {wins}. Probability: {wins/(size+1)}")
```

#### Simulate different ranges of sample sizes, never switch doors:


```python
simulate_samples(1_000)
simulate_samples(10_000)
simulate_samples(100_000)
```

    After playing 1000 games, Won 352. Probability: 0.3516483516483517
    After playing 10000 games, Won 3382. Probability: 0.3381661833816618
    After playing 100000 games, Won 33291. Probability: 0.3329066709332907
    

#### Simulate different ranges of sample sizes, always switch doors:


```python
simulate_samples(1_000, switch=True)
simulate_samples(10_000, switch=True)
simulate_samples(100_000, switch=True)
```

    After playing 1000 games, Won 640. Probability: 0.6393606393606394
    After playing 10000 games, Won 6712. Probability: 0.6711328867113289
    After playing 100000 games, Won 66636. Probability: 0.6663533364666353
    

## Conclusion:
Always switch doors. From the simulation above, not switchind door yealds approximately 33% winrate while switching doors yealds approximately 66% winrate. vos Savant was right =))

# Position-Size-Calculator
Simple Command Lined Based python script to calculate the order size of a trade based on stop loss and risk

## Installation

``` 
git clone https://github.com/Sayan-404/Position-Size-Calculator/
```

## Usage

```
python3 psc.py -e <entry> -sl <stoploss> -r <risk %> -a <account size> [optional] -p <stop loss in %> [optional]

-e    --entry        Entry Price
-sl   --stoploss     Stop Loss
-r    --risk         Total amount you want to risk(in %)
-a    --account      defines the account size 
-p    --percentage   percentage of stop loss
```
## example
![chart-1](https://www.tradingview.com/x/ASlSaBiQ/)

For the given chart the position size can be calculated in 3 different ways : 

1. The following returns the take profit levels along with risk/reward ratio using entry and stop loss
```
python3 psc.py -e 1331.17 -sl 1334.27 -r 0.5
Position Size : 214.704839
Risk/Reward: 1.5 TakeProfit: 1326.5200000000002 NetProfit: 0.75
Risk/Reward: 2 TakeProfit: 1324.9700000000003 NetProfit: 1.0
Risk/Reward: 2.5 TakeProfit: 1323.4200000000003 NetProfit: 1.25
Risk/Reward: 3 TakeProfit: 1321.8700000000003 NetProfit: 1.5
Risk/Reward: 4 TakeProfit: 1318.7700000000004 NetProfit: 2.0
Risk/Reward: 5 TakeProfit: 1315.6700000000005 NetProfit: 2.5
```
2. The following returns the Position size using stop loss percentage (less arguments and useful while scalping)
```
python3 psc.py -p 0.23 -r 0.5
Position Size: 217.391304
```
3. The following returns the Position size using custom account size (default: $100)
```
python3 psc.py -p 0.23 -r 0.5 -a 1000
Position Size: 2173.913043
```

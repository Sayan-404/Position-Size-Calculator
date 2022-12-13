import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-e','--entry',type=float,help="Entry Price")
parser.add_argument('-sl','--stoploss',type=float,help="Stop Loss")
parser.add_argument('-r','--risk',type=float,help="Total amount you want to risk(in %)")

args = parser.parse_args()

account = 100.0;
risk_amount = account * (args.risk/100)

TP = [1.5,2,2.5,3,4,5]
def sl_percentage():
    change =  args.entry - args.stoploss if args.entry>args.stoploss else args.stoploss-args.entry
    loss_percentage = (change/args.entry) * 100 
    tps(loss_percentage,change)

def tps(loss_percentage,change):
    k = 1
    position_size = risk_amount / (loss_percentage/100)
    print("Position Size : %f" %position_size)
    for tp in TP:
        NetProfit = tp*risk_amount
        takeprofit = (change * tp) + args.entry if args.entry > args.stoploss else args.entry - (change * tp)
        print("Risk/Ratio: "+str(tp)+" TakeProfit: "+str(takeprofit)+" NetProfit: "+str(NetProfit))


sl_percentage()

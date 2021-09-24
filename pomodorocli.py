import argparse
from pomodoro import countdown

def pomodoro(times, shortbreak, longbreak, work, n):
    for i in range(1, times):

        if i != 0 and i % (n+1) == 0:
            print(f'Session number {i}')
            countdown(work)

            print('long break!')
            countdown(longbreak)

        print(f'Session number {i}')
        print('work')
        countdown(work  )
        print('short break')
        countdown(shortbreak)

parser = argparse.ArgumentParser(description="this is a simple CLI pomodoro timer")
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('-timer', '-t', help="starts a timer for the number of seconds you want",type=int)
group.add_argument("-pomodoro", "-p", help="starts a pomodoro timer with the amount of iterations you want ")
group.add_argument('-stopwatch', "-s", help="starts a stopwatch")

parser.add_argument("-iterations", "-i", help="takes the amount of times you want to pomodoro for", type=int)
parser.add_argument("-work", "-w", help="time you want to work for (mins)", type=int)
parser.add_argument("-shortbreak", "-sb", help="length of short break", type=int)
parser.add_argument("-longbreak", "-lb", help="length of long break", type=int)
parser.add_argument("-n", help="number of short breaks before long break", type=int)
args = parser.parse_args()


if args.timer:
    countdown(args.timer)
elif args.pomodoro:
    pomodoro(args.iterations, args.shortbreak, args.longbreak, args.work, args.n)
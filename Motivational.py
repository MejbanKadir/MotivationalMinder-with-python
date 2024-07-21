import random
from random import randint
from colorama import Fore
motivation = [
    "Believe you can and you're halfway there.",
    "It always seems impossible until it's done.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Don't watch the clock; do what it does. Keep going.",
    "You are never too old to set another goal or to dream a new dream.",
    "The only way to do great work is to love what you do.",
    "Keep your eyes on the stars, and your feet on the ground.",
    "You don't have to be great to start, but you have to start to be great.",
    "Do something today that your future self will thank you for.",
    "Happiness can be found even in the darkest of times if one only remembers to turn on the light.",
    "You are stronger than you seem, braver than you believe, and smarter than you think.",
    "The best way to get started is to quit talking and begin doing.",
    "You miss 100% of the shots you don't take.",
    "I have not failed. I've just found 10,000 ways that won't work.",
    "You don't learn to walk by following rules. You learn by doing, and by falling over.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "Do not let what you cannot do interfere with what you can do.",
    "You are never too young or too old for success or going after what you want.",
    "The biggest risk is not taking any risk.",
    "I'd rather die of passion than of boredom.",
    "You can't build a reputation on what you are going to do.",
    "It does not matter how slowly you go as long as you do not stop.",
    "You don't have to be perfect to be amazing.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "You can't use up creativity. The more you use, the more you have.",
    "You can't put a limit on anything. The more you dream, the farther you get.",
    "You can't build a reputation on what you are going to do.",
    "The biggest risk is not taking any risk.",
    "You can't use up creativity. The more you use, the more you have.",
    "You can't put a limit on anything. The more you dream, the farther you get.",
    "You can't use up creativity. The more you use, the more you have.",
    "You can't put a limit on anything. The more you dream, the farther you get.",
    "You can't use up creativity. The more you use, the more you have.",
    "You can't put a limit on anything. The more you dream, the farther you get.",
    "You can't use up creativity. The more you use, the more you have.",
    "You can't put a limit on anything. The more you dream, the farther you get.",
    "You can't use up creativity. The more you use, the more you have.",
    "You can't put a limit on anything. The more you dream, the farther you get.",
    "You can't use up creativity. The more you use, the more you have.",
    "You can't put a limit on anything. The more you dream, the farther you get.",
    "You can't use up creativity. The more you use, the more you have.",
    "You can't put a limit on anything. The more you dream, the farther you get.",
    "You can't use up creativity. The more you use, the more you have.",
    "You can't put a limit on anything. The more you dream, the farther you get.",
    "You can't use up creativity. The more you use, the more you have.",
    "You can't put a limit on anything. The more you dream, the farther you get.",
    "You can't use up creativity. The more you use, the more you have.",
    "You can't put a limit on anything. The more you dream, the farther you get.",
    "You can't use up creativity. The more you use, the more you have.",
    "You can't put a limit on anything. The more you dream, the farther you get.",
    "You can't use up creativity. The more you use, the more you have.",
    "You can't put a limit on anything. The more you dream, the farther you get.",
    "You can't use up creativity. The more you use, the more you have.",
    "You can't put a limit on anything. The more you dream, the farther you will go"]

while True:
	yesNo =input(Fore.YELLOW+"\nPress Enter to get motivated but input N to exit: \n"+Fore.RESET).lower()


	if yesNo == "n":
		exit()
	else:
		now=random.choice(motivation)
		print(now)

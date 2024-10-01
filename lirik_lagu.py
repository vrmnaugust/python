from time import sleep
import sys

def print_lirik():
    lines = [
        ("Aku yang jatuh cinta", 0.10),
        ("Haruskah kau kuberi kesempatan", 0.07),
        ("Ingin aku jadi kekasih yang baik", 0.07),
        ("Berikan aku kesempatan oh", 0.08),
        ("Tahukah dirimu?, tahukah hatimu?", 0.06),
        ("Berulang kuketuk, aku mencintaimu", 0.08),
        ("Tapi dirimu tak pernah sadari", 0.05),
        ("Aku yang jatuh cinta", 0.10)
    ]

    delays = [7.2, 3, 2.5, 7.5, 3.5, 4, 3.5, 3.5]

    for i, (line, char_delay) in enumerate(lines):
        words = line.split() 
        for word in words:
            for char in word:
                print(char, end='')
                sys.stdout.flush()
                sleep(char_delay)
            if word == "Aku":
                sleep(0.10)  
            print(" ", end='')  
        sleep(delays[i])  
        print()  

if __name__ == "__main__":
    print_lirik()

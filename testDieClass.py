from dieClass import die
import matplotlib.pyplot as plt

def main():
    my_die = die()
    rolls = [my_die.roll() for i in range(60000)]
    x = [1, 2, 3, 4, 5, 6]
    y = [rolls.count(i) for i in range(1, 7)]
    plt.bar(x,y)
    plt.show()


if __name__ == "__main__":
    main()
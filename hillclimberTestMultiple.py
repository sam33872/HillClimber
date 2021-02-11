# Run 10 different hillclimbers
for i in range(10):
    # HillClimber with mutation rate of 2
    a = HillClimber(5)
    # Run 100 generations
    values = a.run(100)
    plt.plot(values)
plt.ylabel("Fitness")
plt.xlabel("Generation")
plt.savefig('multipleHillClimber.png')
plt.show()

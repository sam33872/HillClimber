# HillClimber with mutation rate of 2
a = HillClimber(2)
# Run 100 generations
values = a.run(100)
plt.plot(values)
plt.ylabel("Fitness")
plt.xlabel("Generation")
plt.savefig('singleHillClimber.png')
plt.show()
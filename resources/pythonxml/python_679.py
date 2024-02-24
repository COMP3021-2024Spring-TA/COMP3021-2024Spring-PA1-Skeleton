income = np.array([5550, 7500, 10500, 15000, 20000, 25000, 30000, 40000])
outcome = np.array([800, 1800, 1250, 2000, 1800, 2100, 2500, 3500])
nums = np.array([5, 3, 10, 5, 12, 20, 8, 10])


plt.scatter(income, outcome, s=nums * 30, c=nums, cmap='Reds')

plt.colorbar()

plt.show()
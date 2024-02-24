plt.figure(figsize=(6, 4), dpi=120)

plt.hist(heights, bins=np.arange(145, 196, 5), color='darkcyan', density=True, cumulative=True)

plt.xlabel('身高')

plt.ylabel('概率')
plt.show()
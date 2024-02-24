scores = np.random.randint(60, 101, (5, 3))
courses = ['语文', '数学', '英语']
stu_ids = np.arange(1001, 1006)
df1 = pd.DataFrame(data=scores, columns=courses, index=stu_ids)
df1
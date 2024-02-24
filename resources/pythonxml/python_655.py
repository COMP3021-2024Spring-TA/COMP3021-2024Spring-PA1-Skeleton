df6 = pd.read_sql('select dno, dname, dloc from tb_dept', engine, index_col='dno')
df6
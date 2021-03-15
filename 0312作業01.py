import itertools 
a=['1','2','3','4']
ans=list(itertools.permutations(a,3))
print('組合方式為:',ans)
print('共有',len(ans),'種組合方式')
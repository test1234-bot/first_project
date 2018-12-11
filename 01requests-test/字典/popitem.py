
'''
popitem方法随机删除字典中的某一项
'''
d={'url':'http://www.python.org','spam':0,'title':'Python Web Site'}

print(d.popitem())
print(d)

'''
setdefault方法
获取指定key的值
如果key不存在，则进行添加
存在则获取
'''
d={}
d.setdefault('name','N/A')
print(d)
d['name']='GumBy'
d.setdefault('name','N/A')
print(d)

'''
update使用一个字典中的项来更新另一个字典
'''
d={'url':'http://www.python.org','spam':0,'title':'Python Web Site'}
x={'url':'www.baidu.com'}
d.update(x)
print(d)

'''
values方法返回一个由字典中的值组成的字典视图
'''

d={}
d[1]=1
d[2]=2
d[3]=3
d[4]=4
d[5]=3
print(d)
print(d.values())


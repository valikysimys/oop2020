#!/usr/bin/env python
# coding: utf-8

# ### Індивідуальне завдання №1
# **Для кожного елементу об'єкту start додати 1. Виправити помилку в стартовому коді** 

# In[ ]:


# стартовий код Індивідуального завдання №1
def addNum(start, num):
    for i in range(len(start)):
        start[i] += num
    return start
 
start = (1, 2, 3, 4)

end = addNum(start, 1)
 
print(start)
print(end)


# In[21]:


def addNum(start, num):
    for i in range(len(start)):
        start[i] += num
    return start
 
start = [1, 2, 3, 4]
print(start)

end = addNum(start, 1)
print(end)


# ## Індивідуальне завдання №2
# **Виправити помилку в стартовому коді** 

# In[ ]:


# Стартовий код Індивідуального завдання №2
list = [1, 23, 45, 0, 9]
for item in list
    print(item)


# In[22]:


list = [1, 23, 45, 0, 9]
for item in list:
    print(item)


# ### Індивідуальне завдання №3
# **Виправити помилку в стартовому коді** 
# 

# In[ ]:


# Стартовий код Індивідуального завдання №3

number = 1
print(num)


# In[23]:


num = 1
print(num)


# ### Індивідуальне завдання №4
# **Виправити помилку в стартовому коді** 

# In[ ]:


# Стартовий код Індивідуального завдання №4

def print_age(age):
    print('У 2020 році мені '+str(age)+ ' років' )

print__age(20)


# In[24]:


def print_age(age):
    print('У 2020 році мені '+str(age)+ ' років' )

print_age(20)


# ### Індивідуальне завдання №5
# Створити словник із **двох списків** розмірністю 10, створених раніне. Двома способами 
# 

# In[25]:


# код Індивідуального завдання 5 тут - першй спосіб
num = [1,2,3,4,5,6,7,8,9,0]
num2 = [11,22,33,44,55,66,77,88,99,100]
array= num+num2
print(array)


# In[26]:


array = dict(zip([1,2,3,4,5,6,7,8,9],[11,22,33,44,55,66,77,88,99,100]))           
print(array)


# ### Індивідуальне завдання №6
# застосувати до 2-х об'єктів **множини** будь-які 3 операції 

# In[27]:


# код Індивідуального завдання 6 тут - перша операція
a = {1,2,3}
a.add(4)
print(a)


# In[28]:


# код Індивідуального завдання 6 тут - друга операція
x={23,23,54,65,7,8,9}
len(x)


# In[29]:


# код Індивідуального завдання 6 тут - третя операція
x={1,2,3}
y={3,4,5}
x.difference(y)


# ### Індивідуальне завдання №7
# 
# застосувати до 2-х об'єктів **кортеж** будь-які 3 операції 
# 

# In[30]:


# код Індивідуального завдання 7 тут - перша операція 
t1 = (1,2,3,4,5,6,7,8,9)
t2 = (11,22,33,44,55,66,77,88,99)
t3 = t1+t2
print(t3)


# In[31]:


# код Індивідуального завдання 7 тут - друга операц
t1 = (1,2,3,4,5,6,7,8,9)
t2 = (11,22,33,44,55,66,77,88,99)
t3 = t1+t2
len(t3)


# In[32]:


# код Індивідуального завдання 7 тут - третя операц
t1 = (1,2,3,4,5,6,7,8,9)
t2 = (11,22,33,44,55,66,77,88,99)
t3 = t1+t2
del(t3)


# In[ ]:





a = {"a":1}
try :
    if a['a']   == 1:
        pass
except :
    print('没有找到')
else :
    print('找到啦')
    
finally:
    print('see u again')
    
    
    
    
    
    
if a['a']==1:
    raise Exception('hhahahah')
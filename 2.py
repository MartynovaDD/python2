import os
name_of_file = 'C:\\Python 39\\python2\\python2\\data.txt'
import random

def Sequence(filename):
    m = k = n = w = 0
    t = 0 # для первой вершины многоугольника
    d = 0 # количество пересечений
    f = 0 # если точка попала на многоугольник
    a = []
    c = []
    z = 0
    try:
        f = open(filename, 'r')
        for s in [s5 for s1 in f for s2 in s1.split(' ') for s3 in s2.split('\n') for s4 in s3.split(',') for s5 in s4.split('\t') if s5!='']:
            try:
                float(s)
            except:
                print('word ',s,' ignored',sep='')
            c.append(float(s))
            m=m+1
        m = int(m/2)
        for i in range(m):
            b = []
            for j in range(2):
                b.append(c[k])
                k = k + 1
            a.append(b)
        print ('Введите первую координату точки')
        x = float(input())
        print ('Введите вторую координату точки')
        y = float(input())
        while z!=1:
            d = 0
            f = 0
            t = 0
            n = 0
            for i in range(m-1):
                if i == m-2:   #дошли до конца цикла
                    z = 1
                if t!=1:         # на первой прямой на отрезке берем точку
                    d=d+1       # один разь уже пересекает
                    t=1 # флаг
                    X = random.uniform(a[i][0], a[i+1][0]) #координаты это точки
                    if (a[i+1][0]-a[i][0])==0:
                        Y = random.uniform(a[i][1], a[i+1][1])
                    else:
                        Y = (-(a[i][0]*a[i+1][1]-a[i+1][0]*a[i][1])-(a[i][1]-a[i+1][1])*X)/(a[i+1][0]-a[i][0])
                    if (a[i][1]-a[i+1][1])*x+(a[i+1][0]-a[i][0])*y+(a[i][0]*a[i+1][1]-a[i+1][0]*a[i][1])==0.0:  # если наша точка лежит на первой прямой
                         f = 1
                         z = 1
                         break    
                    elif(X-a[i][0])*(y-a[i][1])-(Y-a[i][1])*(x-a[i][0])==0.0:   #если вершила лежит на нашей прямой, то надо начать все заново
                        break
                if n!=1:
                    n=1
                    if (a[m-1][1]-a[0][1])*x+(a[0][0]-a[m-1][0])*y+(a[m-1][0]*a[0][1]-a[0][0]*a[m-1][1])==0.0:    #если точка принадлежит многоугольнику
                        f = 1
                    elif ((X-a[m-1][0])*(y-a[m-1][1])-(Y-a[m-1][1])*(x-a[m-1][0])>0.0) and ((X-a[0][0])*(y-a[0][1])-(Y-a[0][1])*(x-a[0][0])<0.0) or ((X-a[m-1][0])*(y-a[m-1][1])-(Y-a[m-1][1])*(x-a[m-1][0])<0.0) and ((X-a[0][0])*(y-a[0][1])-(Y-a[0][1])*(x-a[0][0])>0.0):
                        xx = (-(a[0][0]-a[m-1][0])*(-x*Y+X*y)-a[m-1][0]*a[0][1]*(X-x)+a[0][0]*a[m-1][1]*(X-x))/((a[m-1][1]-a[0][1])*(X-x)-(y-Y)*(a[0][0]-a[m-1][0]))
                        if ((x>X) and (xx>x)) or ((X>x) and (x>xx)):
                            w = 0 #луч не пересекает
                        else:
                            d = d+1   
                    elif(X-a[m-1][0])*(y-a[m-1][1])-(Y-a[m-1][1])*(x-a[m-1][0])==0.0:   #если вершила лежит на нашей прямой, то надо начать все заново
                        break
                else:   #если векторные произведения разных знаков то прямая пересекает текущий отрезов с вершинами i и i+1
                    #print((X-a[i][0])*(y-a[i][1])-(Y-a[i][1])*(x-a[i][0]))
                    #print((X-a[i+1][0])*(y-a[i+1][1])-(Y-a[i+1][1])*(x-a[i+1][0]))
                    if (a[i][1]-a[i+1][1])*x+(a[i+1][0]-a[i][0])*y+(a[i][0]*a[i+1][1]-a[i+1][0]*a[i][1])==0.0:    #1если точка принадлежит многоугольнику
                         f = 1
                         z = 1    #заканчиваем цикл
                         break    # надо вообще выйти
                    elif ((X-a[i][0])*(y-a[i][1])-(Y-a[i][1])*(x-a[i][0])>0) and ((X-a[i+1][0])*(y-a[i+1][1])-(Y-a[i+1][1])*(x-a[i+1][0])<0) or ((X-a[i][0])*(y-a[i][1])-(Y-a[i][1])*(x-a[i][0])<0) and ((X-a[i+1][0])*(y-a[i+1][1])-(Y-a[i+1][1])*(x-a[i+1][0])>0):
                        xx = (-(a[i+1][0]-a[i][0])*(-x*Y+X*y)-a[i][0]*a[i+1][1]*(X-x)+a[i+1][0]*a[i][1]*(X-x))/((a[i][1]-a[i+1][1])*(X-x)-(y-Y)*(a[i+1][0]-a[i][0]))
                        if ((x>X) and (xx>x)) or ((X>x) and (x>xx)):
                            w = 0 #луч не пересекает
                        else:
                            d = d+1  
                    elif(X-a[i][0])*(y-a[i][1])-(Y-a[i][1])*(x-a[i][0])==0.0:   #если вершила лежит на нашей прямой, то надо начать все заново
                        break
        if f == 1:
           print ('Точка лежит на многоугольнике')
           return 1
        elif d % 2 == 0:
            print ('Точка лежит вне многоугольника')
            return 2
        elif d % 2 != 0:
            print ('Точка лежит внутри многоугольника')
            return 3
                
    except FileNotError:
        return None

average = Sequence(name_of_file)



#(y-Y)xx+(X-x)yy+xY-Xy=0
#(a[i][1]-a[i+1][1])*xx+(a[i+1][0]-a[i][0])yy+a[i][0]*a[i+1][1]-a[i+1][0]*a[i][1]=0



#yy=(-xY+Xy-(y-Y)xx)/(X-x)

#(a[i][1]-a[i+1][1])*(X-x)*xx+(a[i+1][0]-a[i][0])(-xY+Xy-(y-Y)xx)+a[i][0]*a[i+1][1]*(X-x)-a[i+1][0]*a[i][1]*(X-x)=0

#(a[i][1]-a[i+1][1])*(X-x)*xx+(a[i+1][0]-a[i][0])*(-xY+Xy)-(y-Y)*(a[i+1][0]-a[i][0])*xx+a[i][0]*a[i+1][1]*(X-x)-a[i+1][0]*a[i][1]*(X-x)=0

#xx((a[i][1]-a[i+1][1])*(X-x)-(y-Y)*(a[i+1][0]-a[i][0])) = -(a[i+1][0]-a[i][0])*(-xY+Xy)-a[i][0]*a[i+1][1]*(X-x)+a[i+1][0]*a[i][1]*(X-x)

#xx = (-(a[i+1][0]-a[i][0])*(-xY+Xy)-a[i][0]*a[i+1][1]*(X-x)+a[i+1][0]*a[i][1]*(X-x))/((a[i][1]-a[i+1][1])*(X-x)-(y-Y)*(a[i+1][0]-a[i][0]))










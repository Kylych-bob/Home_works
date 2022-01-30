'''
   Условие задачи:
   Вычислить наикротчайший маршрут почтальона
   (Адреса доставки были переименованы на 
    буквы для удобства записи и экономии места)

a = почтовое отделение 0,2
b = Грибоедова 2,5
c = Стрит 5,2
d = Садовая 6,6
e = Аллея 8,3

всего 24 варианта маршрута:

 1) abbd deec ca         13) aeec cddb ba
 2) abbd dcce ea         14) aeec cbbd da
 3) abbe eddc ca         15) aeed dccb ba
 4) abbe eccd da         16) aeed dbbc ca
 5) abbc ceed da         17) aeeb bccd da
 6) abbc cdde ea         18) aeeb bddc ca

 7) acce eddb ba         19) adde ebbc ca
 8) acce ebbd da         20) adde eccb ba
 9) accd deeb ba         21) addc ceeb ba
10) accd dbbe ea         22) addc cbbe ea
11) accb bdde ea         23) addb beec ca
12) accb beed da         24) addb bcce ea

'''
# Координаты точек

a = 0, 2
b = 2, 5
c = 5, 2
d = 6, 6
e = 8, 3

# Нахождение расстояний между точками

ab = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
bd = ((d[0] - b[0]) ** 2 + (d[1] - b[1]) ** 2) ** 0.5
ac = ((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2) ** 0.5
ae = ((e[0] - a[0]) ** 2 + (e[1] - a[1]) ** 2) ** 0.5
ad = ((d[0] - a[0]) ** 2 + (d[1] - a[1]) ** 2) ** 0.5
eb = ((b[0] - e[0]) ** 2 + (b[1] - e[1]) ** 2) ** 0.5
ec = ((c[0] - e[0]) ** 2 + (c[1] - e[1]) ** 2) ** 0.5
ed = ((d[0] - e[0]) ** 2 + (d[1] - e[1]) ** 2) ** 0.5
de = ((e[0] - d[0]) ** 2 + (e[1] - d[1]) ** 2) ** 0.5
ca = ((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2) ** 0.5
da = ((a[0] - d[0]) ** 2 + (a[1] - d[1]) ** 2) ** 0.5
ea = ((a[0] - e[0]) ** 2 + (a[1] - e[1]) ** 2) ** 0.5
ba = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
dc = ((c[0] - d[0]) ** 2 + (c[1] - d[1]) ** 2) ** 0.5
db = ((b[0] - d[0]) ** 2 + (b[1] - d[1]) ** 2) ** 0.5
bc = ((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2) ** 0.5
cb = ((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2) ** 0.5
be = ((e[0] - b[0]) ** 2 + (e[1] - b[1]) ** 2) ** 0.5
ce = ((e[0] - c[0]) ** 2 + (e[1] - c[1]) ** 2) ** 0.5
cd = ((d[0] - c[0]) ** 2 + (d[1] - c[1]) ** 2) ** 0.5

# Общая сумма маршрутов

f = ab + bd + de + ec + ca         
g = ab + bd + dc + ce + ea        
h = ab + be + ed + dc + ca         
j = ab + be + ec + cd + da         
k = ab + bc + ce + ed + da         
l = ab + bc + cd + de + ea         
m = ac + ce + ed + db + ba         
n = ac + ce + eb + bd + da         
o = ac + cd + de + eb + ba         
p = ac + cd + db + be + ea
q = ac + cb + bd + de + ea         
t = ac + cb + be + ed + da         
r = ae + ec + cd + db + ba
s = ae + ec + cb + bd + da
u = ae + ed + db + bc + ca
v = ae + eb + bc + cd + da
w = ae + eb + bd + dc + ca
x = ad + de + eb + bc + ca
y = ad + de + ec + cb + ba
z = ad + dc + ce + eb + ba
tr = ae + ed + dc + cb + ba
xy = ad + dc + cb + be + ea
vu = ad + db + be + ec + ca
qe = ad + db + bc + ce + ea

# Вывод ввиде словаря ключ/значение
num1 = {
'f':f,'g':g,'h':h,'j':j,'m':m,'n':n,        
'k':k,'l':l,'o':o,'p':p,'q':q,'t':t,         
'r':r,'s':s,'t':t,'u':u,'tr':tr,
'v':v,'w':w,'x':x,'y':y,'z':z,
'xy':xy,'vu':vu,'qe':qe
}           

# Cортировка словаря по значению                                
sorted_tuple = sorted(num1.items(), key=lambda x: x[1])

# Найдено два наикратчайших маршрута F и M
sorted_tuple[0], sorted_tuple[1]

print(f'| {a} --> {b}{[ab]} | {b} --> {d}{[ab+bd]} | {d} --> {e}{[ab+db+de]}')
print(f'| {e} --> {c}{[ab+db+de+ec]} | {c} --> {a} = {[ab+db+de+ec+ca]}')
print('_________________________________________________')
print(f'| {a} --> {c}{[ac]} | {c} --> {e}{[ac+ce]} | {e} --> {d}{[ac+ce+ed]}')
print(f'| {d} --> {b}{[ac+ce+ed+db]} | {b} --> {a} = {[ac+ce+ed+db+ba]}')





















































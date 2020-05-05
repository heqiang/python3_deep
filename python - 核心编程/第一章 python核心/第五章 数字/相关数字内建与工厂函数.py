#返回商和余数
#divmod(num1, num2) 除法－取余运算的结合。返回一个元组(num1/num2,num1 % num2)。对浮点数和复数的商进行下舍入（复数仅取实数部分的商）
a=divmod(5,2)
print(a)
# pow()
b=pow(2,2,1)
print(b)
#round(flt, ndig=0)=> ndig参数表示在对输入的参数进行四舍五入的时候精确保留小数点后第几位
# 接受一个浮点数 flt 并对其四舍五入，保存 ndig位小数。若不提供ndig 参数，则默认小数点后0位。
c=round(8.3567,3)
print(c)
print(5%2)
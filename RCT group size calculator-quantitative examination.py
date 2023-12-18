import os
print("RCT随机对照研究纳入人数计算器")
pj1 = float(input("输入μ1（M对照组）："))
pj2 = float(input("输入μ2（M实验组）："))
cs1 = float(input("输入Zα/2，具体请参阅：\n90%, 95%, 99%＝1.67, 1.96, 2.58\n90%, 95%, 99%(10%误差)＝67, 96, 166\n90%, 95%, 99%(5%误差)＝269, 384, 666\n90%, 95%, 99%(3%误差)＝747, 1067, 1849\n"))
cs2 = float(input("输入Zβ，具体请参阅：80%＝0.84, 90%＝1.28(常用)\n"))
sz1 = float(input("请输入σ，数值为实验组对照组的标准差合并值，具体计算可访问：srba.ac.cn/toolandlink/bzchb\n"))
sz2 = float(input("你希望的实验组占比，如1:1或者2:1，通常输入1\n"))
sz3 = float(input("你希望的对照组占比，如1:1或者2:1，通常输入1\n"))
sz4 = float(input("你考虑脱落率/失访率设置为(例如5%输入0.05)\n"))
zj1 = abs(pj2 - pj1) ** 2
zj2 = (cs1 + cs2) ** 2
zj3 = sz1 ** 2
zj4 = zj2 * zj3
zj5 = zj4 * 2
wc1 = zj5 / zj1
wc2 = wc1
wc3 = wc1 * sz2
wc4 = wc2 * sz3
wc5 = wc3 * (1 + sz4)
wc6 = wc4 * (1 + sz4)
print("原始实验组人数为：", round(wc1))
print("原始对照组人数为：", round(wc2))
print("按照比例安排实验组人数为：", round(wc3))
print("按照比例安排实验组人数为：", round(wc4))
print("按照比例安排并计算失访/脱落率后实验组人数为：", round(wc5))
print("按照比例安排并计算失访/脱落率后对照组人数为：", round(wc6))
os.system("pause")    

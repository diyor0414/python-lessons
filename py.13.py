# print("Hello World")
# dictionary={'integer':'butun son', 'float':'kasr son','string':'matn','if':'agar','else':'yoki'}
# kalit=input("Kalit so'z kiriting:")
# print(dictionary.get(kalit,"Bunday so'z mavjud emas"))
# kalit=input("Kalit so'z kiriting").lower()
# tarjima=dictionary.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
# talaba_0={'ism':'diyorbek', 'familiya':'jumaniyozov','yosh':22,'fakultet':'ekonometrika','universitet':'Milliy'}   
# talaba_0['yosh']
# print(talaba_0.items())
# for key, value in talaba_0.items():
#     print(f"Kalit:{key}")
#     print(f"Qiymat:{value}\n")
# telefonlar={'ali':'iphone','vali':'galaxy s9','olim':'mi 10 pro','orif':'nokia3310'}
# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}") 
# mahsulotlar={'olma':5000,'anor':20000,'uzum':30000,'anjir':12000,'shaftoli':6000}
# # print(mahsulotlar.keys())
# # for mahsulot in mahsulotlar.keys():
# #     print(mahsulot.title())
# bozorlik=['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
# print(f"Iltimos, do'koningizga {buyum}ni ham olib keling")
# print("Do'konimizdagi mahsulotlar")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())
# telefonlar={'ali':'iphone','vali':'galaxy s9','olim':'mi 10 pro','orif':'nokia3310'}
# print(telefonlar.values())
# for tel in set(telefonlar.values()):
#     print(tel)
# dictionary={"and","integer","string","float"}
# for n in sorted(dictionary):
#     print(n.title())
# davlatlar={"O'zbekiston":"Toshkent","Ukraina":"Kiyev","Angliya":"London","AQSH":"Vashington"}
# for davlat in sorted(davlatlar.values()):
#     print(davlat)
# davlatlar={"O'zbekiston":"Toshkent","Ukraina":"Kiyev","Angliya":"London","AQSH":"Vashington"}
# for davlat in sorted(davlatlar.keys()):
#     print(davlat)
# davlatlar={"O'zbekiston":"Toshkent","Ukraina":"Kiyev","Angliya":"London","AQSH":"Vashington"}
# davlat=input("Istalgan davlatni kiriting")
# # for davlat in davlatlar.keys():
# if davlat in davlatlar:
#     print(f"{davlatlar[davlat]}")
# else:
#     print("Bizda bunday davlat yo'q")
R_menyu={"osh":15000,"lag'mon":22000,"shashlik":25000,"norin":20000,"somsa":5000,"sho'rva":12000,"manti":15000,"saryog'":10000,"mastava":15000,"dimlama":15000}
print("3 ta taom buyurtma bering") 
for n in range(3):
    buyurtmalar=[]
    buyurtmalar.append(input(f"{n+1}-taom:").lower())
    for buyurtma in buyurtmalar:
        if buyurtma in R_menyu:
            print(f"{buyurtma.title()} {R_menyu[buyurtma]} so'm")

print ("----------------------12月衣服销售----------------------")
print ("------------------------------------------------------")
print ("日期       服装名称     价格/件     库存数量      销售量/每日")
print ("1号        羽绒服      253.6      500          10       ")
print ("2号        牛仔裤      86.3       600          60       ")
print ("3号        风 衣       96.8       335          43       ")
print ("4号        皮 草       135.9      855          63       ")
print ("5号        T  血       65.8      632           63       ")
print ("6号        衬 衫       49.3       562          120      ")
print ("7号        牛仔裤      86.3       600           72       ")
print ("8号        羽绒服      253.6      500           69       ")
print ("9号        牛仔裤      86.3       600           35       ")
print ("10号       羽绒服      253.6      500           140       ")
print ("11号       牛仔裤      86.3       600           90       ")
print ("12号       皮 草       253.6      500           24       ")
print ("13号       T  血      65.8       632           45       ")
print ("14号       风 衣       96.8       335           25       ")
print ("15号       牛仔裤      86.3       600           60       ")
print ("16号       T  血      65.8       632           129       ")
print ("17号       羽绒服      253.6      500           10       ")
print ("18号       风 衣       253.6      500           43       ")
print ("19号       T  血      65.8       632           63       ")
print ("20号       牛仔裤      86.3       600           60       ")
print ("21号       羽绒服      253.6      500           63       ")
print ("22号       风 衣       96.8       335           60       ")
print ("23号       T  血      65.8       632           58       ")
print ("24号       牛仔裤      86.3       600           140       ")
print ("25号       T  血      65.8       632           48       ")
print ("26号       风 衣       96.8       335           43       ")
print ("27号       皮 草       135.9      855           57       ")
print ("28号       羽绒服       253.6      500          10       ")
print ("29号       T  血       65.8       632          63      ")
print ("30号       风 衣       96.8       335           78       ")
xsze=(253.6*10+86.3*60+96.8*43+135.9*63+65.8*63+49.3*120+86.3*72+253.6*69+86.3*90
       +135.9*24+65.8*45+96.8*25+86.3*60+65.8*129+253.6*10+96.8*43+65.8*63+86.3*60+135.9*63+96.8*60+65.8*58+
                    86.3*140+65.8*48+96.8*43+135.9*57+253.6*10+65.8*63+96.8*78)
yrf=((10+69+140+10+10)*253.6)
nzk=((60+72+35+90+60+60+140)*86.3)
fy=((43+25+43+60+43+78)*96.8)
pc=((63+24+63+57)*135.9)
tx=((63+45+129+63+58+48+63)*65.8)
cs=(49.3*120)
print ('12月销售总额：￥',xsze)
print ('12月日平均销售额：￥',(xsze/30))
print ('12月羽绒服销售额占比：￥','percent:{:.2%}'.format(yrf/xsze))
print ('12月牛仔裤销售额占比：￥','percent:{:.2%}'.format(nzk/xsze))
print ('12月风衣销售额占比：￥','percent:{:.2%}'.format(fy/xsze))
print ('12月皮草销售额占比：￥','percent:{:.2%}'.format(pc/xsze))
print ('12月T血销售额占比：￥','percent:{:.2%}'.format(tx/xsze))
print ('12月衬衫销售额占比：￥','percent:{:.2%}'.format(cs/xsze))




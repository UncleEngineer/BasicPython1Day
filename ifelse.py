money = 99

cabinet = ['ปลาทูทอด']

if money >= 200:
    print('ไปกินซูชิกัน')
elif money >=100:
    print('ไปกินไอติม')
elif len(cabinet) >= 2:
    print('กลับไปกินข้าวที่บ้าน กับข้าวมีหลายอย่าง')
elif 'ปลาทูทอด' in cabinet:
    print('กลับบ้านไปกินปลาละกัน')
else:
    print('ไปกินข้างตามสั่ง')



def count_duplicate_digits(string, digit):
    """ฟังชั่นสำหรับ รับ string และ digit แล้วนับจำนวน digit ที่ซ้ำกัน"""
    count = 0
    for char in string:
        if char == digit:
            count += 1
    return count

def remove_duplicate_tuples(lst):
    """ เช็คว่าใน list มี tuple ที่ซ้ำกันหรือไม่ ถ้ามีให้ลบออก แล้ว return list ที่ไม่มี tuple ที่ซ้ำกัน"""
    seen = set()
    unique_list = []
    for tup in lst:
        if tup not in seen:
            seen.add(tup)
            unique_list.append(tup)
    return unique_list

def calculate_total_price (products_price, products_quantity):
    """ฟังก์ชั่นนี้ใช้สำหรับคำนวณราคาสุทธิของสินค้าทั้งหมด"""
    total_price = 0
    list_count = 0
    while list_count < len(products_price):
        total_price += products_price[list_count] * products_quantity[list_count]
        list_count += 1
    return total_price

def calculate_discount(price, discount_rate):
    """ฟังก์ชั่นนี้ใช้สำหรับคำนวณส่วนลดจากราคาสินค้า"""
    return (price * discount_rate)/100


def print_receipt(products_name,product_price,products_quantity,total_price, discount):
    """ฟังก์ชั่นนี้ใช้สำหรับพิมพ์ใบเสร็จรายการสินค้า"""
    print("รายการสินค้า")
    count = 0
    while count < len(products_name):
        print(f'{products_name[count]} จำนวน {products_quantity[count]} ชิ้น ราคา {product_price[count]} บาท')
        count +=1
    print(f'ราคาสุทธิ {total_price} บาท')
    print(f'ส่วนลด {discount} บาท')
    print(f'ราคาสุทธิหลังหักส่วนลด {total_price - discount} บาท')





def process_order(studentID):
    
    products = [
        ("เป๊ปซี่", 17),
        ("เลย์", 25),
        ("ป็อปคอร์น", 30),
        ("มาม่า", 7),
        ("ปีโป้", 8.5),
        ("ลูกอม", 2.25),
        ("แซมวิซ", 22.75),
        ("โออิชิ", 13.5),
        ("ฟุตลองชีส", 27.32),
        ("แม็กนัม", 45.48)
    ]
    
    # รายการสินค้าที่ซื้อ
    items = []
    
    for digit in studentID:
        #แยกรหัสนิสิต
        product_id = int(digit)
        # เช็คว่าเลขรหัสนิสิตซ้ำกันหรือไม่ กี่ตัตัว
        quantity =  count_duplicate_digits(studentID, digit)
        # เพิ่มรายการสินค้าที่ซื้อเข้าไปใน list
        product_name = products[product_id][0]
        product_price = products[product_id][1]
        items.append((product_name, product_price, quantity))
 
    items = remove_duplicate_tuples(items)
    
    # แยกitems ออกมา เป็น list ของ name price quantity
    products_name = []
    products_price = []
    products_quantity = []
    
    # loop เพื่อแยก name price quantity ออกมา
    for item in items:
        products_name.append(item[0])
        products_price.append(item[1])
        products_quantity.append(item[2])
    
    
    
    total_price = calculate_total_price(products_price, products_quantity)
    discount = calculate_discount(total_price, 5)

    print_receipt(products_name,products_price,products_quantity, total_price, discount)
    
        
process_order("0227")
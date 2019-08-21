import ShoppingMan_1.search_main
import ShoppingMan_2.BuyRecord_main

def shopping_1:
    while True:
        product = Shopping_Search
        print("구매하시고자 하는 물건이 \n"+product+" 가 맞으신가요?")
        cont = input("맞으시면 엔터 아니면 n을 입력하고 엔터를 누르세요")
        if cont =="":
            input("계속해서 구매를 진행하시려면 엔터를 아니면 n을 입력하고 엔터를 누르세요")
            if cont =="":  
        else:
            

def remove_shopping_list(shopping_list):
    for i in range(len(product)):
        print(i,product)
    del_i = input("제거하고자 하는 물건을 선택해주세요")
    while not del_i.isdigit():
        del_i = input("제거하고자 하는 물건의 순서를 숫자로 입력해주세요 \n1 미역 \n2 다시마 ...\n미역을 지우려면 1을 입력하세요")
    del_y = input(shopping_list[del_i]+"가 제거하고자 하는 물건이 맞나요? 맞으면 엔터 아니면 n을 입력하고 엔터를 누르세요")
    if del_y == "":
        del shopping_list[del_i]
    product = []
    continue

#main code block

print("쇼핑 검색을 해주는 쇼핑맨")
print("ver 0.1 2019-8-20-17:35수정")
while True:
    choice = input("1. 쇼핑 물건 검색      2. 구매내역      3. 종료")
    if choice == "1":
                


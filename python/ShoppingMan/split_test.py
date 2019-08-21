a = "https://search.shopping.naver.com/search/all.nhn?query=&cat_id=&frm=NVSHATC"

b = a.split("&")

b[0]+"세제"
a = ""
for i in range(len(b)-1):
    a = a+b[i]+'&'
print(a+b[-1])

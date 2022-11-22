import random
import datetime



def shutudai(qa_lst):
    qa = random.choice(qa_lst)
    print("問題:"+qa)
    return qa["a"]

def kaitou():
    st = datetime.datetime.now()
    ans = input("答えるんだ:")
    ed = datetime.datetime.now()

    if ans in ans_list:
        print("正解")
    else:
        print("出直してこい")
    
    #print("回答時間": + str((ed-st).seconds)+"秒")

if __name__=="__main__":
    qa_lst=[
        {"q":"サザエの旦那の名前は？","a":["マスオ","ますお"]},
        {"q":"カツオのもう都の名前は？","a":["ワカメ","わかめ"]},
        {"q":"タラオはカツオから見てどんな関係？","a":["甥","おい","甥っ子","おいっこ"]}
        ]
    ans_list=shutudai(qa_lst)
    kaitou(qa_lst)


'''
def shutudai():
    quiz=["サザエの旦那の名前は？","カツオのもう都の名前は？","タラオはカツオから見てどんな関係？"]
    masuo=["マスオ","ますお"]
    wakame=["ワカメ","わかめ"]
    oi=["甥","おい","甥っ子","おいっこ"]

    mondai=random.choice(quiz)
    

    if mondai == quiz[0]:
        ans = masuo
    elif mondai == quiz[1]:
        ans = wakame
    else:
        ans = oi
    
    return print(mondai)
    return ans

def kaitou():


shutudai()
imp = input("答えは？：")
print(ans)
if 
'''
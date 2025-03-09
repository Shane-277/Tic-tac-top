lis = ["1","2","3","4","5","6","7","8","9"]
def tic_tac_board(list):
    for i in range(3):
        print(list[i*3], "|", list[i*3+1],"|",list[i*3+2])
        print("-----------")

def main():
    count=0
    while True:
        a xiaqi



def check_winner(list):
    win_status=[
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    for xx in win_status:
        if list[xx[0]]!=" "and list[xx[0]]==list[xx[1]]==lis
        return list[xx[0]]

    if list[0]==list[1]==list[2]:


tic_tac_board(lis)
lis = ["1","2","3","4","5","6","7","8","9"]
def tic_tac_board(list):
    for i in range(3):
        print(list[i*3], "|", list[i*3+1],"|",list[i*3+2])
        print("-----------")

tic_tac_board(lis)
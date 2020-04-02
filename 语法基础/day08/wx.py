import itchat, time
def lc():
    print("Finash Login!")
def ec():
    print("exit")
itchat.auto_login(loginCallback=lc, exitCallback=ec)
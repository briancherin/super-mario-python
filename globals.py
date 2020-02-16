
def init():
    global mic_vol
    mic_vol = -1

def setVol(vol):
    global mic_vol
    mic_vol = vol

def getVol():
    global mic_vol
    return mic_vol
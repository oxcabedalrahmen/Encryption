from cryptography.fernet import Fernet
key="p2CvPls4JfrNPSvTJytrHnBlx2Ly9LUQ1rMF8hTSOj4="
up=Fernet(key)

def cy(x:str)->str:
    return up.encrypt(x.encode()).decode()


def de(x1:str)->str:
    return up.decrypt(x1.encode()).decode()

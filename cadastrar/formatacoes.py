import re

def formatar_cpf(cpf):
    cpf=re.sub(r'[^0-9]','',cpf)
    if len(cpf)==11:
        cpf=f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
        return cpf
    else:
        return False

def formatar_rg(rg):
    rg=re.sub(r'[^0-9]','',rg)
    if len(rg)==10:
        rg=f'{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8:]}'
        return rg
    else:
        return False
    
def formatar_data(data):
    data=re.sub(r'[^0-9]','',data)
    if len(data)==8:
        data=f'{data[:2]}/{data[2:4]}/{data[4:]}'
        return data
    else:
        return False

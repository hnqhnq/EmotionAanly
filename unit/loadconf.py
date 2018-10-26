from unit import context

def loadbase():
    ct = context.Context()
    ct.init('../conf/base.conf')
    basedic = {}
    basedic['usrhost'] = ct.getString('usrhost')
    basedic['un'] = ct.getInt('un')    
    basedic['dic'] = eval(ct.getString('dic'))
    
    return basedic
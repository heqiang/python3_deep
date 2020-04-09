class RounFloat(object):
    def __init__(self,val):
        assert isinstance(val,float),"必须是浮点数"
        "Value must be a float!"
        self.val=round(val,2)

rfm=RounFloat(10)
class GameUnitError(Exception):

    def __init__(self, message = '', code = 000):
        try:
            super().__init__(message)
        except TypeError:
            Exception.__init__(self,message)
        self.error_message = '~'*50 + '\n'
        
        self.error_dict = {
            000: "ERROR-000: Unspercified Error!",
            101: "ERROR-101: Health Meter Problem!",
            102: "ERROR-102: Attack issue! Ignored",
        }
        try:
            self.error_message += self.error_dict[code]
        except KeyError:
            self.error_message += self.error_dict[000]
        self.error_message += '\n' + '~'*50
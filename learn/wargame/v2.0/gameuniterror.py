class GameUnitError(Exception):

    def __init__(self, message = '', code = 000):
        try:
            super().__init__(message)
        except TypeError:
            Exception.__init__(self,message)
        self.error_message = '~'*50 + '\n'
        
        self.error_dict = {
            000: "ERROR-000: Unspercified Error!",
            101
        }
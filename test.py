# ### Funcion Sin Uso de Pytest
# def test(): 
#     a=16 
#     b=14 
#     try: 
#         assert a+1 == b 
#         print("test pass") 
#         return True 
#     except Exception as e: 
#         print("test failed") 
#         print("result:",a+1," not equal to:",b) 
#         return False 

# if __name__ == "__main__": 
#     test()

def test():
    a=13 
    b=14 

    assert a+1 == b,"Pass Test"

if __name__ == "__main__": 
    test()

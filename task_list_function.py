
def read_float(n):
    result=[]
    for i in range(n):
        num = float(input("enter a number:"))
        result.append(num)
    return result



def multiply(ls, factor):
    for i in range(len(ls)):
        ls[i] = ls[i]*factor
    return ls

def print_reverse(ls):
    ls.reverse()
    return ls


        
def main():
    my_list= read_float(3)
    number = int(input("Enter the factor: "))
    new_list =multiply(my_list, number)
    final_list = print_reverse(new_list)
    print(final_list)
    
main()
    

    


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

operator_dict={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
numb1=int(input("enter first number:"))
for symbol in operator_dict:
    print(symbol)
continue_flag=True
while continue_flag:
    op_symbol=input("pick an operation:")
    numb2=int(input("enter next number:"))
    calculator_function=operator_dict[op_symbol]
    output=calculator_function(numb1,numb2)
    print(f"{numb1} {op_symbol} {numb2}={output}")
    should_continue=input(f"Enter 'y' to continue calculation with {output} or 'n' to exit:").lower()
    if should_continue=='y':
       number1=output
    else:
        continue_flag=False
        print("Bye")

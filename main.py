import calc_pkg.ops as ops
import calc_pkg.formatting as fmt

op = input("Välj en operator (+, -, *, /): ")

a = int(input("Första talet: "))
b = int(input("Andra talet: "))


if op == "+":
    result = ops.add(a, b)
elif op == "-":
    result = ops.sub(a, b)
elif op == "*":
    result = ops.mul(a, b)
elif op == "/":
    result = ops.div(a, b)

print(fmt.pretty(op, a, b, result))
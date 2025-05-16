def salario_neto(salarioBruto):
    inss = salarioBruto * 0.07
    ir = (salarioBruto - inss) * 0.15
    salNeto = salarioBruto - inss - ir
    return salario_neto

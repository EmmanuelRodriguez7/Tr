#!/usr/bin/env python3
import de_numero_a_letra

str_numero = de_numero_a_letra.a_numero("99")
if str_numero == "cinco mil millones novecientos cincuenta y dos millones novecientos cuarenta y seis mil quinientos cuarenta y uno":
    print("OK")
else:
    print("BAD")

str_numero = de_numero_a_letra.a_numero("7")
if str_numero == "siete":
    print("OK")
else:
    print("BAD")

str_numero = de_numero_a_letra.a_numero("421")
if str_numero == "cuatrocientos veintiuno":
    print("OK")
else:
    print("BAD")
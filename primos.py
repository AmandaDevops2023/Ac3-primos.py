# Amanda Pagani Lima - RA:2200564
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def encontra_cem_primos():
    num = 3
    lista_primos = [2]
    is_primo = True

    while len(lista_primos) != 100:
        for divisor in range(2, num):
            if num % divisor == 0:
                is_primo = False
                break
        if is_primo:
            lista_primos.append(num)
        num += 1
        is_primo = True
    
    result = {"lista_primos": lista_primos, "qtd_primos": len(lista_primos)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
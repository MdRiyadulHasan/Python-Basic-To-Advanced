import re
dictionary = {"/^(4026|417500|4405|4508|4844|4913|4917)\d+$/":"electron", 'Talgvägen': 51, 'Malmstigen': 8, 'Huvudgatan': 3}
def detectCard(number):
    cardType = {
        "electron":"/^(4026|417500|4405|4508|4844|4913|4917)\d+$/",
        "maestercard":"^5[1-5][0-9]{14}|^(222[1-9]|22[3-9]\\d|2[3-6]\\d{2}|27[0-1]\\d|2720)[0-9]{12}$",
        "American Express":"^3[47][0-9]{13}$",
        "unionpay":"/^(4026|417500|4405|4508|4844|4913|4917)\d+$/",
        "visa":"^4[0-9]{12}(?:[0-9]{3})?$",
        "amex":"/^3[47][0-9]{13}$/",
        "diners":"",
        "discover":"/^6(?:011|5[0-9]{2})[0-9]{12}$/",
        "jcb":"/^(?:2131|1800|35\d{3})\d{11}$/",    
    }
    for k,v in cardType.items():
        r = re.compile(v)
        if re.match(r,number):
            return k
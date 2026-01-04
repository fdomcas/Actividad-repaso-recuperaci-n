


def procesar_ventas_diarias():
    ventas = {
        "lunes": [120, 150, 130],
        "martes": [200, 180, 220],
        "miercoles": [90, 110, 100],
        "jueves": [160, 170, 155]
    }

    res={"total":None,
         "dias buenos":None,
         "mejor dia": None
         } 
    catidades= [sum(ventas[dia]) for dia in ventas]
    res["total"]={dia:sum(ventas[dia]) for dia in ventas}
    res["dias buenos"]= [dia for dia in ventas if (sum(ventas[dia]) / len(ventas[dia]) >= 150)]
    res["mejor dia"]= [dia for dia in ventas if  sum(ventas[dia])== max(catidades)]

def calcular_articuls(*args, **kwargs):
    res = {
        "precio_articulo":None,
        "descuento":None,
        "IVA":None
    }
    res["total"]= sum(*args)

procesar_ventas_diarias()


def precio_comida(*args, **kwargs):
    """*platos: Tupla precios individuales (€)
    **descuentos: 
  - 'grupo': True/False (descuento grupo 10%)
  - 'fidelidad': nivel (bronze=0%, silver=5%, gold=15%)
  - 'horario': "tarde" (15%) o "normal" (0%)
  - 'iva_especial': True (10%) o False (21%)"""


    pedidos= []
    
    res={
        "pedido":{
            "items": len(*args),
             "subtotal":sum(*args),
             "plato_caro":{"precio": max(*args),
                           "posicion": [ind for ind, precio in enumerate(*args) if precio== max(*args)]
                           } 
        },
        "descuentos":{
            "grupo": None,
            "fidelidad": None, 
            "horario": None,
            "Total_ahorado": 0
        },
        "Inpuestos": {
            "iva_porcentaje": 21,
            "Importe_iva":None
        },
        "Total_final":None
    } 
    
    if kwargs.get("grupo"):
        res["descuentos"]["grupo"]=10
    else:
        res["descuentos"]["grupo"]=None



    if kwargs.get("fidelidad") == "bronze":
        res["descuentos"]["fidelidad"]= 0
    elif kwargs.get("fidelidad") == "silver":
        res["descuentos"]["fidelidad"]= 5
    elif kwargs.get("fidelidad") == "gold":
        res["descuentos"]["fidelidad"]= 15
    else:
        res["descuentos"]["fidelidad"]= None
    

    if kwargs.get("horario") == "tarde":
        res["descuentos"]["horario"]= 10
    elif kwargs.get("horario") == "normal":
        res["descuentos"]["horario"]= 0


    precio= res["pedido"]["subtotal"]

    if kwargs.get("grupo") and kwargs.get("fidelidad") and kwargs.get("horario"):
        
        subtotal= precio * (1 - res["descuentos"]["grupo"] / 100) * (1 - res["descuentos"]["fidelidad"] / 100) * (1 - res["descuentos"]["horario"] / 100)
        descuento= precio - subtotal
        res["descuentos"]["Total_ahorado"]= round(descuento,2)

    elif kwargs.get("fidelidad") and kwargs.get("horario"):
        subtotal= precio * (1 - res["descuentos"]["fidelidad"] / 100) * (1 - res["descuentos"]["horario"] / 100)
        descuento= precio - subtotal
        res["descuentos"]["Total_ahorado"]= round(descuento,2)

    elif kwargs.get("grupo") and kwargs.get("horario"):
        subtotal= precio * (1 - res["descuentos"]["grupo"] / 100) * (1 - res["descuentos"]["horario"] / 100)
        descuento= precio - subtotal
        res["descuentos"]["Total_ahorado"]= round(descuento,2)
    
    elif kwargs.get("grupo") and kwargs.get("fidelidad"):
        subtotal= precio * (1 - res["descuentos"]["grupo"] / 100) * (1 - res["descuentos"]["fidelidad"] / 100)
        descuento= precio - subtotal
        res["descuentos"]["Total_ahorado"]=round(descuento,2)

    elif kwargs.get("grupo"):
        
        subtotal= precio * (1 - res["descuentos"]["grupo"] / 100)
        descuento= precio - subtotal
        res["descuentos"]["Total_ahorado"]= round(descuento,2)
    elif  kwargs.get("fidelidad"):
        subtotal= precio * (1 - res["descuentos"]["fidelidad"] / 100)
        descuento= precio - subtotal
        res["descuentos"]["Total_ahorado"]= round(descuento,2)
    elif kwargs.get("horario"):
        
        subtotal= precio * (1 - res["descuentos"]["horario"] / 100)
        descuento= precio - subtotal
        res["descuentos"]["Total_ahorado"]= round(descuento,2)





    if kwargs.get("iva_especial"):
        res["Inpuestos"]["iva_porcentaje"]= kwargs.get("iva_especial")
    iva= round(1 -res["Inpuestos"]["iva_porcentaje"] / 100,21)
    print(iva)
    res["Inpuestos"]["Importe_iva"]=  round(res["pedido"]["subtotal"]  -(res["pedido"]["subtotal"] - res["descuentos"]["Total_ahorado"]) * iva, 2)

    res["Total_final"]= round((res["pedido"]["subtotal"] - res["descuentos"]["Total_ahorado"]) + res["Inpuestos"]["Importe_iva"], 2)
    
    pedidos.append(res)
    print(pedidos)
precio_comida((3,12,54), fidelidad="gold")









def processText(facturasText):
    from dataTransformers.textToFactura import textToFactura

    facturas = []
    for text in facturasText:
        factura = textToFactura(text)
        if factura:
            facturas.append(factura)
    return facturas

import re
from model.factura import Factura
import strings

patronRazonSocial = r"Raz.n Social: ([A-Za-z].*[A-Za-z])  *Fecha de.*"

r_CbteModo = r"CAE.?"
r_CuitEmisor = r"CUIT: ([0-9]{11})"
r_PtoVta = r"Punto de Venta: ([0-9]{4,5})"
r_CbteTipo = r""
r_CbteNro = r"Comp. Nro: ([0-9]{8})"
r_CbteFch = r"Fecha de Emisión: ([0-9]{2}/[0-9]{2}/[0-9]{4})"
r_ImpTotal = r"Importe Total:(?:.*) ([0-9]+(?:\,[0-9]{2})?)"
r_CodAutorizacion = r"CAE.? N°: ([0-9]{14})"
r_DocTipoReceptor = r""
r_DocNroReceptor = r"\n     CUIT: ([0-9]{11})"


def textToFactura(texto: str) -> Factura:
    try:
        CbteModo = buscarSubString(texto, r_CbteModo)[0]
        CuitEmisor = buscarSubString(texto, r_CuitEmisor)[0]
        PtoVta = buscarSubString(texto, r_PtoVta)[0]
        CbteTipo = "011"
        CbteNro = buscarSubString(texto, r_CbteNro)[0]
        CbteFch = buscarSubString(texto, r_CbteFch)[0]
        ImpTotal = buscarSubString(texto, r_ImpTotal)[0]
        CodAutorizacion = buscarSubString(texto, r_CodAutorizacion)[0]
        DocTipoReceptor = "80"
        DocNroReceptor = buscarSubString(texto, r_DocNroReceptor)[0]

        factura = Factura(CbteModo, CuitEmisor, PtoVta, CbteTipo, CbteNro,
                          CbteFch, ImpTotal, CodAutorizacion, DocTipoReceptor, DocNroReceptor)
        return factura
    except Exception as e:
        # print(f"{strings.ERROR_READ_PDF}: {e}")
        return None


def buscarSubString(context, patron):
    coincidencias = re.findall(patron, context)
    return coincidencias if coincidencias else None

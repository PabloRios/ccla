
class Factura:
    def __init__(self, cbte_modo, cuit_emisor, pto_vta, cbte_tipo, cbte_nro, cbte_fch,
                 imp_total, cod_autorizacion, doc_tipo_receptor, doc_nro_receptor):
        self.CbteModo = cbte_modo
        self.CuitEmisor = cuit_emisor
        self.PtoVta = pto_vta
        self.CbteTipo = cbte_tipo
        self.CbteNro = cbte_nro
        self.CbteFch = cbte_fch
        self.ImpTotal = imp_total
        self.CodAutorizacion = cod_autorizacion
        self.DocTipoReceptor = doc_tipo_receptor
        self.DocNroReceptor = doc_nro_receptor

    def __repr__(self):
        return (f"Factura(CbteModo={self.CbteModo}, CuitEmisor={self.CuitEmisor}, "
                f"PtoVta={self.PtoVta}, CbteTipo={self.CbteTipo}, CbteNro={self.CbteNro}, "
                f"CbteFch={self.CbteFch}, ImpTotal={self.ImpTotal}, "
                f"CodAutorizacion={self.CodAutorizacion}, "
                f"DocTipoReceptor={self.DocTipoReceptor}, DocNroReceptor={self.DocNroReceptor})")

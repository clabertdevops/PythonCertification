#Classe con @property
class StudenteProperty:
    def __init__(self, nome, eta):
        self._nome = nome
        self._eta = eta

    @property
    def eta(self):
        return self._eta

    @eta.setter
    def eta(self, valore):
        if valore < 0:
            raise ValueError("Età non valida")
        self._eta = valore


#Versione che in pratica spaccheta le property per vedere che cosa fanno effetivamete
class EtaDescriptor:
    def __get__(self, instance, owner):
        # equivale al getter
        return instance._eta

    def __set__(self, instance, valore):
        # equivale al setter
        if valore < 0:
            raise ValueError("Età non valida")
        instance._eta = valore

class StudenteDescriptor:
    eta = EtaDescriptor()   # 👈 descrittore dichiarato a livello di classe

    def __init__(self, nome, eta):
        self._nome = nome
        self._eta = eta

s_d = StudenteDescriptor("Descriptor", 20)

print(s_d.eta)    # → chiama EtaDescriptor.__get__
s_d.eta = 30      # → chiama EtaDescriptor.__set__

s_p = StudenteProperty("Property", 20)

print(s_p.eta)    # → chiama EtaDescriptor.__get__
s_p.eta = 30      # → chiama EtaDescriptor.__set__

#Versione più avanzata ma per uso didattico con il metodo "__getattribute__"

class StudenteAttribute:
    def __init__(self, nome, eta):
        # bypassiamo __setattr__
        super().__setattr__("_nome", nome)
        super().__setattr__("_eta", eta)

    def __getattribute__(self, name):
        if name == "eta":
            return super().__getattribute__("_eta")
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name == "eta":
            if not isinstance(value, int):
                raise TypeError("L'età deve essere un intero")
            if value < 0:
                raise ValueError("Età negativa")
            super().__setattr__("_eta", value)
        else:
            super().__setattr__(name, value)

    def __delattr__(self, name):
        if name == "eta":
            raise AttributeError("Non puoi eliminare l'età")
        super().__delattr__(name)

s_a = StudenteAttribute("Property", 20)

print(s_a.eta)    # → chiama EtaDescriptor.__get__
s_a.eta = 30      # → chiama EtaDescriptor.__set__

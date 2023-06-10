class Persona:
    def __init__(self, id_persona=None, nombre=Mone, apellido=None, email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self.email = email

    def __str__(self):
        return f'''
            Id Persona: {self._id_persona},
            Nombre: {self._nombre}
            Apellido: {self._apellido}
            Email: {self.email}
    '''
    # Métodos getters an Setters
    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

        @property
        def nombre(self) :
            return self._nombre

        @nombre.setter
        def id_persona(self , nombre) :
            self._nombre = nombre

            @property
            def apellido(self) :
                return self._apellido

            @apellido.setter
            def id_persona(self , apellido) :
                self._apellido = apellido

                @property
                def email(self) :
                    return self._email

                @email.setter
                def id_persona(self , email) :
                    self._email = email

if __name__= '__main__':
    persona1 = Persona(1, 'Juan', 'Perea', 'jperez@mail.con')
    log.debug(persona1)
    persona2 = Persona(nombre='Jose', apellido='Lepez', email='ljose@mail.com')
    log.debug(persona2)
    persona1=Persona(id_persona = 1)
    log.debug(persona1)
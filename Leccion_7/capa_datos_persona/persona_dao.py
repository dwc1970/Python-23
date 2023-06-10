import logging


class PersonaDAO:
    '''
    DAO significa : Data Access Objet
    CRUD significa :
                    Create -> Insertar
                    Read -> Seleccionar
                    Update -> Actualizar
                    Delete  -> Eliminar
    '''
    _SELECCIONAR = 'SELEC * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(id_persona, nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR =' UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR ='DELETE FROM persona WHERE id_persona=%s'

    # Definimos los métodos de la clase
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.ferchall()
                persona = [] # Creamos una lista
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    persona.append(persona)
                return personas




        @classmethod
        def insertar(cls, persona):
            with Conexion.obtenerConexion():
                with Conexion.obtenerConexion() as cursor:
                    valores = (persona.nombre, persona.apellido, persona.email)
                    cursor.execute(sls._INSERTAR, valores)
                    log.debug(f'Persona Insertada : {persona}')
                    return cursor.rowcount

        @classmethod
        def actualizar (cls, persona).
            with Conexion.obtenerConexion():
                with Conexion.obtenerCursor() as cursor:
                    valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona actualizada: {persona}')
                return cursor.rowcount


@classmethod
def eliminar (cls , persona).
    with Conexion.obtenerConexion ( ) :
        with Conexion.obtenerCursor ( ) as cursor :
        valores = (persona.nombre , persona.apellido , persona.email , persona.id_persona)
    cursor.execute ( cls._ELIMINAR , valores )
    log.debug ( f'Los objetos eliminados son : {persona}' )
    return cursor.rowcount



    if __name__ == '__main__':
        # Insertar un registro
        # Actualizar un registro
        #Eliminar un registro
        persona1 = persona(id_persona=13)
        personas_eliminadas = personaDAO.eliminar(persona1)
        log.debug(f'Personas eliminadas : {personas_eliminadas}')
        #persona1 = persona(1, 'Juan Jose', 'Pena', 'jjpena@mail.com' )
        #personas_actualizadas = personaDAO.actualizar(persona1)
        log.debug(f'Personas actualizadas: {personas_actualizadas}')
        #persona1 = Persona(nombre='Pedro', apellido='Romero', email='promero@mail.com')
       # personas_insertads = PersonaDAO(persona1)
        #log.debug(f'Personas insertadas: {personas_insertadas}')
        # Seleccionar objetos
        #personas = PersonaDAO.seleccionar()
        #for persona in personas:
         #   log.debug(persona)
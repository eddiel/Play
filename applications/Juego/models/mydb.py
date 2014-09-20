# coding: utf8

db.define_table('Tema', 
                Field ('Titulo',requires=(IS_SLUG(),IS_LOWER(),IS_NOT_IN_DB(db,'Tema.Titulo'))))

db.define_table('Pregunta',
               Field ('id_tema','reference Tema',readable=False,writable=False),
               Field ('pregunta',requires=IS_NOT_EMPTY()),
               Field('respuesta',requires=IS_NOT_EMPTY())
               )

db.define_table('Equipo',
                   Field('Nombre',requires=IS_NOT_EMPTY()),
                   Field ('score','integer'),
                   Field('racha','integer'))

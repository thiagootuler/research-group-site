
class Artigo:
    def __init__(self, titulo, autores, capa, miniatura, resumo, citacoes, qualis, doi):
        self._titulo = titulo
        self._autores = autores
        self._capa = capa
        self._miniatura = miniatura
        self._resumo = resumo
        self._citacoes = citacoes
        self._qualis = qualis
        self._doi = doi

    @property
    def titulo(self):
        return self._titulo

    @property
    def autores(self):
        return self._autores

    @property
    def capa(self):
        return self._capa

    @property
    def miniatura(self):
        return self._miniatura

    @property
    def resumo(self):
        return self._resumo

    @property
    def citacoes(self):
        return self._citacoes

    @property
    def qualis(self):
        return self._qualis

    @property
    def doi(self):
        return self._doi


class Membro:
    def __init__(self, nome, foto, lattes, nivel, resumo):
        self._nome = nome
        self._foto = foto
        self._lattes = lattes
        self._nivel = nivel
        self._resumo = resumo

    @property
    def nome(self):
        return self._nome

    @property
    def foto(self):
        return self._foto

    @property
    def lattes(self):
        return self._lattes

    @property
    def nivel(self):
        return self._nivel

    @property
    def resumo(self):
        return self._resumo


class Localizacao:
    def __init__(self, logradouro, numero, bairro, cidade, uf):
        self._logradouro = logradouro
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade
        self._uf = uf

    def __str__(self):
        return "{}, {} - {}, {}/{}".format(
            self._logradouro,
            self._numero,
            self._bairro,
            self._cidade,
            self._uf
        )


class Coordenada:
    def __init__(self, longitude, latitude, altitude):
        self._longitude = str(longitude)
        self._latitude = str(latitude)
        self._altitude = str(altitude)

    def __str__(self):
        return ','.join(self._longitude, self._latitude, self._altitude)


class Endereco:
    def __init__(self, nome, instituicao, departamento, localizacao, cep, coordenada):
        self._nome = nome
        self._instituicao = instituicao
        self._departamento = departamento
        self._localizacao = localizacao
        self._cep = cep
        self._coordenada = coordenada

    @property
    def nome(self):
        return self._nome

    @property
    def instituicao(self):
        return self._instituicao

    @property
    def departamento(self):
        return self._departamento

    @property
    def localizacao(self):
        return str(self._localizacao)

    @property
    def cep(self):
        cep = self._cep
        return "%s.%s - %s" % (cep[0:2], cep[2:5], cep[5:8])

    @property
    def coordenada(self):
        return str(self._coordenada)


class Contato:
    def __init__(self, endereco, telefone, email, mapa):
        self._endereco = endereco
        self._telefone = telefone
        self._email = email
        self._mapa = mapa

    @property
    def endereco(self):
        return self._endereco

    @property
    def telefone(self):
        tel = self._telefone
        return "(%s) %s - %s" % (tel[0:2], tel[2:6], tel[6:10])

    @property
    def email(self):
        return self._email

    @property
    def mapa(self):
        return self._mapa

import os
class CarregaDados():
    def __init__(self):
        self.apresentacao = """
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. <strong>Dignissimos exercitationem commodi</strong> sint excepturi ex quis ducimus sequi voluptatem possimus, odio nostrum cupiditate enim earum repellat, at expedita reiciendis assumenda veritatis. <em>Lorem</em>, <em>ipsum</em> e <em>dolor</em> sit amet consectetur adipisicing elit. Aperiam, magni?</p>
        <p>Atque unde sint velit, omnis iusto sequi. Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis, ratione fuga. Corporis, provident, cum eligendi atque aliquam non saepe laudantium odit soluta nostrum labore, voluptas fuga sit laboriosam veniam eos? Lorem ipsum dolor sit, amet consectetur adipisicing elit. Labore beatae, ut dolorum ipsum consequatur eveniet accusantium, in repellendus repudiandae assumenda animi voluptas quibusdam cumque ad architecto. Fugiat laboriosam eos quas!</p>
        <img class="mx-auto d-block pb-3" src="http://placehold.it/500x250">
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi autem provident velit repellat suscipit error rem similique possimus sit ad tempore voluptate eaque alias magni, a perferendis nesciunt tenetur amet! Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatum fugiat ut ullam, facilis deleniti repudiandae autem doloremque sapiente ipsa ipsam ea quo unde. Reprehenderit distinctio, incidunt quibusdam molestias ipsam impedit:</p>
        <ul>
            <li>Lorem ipsum dolor sit amet consectetur adipisicing elit.</li>
            <li>Mollitia ad quasi totam numquam.</li>
            <li>Voluptas corrupti quibusdam doloremque consequuntur est repellat cumque.</li>
            <li>Rem aliquam neque sapiente error voluptates debitis temporibus ducimus.</li>
        </ul>
        """
        self.artigo = Artigo(
            titulo="Titulo do artigo",
            autores=["Nome do Autor 1", "Nome do Autor 2"],
            capa="http://placehold.it/400x200?text=Graphical+Abstract",
            miniatura="http://placehold.it/85",
            resumo="Atque unde sint velit, omnis iusto sequi. Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis, ratione fuga. Corporis, provident, cum eligendi atque aliquam non saepe laudantium odit soluta nostrum labore, voluptas fuga sit laboriosam veniam eos? Lorem ipsum dolor sit, amet consectetur adipisicing elit. Labore beatae, ut dolorum ipsum consequatur eveniet accusantium, in repellendus repudiandae assumenda animi voluptas quibusdam cumque ad architecto. Fugiat laboriosam eos quas!",
            citacoes={
                'BibTeX': '@ARTICLE{nome, AUTHOR = {Nome do Autor},TITLE = {Titulo do artigo},PUBLISHER = {Revista},YEAR = {2020} }',
                'EndNote': '_'
            },
            qualis=0.0,
            doi="http://dx.doi.org/..."
        )
        self.publicacoes = [self.artigo] * 2
        membro = Membro(
            foto=os.path.join('static/images', 'perfil.png'),
            lattes="http://lattes.cnpq.br/",
            nome="Fulano de Tal",
            nivel="Doutorando",
            resumo="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quisquam consequatur autem rerum nam quaerat placeat cupiditate, atque enim expedita obcaecati, quae fugit tempora illum facilis neque id laboriosam, dolores sapiente."
        )
        self.membros = [membro for i in range(7)]
        self.contato = Contato(
            endereco = Endereco(
                nome="NOME Research Group",
                instituicao="Universidade Federal do Espírito Santo (UFES) - Campus de Alegre",
                departamento="Departamento de Ciências Florestais e da Madeira (DCFM)",
                localizacao=Localizacao("Av. Gov. Lindenberg", "316", "Centro", "Jerônimo Monteiro", "ES"),
                cep="29550000",
                coordenada=Coordenada(-20.7898091, -41.3897484, 19)
            ),
            telefone='0000000000',
            email="contato@mail.dominio.com",
            mapa="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1865.0067791136726!2d-41.38998983161366!3d-20.790739381509162!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xbbe71d08ccb731%3A0x43f2a4d6bcdc9cb3!2sDepartamento+de+Ci%C3%AAncias+Florestais+e+da+Madeira+-+CCAE%2FUFES!5e0!3m2!1spt-BR!2sbr!4v1556632159367!5m2!1spt-BR!2sbr"
        )
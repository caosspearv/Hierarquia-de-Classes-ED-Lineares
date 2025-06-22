from linear_structures_full import Queue
from datetime import datetime, timedelta

class UsuarioFila:
    def __init__(self, nome, tempo_medio_atendimento_min):
        self.nome = nome
        self.tempo_medio = timedelta(minutes=tempo_medio_atendimento_min)
        self.tempo_restante = None
        self.hora_entrada = None
        self.hora_prevista_retirada = None

    def __str__(self):
        tr = self.tempo_restante.total_seconds() / 60 if self.tempo_restante else None
        hpr = self.hora_prevista_retirada.strftime("%H:%M:%S") if self.hora_prevista_retirada else "N/A"
        return f"{self.nome} | Espera: {tr:.1f} min | Retirada prevista: {hpr}"

class FilaBandejao:
    def __init__(self, tempo_medio_atendimento_min=5):
        self.fila = Queue()
        self.tempo_medio_atendimento = timedelta(minutes=tempo_medio_atendimento_min)

    def tamanho(self):
        return self.fila.length()

    def tempo_espera_estimado(self):
        return self.tempo_medio_atendimento * self.tamanho()

    def entrar_na_fila(self, usuario: UsuarioFila):
        now = datetime.now()
        usuario.hora_entrada = now
        posicao = self.tamanho()
        usuario.tempo_restante = self.tempo_medio_atendimento * posicao
        usuario.hora_prevista_retirada = now + usuario.tempo_restante
        self.fila.insert_end(usuario)

    def desistir(self, nome_usuario):
        nova_fila = Queue()
        ajusta = False
        while not self.fila.is_empty():
            usuario = self.fila.remove_start()
            if usuario.nome == nome_usuario:
                ajusta = True
                continue
            nova_fila.insert_end(usuario)
        self.fila = nova_fila
        if ajusta:
            self._atualizar_tempos()

    def atender_usuario(self):
        if self.fila.is_empty():
            print("Fila vazia.")
            return None
        usuario = self.fila.remove_start()
        self._atualizar_tempos()
        return usuario

    def _atualizar_tempos(self):
        now = datetime.now()
        temp_fila = []
        while not self.fila.is_empty():
            temp_fila.append(self.fila.remove_start())
        for i, usuario in enumerate(temp_fila):
            usuario.tempo_restante = self.tempo_medio_atendimento * i
            usuario.hora_prevista_retirada = now + usuario.tempo_restante
            self.fila.insert_end(usuario)

    def visualizar_fila(self):
        usuarios = []
        temp_fila = []
        while not self.fila.is_empty():
            usuario = self.fila.remove_start()
            usuarios.append(usuario)
            temp_fila.append(usuario)
        for usuario in temp_fila:
            self.fila.insert_end(usuario)
        return usuarios

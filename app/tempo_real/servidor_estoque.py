import asyncio
import json
import threading

import websockets


class ServidorEstoque:

    def __init__(self, host='0.0.0.0', porta=8081):
        self.host = host
        self.porta = porta
        self._clientes = set()
        self._loop = None

    def iniciar(self):
        pronto = threading.Event()
        thread = threading.Thread(target=self._executar, args=(pronto,), daemon=True)
        thread.start()
        pronto.wait(timeout=5)

    def _executar(self, pronto):
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        self._loop.call_soon(pronto.set)
        self._loop.run_until_complete(self._servir())

    async def _servir(self):
        async with websockets.serve(self._atender, self.host, self.porta):
            await asyncio.Future()

    async def _atender(self, websocket):
        self._clientes.add(websocket)
        try:
            async for _ in websocket:
                pass
        finally:
            self._clientes.discard(websocket)

    def avisar(self, evento, produto):
        """Chamado pelo controller (thread do Bottle) apos criar/atualizar/excluir."""
        if self._loop is None:
            return
        dados = produto.to_dict()
        dados['preco_formatado'] = produto.preco_formatado
        mensagem = {'evento': evento, 'produto': dados}
        asyncio.run_coroutine_threadsafe(self._transmitir(mensagem), self._loop)

    async def _transmitir(self, mensagem):
        if not self._clientes:
            return
        payload = json.dumps(mensagem, ensure_ascii=False)
        await asyncio.gather(
            *(cliente.send(payload) for cliente in self._clientes),
            return_exceptions=True,
        )

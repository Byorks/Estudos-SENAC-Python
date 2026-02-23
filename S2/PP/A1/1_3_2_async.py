import asyncio

async def tarefa_principal(callback):
    print('Executando tarefa principal')
    await asyncio.sleep(2)
    print('Tarefa concluída')
    callback()
    
def meu_callback():
    print("Callback executado após minha função assíncrona")
    
asyncio.run(tarefa_principal(meu_callback))
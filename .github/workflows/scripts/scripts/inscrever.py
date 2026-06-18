import json
import sys
from datetime import datetime
from pathlib import Path

ARQUIVO = Path(__file__).parent.parent / "subscribers.json"


def carregar():
    if not ARQUIVO.exists():
        return []
    return json.loads(ARQUIVO.read_text())


def salvar(dados):
    ARQUIVO.write_text(json.dumps(dados, ensure_ascii=False, indent=2))


def adicionar(email: str, nome: str = ""):
    dados = carregar()
    if email.lower() in [s["email"].lower() for s in dados]:
        print(f"{email} ja esta inscrito.")
        return
    dados.append({
        "nome": nome,
        "email": email.lower(),
        "ativo": True,
        "inscrito_em": datetime.now().strftime("%Y-%m-%d"),
    })
    salvar(dados)
    print(f"{email} adicionado.")


def remover(email: str):
    dados = carregar()
    antes = len(dados)
    dados = [s for s in dados if s["email"].lower() != email.lower()]
    if len(dados) == antes:
        print(f"{email} nao encontrado.")
        return
    salvar(dados)
    print(f"{email} removido.")


def listar():
    dados = carregar()
    ativos = [s for s in dados if s.get("ativo", True)]
    print(f"\n{len(ativos)} inscrito(s):\n")
    for s in ativos:
        print(f"  {s['email']}  {s.get('nome', '')}  ({s.get('inscrito_em', '')})")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python inscrever.py adicionar email@exemplo.com 'Nome'")
        print("     python inscrever.py remover  email@exemplo.com")
        print("     python inscrever.py listar")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "adicionar" and len(sys.argv) >= 3:
        nome = sys.argv[3] if len(sys.argv) > 3 else ""
        adicionar(sys.argv[2], nome)
    elif cmd == "remover" and len(sys.argv) >= 3:
        remover(sys.argv[2])
    elif cmd == "listar":
        listar()

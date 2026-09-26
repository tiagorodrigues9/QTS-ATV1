import typing

class Ticket:
    VALID_PRIORITIES = {"baixa", "media", "alta", "critica"}

    def __init__(self, id: int, priority: str, cost: float, description: str):
        if priority not in self.VALID_PRIORITIES:
            raise ValueError(f"Prioridade inválida: {priority}. Valores válidos: {self.VALID_PRIORITIES}")
        if cost < 0:
            raise ValueError("O custo do chamado não pode ser negativo.")
        if not description or not description.strip():
            raise ValueError("A descrição do chamado não pode ser vazia ou apenas espaços.")
        
        self.id = id
        self.priority = priority
        self.cost = cost
        self.description = description.strip()


def approve_ticket(ticket: Ticket, user_role: str) -> bool:
    valid_roles = {"funcionario", "gerente", "admin"}
    if user_role not in valid_roles:
        raise ValueError(f"Papel de usuário inválido: {user_role}. Valores válidos: {valid_roles}")

    # Regra 1: Custo Máximo (Sempre requer admin)
    if ticket.cost >= 1000.0:
        return user_role == "admin"
    
    # Regra 2: Prioridade Crítica (Sempre requer admin)
    if ticket.priority == "critica":
        return user_role == "admin"

    # Regra 3: Prioridade Alta (Requer gerente ou admin)
    if ticket.priority == "alta":
        return user_role in {"gerente", "admin"}

    # Regra 4: Prioridade Média e Baixa
    if ticket.priority in {"media", "baixa"}:
        if ticket.cost < 100.0:
            return True  # Qualquer papel pode aprovar
        else:
            return user_role in {"gerente", "admin"}

    return False

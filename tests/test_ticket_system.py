import pytest
from app.ticket_system import Ticket, approve_ticket

@pytest.mark.unit
class TestTicketValidation:
    
    # BVA: Custo negativo
    def test_create_ticket_negative_cost_raises_error(self):
        # Arrange
        cost = -0.01
        
        # Act & Assert
        with pytest.raises(ValueError, match="O custo do chamado não pode ser negativo."):
            Ticket(id=1, priority="baixa", cost=cost, description="Valid")

    # EP: Prioridade inválida, Error Guessing
    @pytest.mark.parametrize("invalid_priority", ["", "urgente", "  ", "BAIXA"])
    def test_create_ticket_invalid_priority_raises_error(self, invalid_priority):
        # Arrange
        # Act & Assert
        with pytest.raises(ValueError, match="Prioridade inválida"):
            Ticket(id=1, priority=invalid_priority, cost=50.0, description="Valid")

    # EP: Descrição inválida, Error Guessing
    @pytest.mark.parametrize("invalid_desc", ["", "   ", "\t", "\n"])
    def test_create_ticket_invalid_description_raises_error(self, invalid_desc):
        # Arrange
        # Act & Assert
        with pytest.raises(ValueError, match="A descrição do chamado não pode ser vazia"):
            Ticket(id=1, priority="baixa", cost=50.0, description=invalid_desc)

    # Valid creation
    def test_create_ticket_valid(self):
        # Arrange
        # Act
        ticket = Ticket(id=1, priority="alta", cost=150.0, description="  Needs fixing  ")
        
        # Assert
        assert ticket.id == 1
        assert ticket.priority == "alta"
        assert ticket.cost == 150.0
        assert ticket.description == "Needs fixing"

@pytest.mark.unit
class TestApproveTicket:
    
    # EP: Papel inválido
    @pytest.mark.parametrize("invalid_role", ["", "ceo", "ADMIN", "  "])
    def test_approve_ticket_invalid_role_raises_error(self, invalid_role):
        # Arrange
        ticket = Ticket(id=1, priority="baixa", cost=50.0, description="Valid")
        
        # Act & Assert
        with pytest.raises(ValueError, match="Papel de usuário inválido"):
            approve_ticket(ticket, user_role=invalid_role)

    # Regra 1: Custo >= 1000 requer admin (BVA: 999.99, 1000.0, 1000.01)
    @pytest.mark.parametrize("cost, role, expected", [
        (1000.0, "admin", True),
        (1000.0, "gerente", False),
        (1000.0, "funcionario", False),
        (1000.01, "admin", True),
        (5000.0, "gerente", False)
    ])
    def test_approve_ticket_high_cost(self, cost, role, expected):
        # Arrange
        ticket = Ticket(id=1, priority="baixa", cost=cost, description="Valid")
        # Act
        result = approve_ticket(ticket, role)
        # Assert
        assert result == expected

    # Regra 2: Prioridade Critica requer admin
    @pytest.mark.parametrize("role, expected", [
        ("admin", True),
        ("gerente", False),
        ("funcionario", False),
    ])
    def test_approve_ticket_critical_priority(self, role, expected):
        # Arrange
        # Using cost < 1000 to isolate priority rule
        ticket = Ticket(id=1, priority="critica", cost=500.0, description="Valid")
        # Act
        result = approve_ticket(ticket, role)
        # Assert
        assert result == expected

    # Regra 3: Prioridade Alta requer gerente ou admin
    @pytest.mark.parametrize("role, expected", [
        ("admin", True),
        ("gerente", True),
        ("funcionario", False),
    ])
    def test_approve_ticket_high_priority(self, role, expected):
        # Arrange
        # Using cost < 1000 to isolate priority rule
        ticket = Ticket(id=1, priority="alta", cost=500.0, description="Valid")
        # Act
        result = approve_ticket(ticket, role)
        # Assert
        assert result == expected

    # Regra 4: Prioridade media/baixa com custo < 100
    @pytest.mark.parametrize("priority", ["baixa", "media"])
    @pytest.mark.parametrize("role", ["admin", "gerente", "funcionario"])
    def test_approve_ticket_low_medium_priority_low_cost(self, priority, role):
        # Arrange
        # BVA: cost < 100 (99.99, 0.0)
        ticket = Ticket(id=1, priority=priority, cost=99.99, description="Valid")
        # Act
        result = approve_ticket(ticket, role)
        # Assert
        assert result == True

    # Regra 4: Prioridade media/baixa com custo >= 100 (e < 1000)
    @pytest.mark.parametrize("priority", ["baixa", "media"])
    @pytest.mark.parametrize("role, expected", [
        ("admin", True),
        ("gerente", True),
        ("funcionario", False),
    ])
    def test_approve_ticket_low_medium_priority_medium_cost(self, priority, role, expected):
        # Arrange
        # BVA: cost >= 100 (100.0, 999.99)
        ticket = Ticket(id=1, priority=priority, cost=100.0, description="Valid")
        # Act
        result = approve_ticket(ticket, role)
        # Assert
        assert result == expected

    # Regra para fallback / error guessing
    def test_approve_ticket_unknown_priority(self):
        # Arrange
        ticket = Ticket(id=1, priority="baixa", cost=50.0, description="Valid")
        ticket.priority = "desconhecida" # Mutating to bypass validation
        # Act
        result = approve_ticket(ticket, "admin")
        # Assert
        assert result == False

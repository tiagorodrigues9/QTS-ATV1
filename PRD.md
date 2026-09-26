# Product Requirements Document (PRD) - Sistema de Aprovação de Chamados de Suporte

## 1. Visão Geral
Este sistema tem como objetivo automatizar e validar a aprovação de chamados de suporte técnico, aplicando regras de negócio baseadas no papel do usuário (role), custo associado ao chamado e a prioridade do mesmo.

## 2. Entidades
### 2.1. Chamado (Ticket)
- `id`: Inteiro, identificador único do chamado.
- `priority`: String, prioridade do chamado. Valores válidos: `'baixa'`, `'media'`, `'alta'`, `'critica'`.
- `cost`: Float, custo estimado do chamado. Deve ser >= 0.
- `description`: String, descrição do chamado. Não pode ser vazia ou conter apenas espaços.

### 2.2. Usuário (User)
- `role`: String, papel do usuário avaliador. Valores válidos: `'funcionario'`, `'gerente'`, `'admin'`.

## 3. Regras de Negócio e Aprovação
A função de aprovação avalia um `Ticket` e o `role` do usuário que está tentando aprovar, retornando `True` se aprovado, ou `False` caso não tenha permissão (ou levantando exceções se as regras de validação falharem).

### Regras de Validação (Tratamento Defensivo)
1. **Prioridade Inválida**: Se a prioridade não for uma das válidas, levantar `ValueError`.
2. **Custo Inválido**: Se o custo for menor que 0, levantar `ValueError`.
3. **Descrição Inválida**: Se a descrição for vazia ou conter apenas espaços, levantar `ValueError`.
4. **Papel Inválido**: Se o papel do usuário não for um dos válidos, levantar `ValueError`.

### Regras de Autorização
1. **Regra de Custo Máximo**: Qualquer chamado com `cost >= 1000.0` requer obrigatoriamente o papel `'admin'`. Se for outro papel, a aprovação é negada (retorna `False`).
2. **Prioridade Crítica**: Chamados de prioridade `'critica'` exigem o papel `'admin'`, independentemente do custo (mas ainda obedecendo à regra 1).
3. **Prioridade Alta**: Chamados de prioridade `'alta'` podem ser aprovados por `'gerente'` ou `'admin'`.
4. **Prioridade Média e Baixa**:
   - Se `cost < 100.0`, podem ser aprovados por qualquer papel (`'funcionario'`, `'gerente'` ou `'admin'`).
   - Se `cost >= 100.0` (mas < 1000.0, pela regra 1), exigem `'gerente'` ou `'admin'`.

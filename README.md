# Sistema de Aprovação de Chamados de Suporte (QTS - ATV1)

Este repositório contém a entrega da **Atividade Prática 1 (ATV1)** da disciplina de **Qualidade e Teste de Software (QTS)**. O objetivo deste projeto é aplicar na prática os conceitos de Engenharia de Testes Unitários, Cobertura de Código e Governança de IA no desenvolvimento de um sistema de avaliação de chamados.

## 📋 Sobre o Projeto

O domínio implementado é um sistema de suporte técnico que aprova ou rejeita a abertura de chamados (Tickets) com base em **Regras de Negócio** pré-definidas. O sistema analisa as propriedades do chamado (Custo e Prioridade) e o Nível de Acesso (Papel/Role) do usuário que está validando a operação.

### Documentações de Apoio
- 📄 **[PRD.md](./PRD.md)**: Product Requirements Document contendo todas as regras de negócio de validação e de autorização.
- 🤖 **[AI_USAGE.md](./AI_USAGE.md)**: Relatório de Transparência que descreve como a IA foi utilizada como ferramenta de apoio durante o planejamento, desenvolvimento e testes.
- ⚙️ **[.cursorrules](./.cursorrules)**: Regras de contexto utilizadas para governança de geração de código, garantindo uso do padrão AAA e validação rigorosa (Defensive Programming).

## 🚀 Tecnologias e Ferramentas

- **Linguagem**: Python 3.12+ (Utilizando Type Hints rigorosos)
- **Gerenciamento de Pacotes**: [uv](https://github.com/astral-sh/uv) (Extremamente rápido e moderno)
- **Framework de Testes**: `pytest`
- **Cobertura de Código**: `pytest-cov`

## 🧪 Estratégias de Testes Aplicadas

A suíte de testes unitários foi elaborada seguindo rigorosamente o padrão **AAA (Arrange, Act, Assert)** e cobre 100% dos caminhos lógicos do código (incluindo ramificações).
As técnicas utilizadas incluem:
- **Particionamento de Equivalência (EP)**: Agrupamento de prioridades válidas/inválidas e diferentes papéis de usuário.
- **Análise do Valor Limite (BVA)**: Casos de teste desenvolvidos exatamente sobre as fronteiras de decisão das regras financeiras (ex: `-0.01`, `0`, `99.99`, `100.00`, `999.99` e `1000.00`).
- **Error Guessing**: Testes propositais com propriedades nulas, espaços em branco, papéis inventados e injeção tardia de propriedades inválidas visando resiliência.

---

## 💻 Como Executar

### 1. Pré-requisitos
Certifique-se de ter o gerenciador **`uv`** instalado em sua máquina. Caso não tenha, [siga as instruções de instalação aqui](https://github.com/astral-sh/uv).

### 2. Rodando os Testes
Para rodar a suíte completa de testes no modo verbose e atestar os 38 cenários de aprovação:

```bash
uv run pytest -v
```

### 3. Relatório de Cobertura
Para atestar a medição de 100% de cobertura de código (linhas e ramificações condicionais) do pacote principal `app`:

```bash
uv run pytest --cov=app --cov-branch --cov-report=term-missing
```

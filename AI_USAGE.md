# Relatório de Transparência - Uso de IA

## Ferramenta Utilizada

O desenvolvimento deste projeto contou com o auxílio do **Gemini 3.1 Pro (High) / Antigravity**, utilizado como ferramenta de apoio durante as etapas de planejamento, implementação e testes do sistema.

A utilização da IA teve como objetivo auxiliar na elaboração de código, estruturação dos testes e identificação de possíveis cenários, enquanto as decisões relacionadas às regras de negócio, organização do projeto, revisão e validação dos resultados foram realizadas durante o desenvolvimento do projeto.

## Como a IA foi Empregada

A Inteligência Artificial foi utilizada como ferramenta de apoio nas seguintes etapas do ciclo de desenvolvimento:

1. **Definição de Requisitos**: auxílio na organização e estruturação inicial do PRD (Product Requirements Document), a partir das regras de negócio definidas para o escopo de **"Aprovação de Chamados"**. As regras e critérios utilizados foram analisados e ajustados durante o desenvolvimento.

2. **Implementação do Domínio (SUT)**: utilização da IA como apoio na elaboração do código Python (`app/ticket_system.py`), contendo a classe `Ticket` e as funções de avaliação. Durante essa etapa, o código foi analisado e ajustado conforme as necessidades do projeto, incluindo o uso de Type Hints (`typing`) e tratamento de exceções (`ValueError`).

3. **Engenharia de Testes**:

   * Auxílio na criação e organização da suite de testes (`tests/test_ticket_system.py`) utilizando `pytest`.
   * Estruturação dos casos de teste seguindo o padrão AAA (Arrange, Act, Assert).
   * Aplicação de técnicas de **Particionamento de Equivalência (EP)** para dividir custos e prioridades em classes testáveis.
   * Aplicação de **Análise do Valor Limite (BVA)**, considerando valores nas fronteiras das regras, como `0`, `99.99`, `100.00`, `999.99` e `1000.00`.
   * Utilização de **Error Guessing** para verificar situações como valores em branco, papéis inválidos e prioridades inexistentes.
   * Utilização das marcações `@pytest.mark.parametrize` e `@pytest.mark.unit`.

   Os cenários de teste foram analisados e selecionados de acordo com as regras definidas para o sistema, utilizando as sugestões da IA como apoio durante essa etapa.

4. **Automação do Ambiente e Cobertura**: auxílio na configuração do projeto utilizando a ferramenta `uv` e na verificação da cobertura de código por meio do `pytest-cov` com a opção `--cov-branch`. A cobertura de 100% foi posteriormente verificada por meio da execução dos testes.

## Participação e Auditoria do Desenvolvimento

Embora a Inteligência Artificial tenha sido utilizada como ferramenta de apoio em diferentes etapas, o desenvolvimento não foi realizado de forma totalmente autônoma pela ferramenta. As regras de negócio, decisões sobre o comportamento esperado do sistema, análise dos casos de teste e validação dos resultados fizeram parte do processo de desenvolvimento.

Após a geração e sugestão de trechos de código e testes pela IA, foi realizada uma auditoria do material produzido, contemplando:

* **Análise Estática**: revisão do código para verificar a utilização adequada de Type Hints, organização das funções e aderência às regras de negócio estabelecidas.

* **Validação Funcional**: execução do comando `pytest` localmente para verificar se os testes apresentavam os resultados esperados e se as funcionalidades implementadas estavam de acordo com os requisitos.

* **Auditoria de Cobertura**: execução do relatório de cobertura por meio de `pytest --cov=app --cov-branch`, verificando a cobertura das linhas e dos ramos condicionais.

* **Revisão dos Testes**: análise dos cenários propostos para verificar se contemplavam as diferentes classes de equivalência, valores limites e possíveis entradas inválidas.

Dessa forma, a IA foi utilizada como **ferramenta de assistência ao desenvolvimento**, contribuindo para a geração de sugestões de implementação e testes, enquanto a definição das regras, análise, revisão, ajustes e validação final fizeram parte da participação humana no desenvolvimento do projeto.

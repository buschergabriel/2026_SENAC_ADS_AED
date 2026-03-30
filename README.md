# 🎓 Algoritmos e Estruturas de Dados — SENAC ADS

![Status](https://img.shields.io/badge/Status-Em%20Progresso-blue)
![Semestre](https://img.shields.io/badge/Semestre-3º-brightgreen)
![Professor](https://img.shields.io/badge/Professor-Adalto%20Sparremberger-orange)

> Repositório com anotações, exemplos de código e resumos das aulas de **Algoritmos e Estruturas de Dados I** — SENAC ADS 2026, turma noturna.

## 📚 Aulas

| Aula | Tópico | Status | Data | Link |
|------|--------|--------|------|------|
| 01 | Memória e Tipos em C | ✅ Assistida | 24/03 | [➜ Ir](./aula-01-memoria-tipos/) |
| 02 | Alocação Dinâmica, Nós e Ponteiros | ✅ Assistida | 27/03 | [➜ Ir](./aula-02-nos-ponteiros/) |
| 03 | Operações em Listas: Inserção e Relinking | ✅ Assistida | 28/03 | [➜ Ir](./aula-03-operacoes-insercao/) |
| 04 | Complexidade de Algoritmos (Big O) | ✅ Assistida | 29/03 | [➜ Ir](./aula-04-complexidade/) |
| 05 | Pilhas (LIFO) / Filas (FIFO) | 🔄 Próxima | 31/03 | [➜ Ir](./aula-05-pilhas-filas/) |

## 🎯 Como Usar Este Repositório

1. **Para cada aula**: Acesse a pasta da aula (ex: `aula-01-memoria-tipos/`)
2. **Leia o README** dentro de cada pasta — resumo visual e conceitos-chave
3. **Copie e execute o `.c`** para praticar em casa
4. **Adicione suas anotações** no `notas.txt`

## 🛠️ Pré-requisitos

- **Compilador C**: GCC ou Clang
- **Editor**: VS Code, Code::Blocks, Dev-C++ (ou terminal + Vim)
- **Conhecimento**: Lógica de programação (C básico)

## 🔧 Como Compilar e Executar

```bash
# Exemplo: compilar exemplo da Aula 01
cd aula-01-memoria-tipos/
gcc exemplos.c -o exemplos
./exemplos
```

## 📖 Estrutura de Cada Aula

Cada pasta de aula segue este padrão:

- **README.md**: Resumo visual + tabela de conceitos + perguntas-chave
- **exemplos.c** ou **[arquivo].c**: Código comentado, pronto para executar
- **notas.txt**: Anotações do aluno (suas observações em sala)

## 🤔 Perguntas-Chave Por Aula

### Aula 01: Memória e Tipos
- [ ] Quantos bytes ocupa um `int`?
- [ ] Por que `char` é mais eficiente que `int` para números pequenos?
- [ ] O que é endereçamento de memória?

### Aula 02: Nós e Ponteiros
- [ ] Como criar um nó em C usando `malloc`?
- [ ] O que `->` faz em C?
- [ ] Qual é a diferença entre `*ptr` e `&var`?

### Aula 03: Inserção Ordenada
- [ ] Como fazer relinking sem perder referências?
- [ ] Por que inserção no início é O(1) mas no meio é O(n)?
- [ ] O que acontece se você errar o relinking?

### Aula 04: Big O
- [ ] Array é O(1) para acesso. Por quê?
- [ ] Lista Encadeada é O(n) para acesso. Por quê?
- [ ] O que é melhor: Array ou Lista? Depende de quê?

### Aula 05: Pilhas / Filas
- [ ] Qual é a regra LIFO e FIFO?
- [ ] Uma pilha pode usar um array estático?
- [ ] Uma fila precisa de dois ponteiros? Por quê?

## 📚 Recursos Externos

- **[Notion - Dashboard de Aprendizado](https://www.notion.so/ba2f8db71bd74a5b9c07e4064e649885)** — Aulas, competências, habilidades
- **[NotebookLM - Caderno](https://notebooklm.google.com/notebook/a2445aef-b6d5-44d6-a4c9-9e02e5f40127)** — Material completo com IA
- **[GitHub Professor](https://github.com/assparremberger/2026_1_Algotirmos_Estruturas_Dados_I_noite)** — Código oficial e slides
- **[Blackboard SENAC](https://blackboard.senac.br)** — Material e cronograma

## 🚀 Commit Strategy

Após cada aula, faça commit:

```bash
git add aula-XX-*/
git commit -m "Aula XX: [Tópico] - [Data]"
git push origin main
```

**Exemplo**:
```bash
git commit -m "Aula 01: Memória e Tipos em C - 24/03"
```

## 📊 Status Geral

```
✅ Aula 01: Pronto
✅ Aula 02: Pronto
✅ Aula 03: Pronto
✅ Aula 04: Pronto
🔄 Aula 05: Em andamento (31/03)
```

## 👨‍💼 Autor

Gabriel Buscher de Oliveira  
📍 Viamão, RS  
🎓 SENAC ADS — 3º Semestre (2026)

## 📄 Licença

Este repositório é apenas para fins educacionais.

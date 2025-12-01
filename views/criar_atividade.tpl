% rebase('layout', title='Criar Atividade')

<h2>Criar Atividade</h2>
<form method="post" action="/criar_atividade">
  <label for="titulo">Título:</label>
  <input type="text" id="titulo" name="titulo" required><br>

  <label for="descricao">Descrição:</label>
  <textarea id="descricao" name="descricao" rows="4" required></textarea><br>

  <label for="disciplina">Disciplina:</label>
  <input type="text" id="disciplina" name="disciplina" required><br>

  <label for="prazo">Prazo (YYYY-MM-DD):</label>
  <input type="date" id="prazo" name="prazo" required><br>

  <button type="submit">Criar</button>
</form>

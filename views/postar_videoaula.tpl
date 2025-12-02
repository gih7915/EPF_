% rebase('layout', title='Postar Videoaula')

<h2>Postar Videoaula</h2>
<form method="post" action="/postar_videoaula">
  <label for="titulo">Título:</label>
  <input type="text" id="titulo" name="titulo" required><br>

  <label for="link">Link:</label>
  <input type="url" id="link" name="link" required><br>

  <label for="disciplina">Disciplina:</label>
  <input type="text" id="disciplina" name="disciplina" required><br>

  <label for="descricao">Descrição:</label>
  <textarea id="descricao" name="descricao" rows="4"></textarea><br>

  <button type="submit">Publicar</button>
</form>

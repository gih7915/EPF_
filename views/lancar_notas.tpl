% rebase('layout', title='Lançar Notas')

<h2>Lançar Notas</h2>
<form method="post" action="/lancar_notas">
    <label for="disciplina">Disciplina:</label>
    <input type="text" id="disciplina" name="disciplina" required><br>
    <label for="aluno">Aluno:</label>
    <input type="text" id="aluno" name="aluno" required><br>
    <label for="nota">Nota:</label>
    <input type="number" id="nota" name="nota" min="0" max="10" step="0.1" required><br>
    <button type="submit">Lançar Nota</button>
</form>
